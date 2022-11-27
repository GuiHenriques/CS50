import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, new_symbol

from datetime import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Get variables values
    info = db.execute("SELECT * FROM display WHERE user_id = ?", session["user_id"])

    for data in info:
        data["value"] = data["shares"] * data["price"]

    cash = float(db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"])
    total = db.execute("SELECT shares, price FROM display WHERE user_id = ?", session["user_id"])

    # Get sum of all stocks
    stock_sum = 0
    for stock in total:
        stock_sum += stock["shares"] * stock["price"]

    soma = stock_sum + cash

    time_now = datetime.now().strftime("%b %d %H:%M")
    return render_template("index.html", info=info, cash=cash, soma=soma, time=time_now)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()

        info = lookup(symbol)

        if info == None:
            return apology("This stock symbol doesn't exist")

        shares = request.form.get("shares")
        if not shares:
            return apology("The number of shares must be a positive integer")

        try:
            shares = int(shares)
        except:
            return apology("The number of shares must be a positive integer")

        if shares < 1:
            return apology("The number of shares must be a positive integer")

        price = info["price"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

        if price * shares > cash:
            return apology("You don't have enough money to do this")

        # Call function to check existing symbol
        new = new_symbol(symbol, session["user_id"])

        # Track Time
        time_now = datetime.now().strftime("%b %d %H:%M")

        if new:
            # If new symbol insert new row in table
            db.execute("INSERT INTO display (user_id, symbol, shares, price, time) VALUES (?, ?, ?, ?, ?)",
                       session["user_id"], symbol, shares, price, time_now)
        else:
            # If existing symbol update table
            shares_old = int(db.execute("SELECT * FROM display WHERE symbol = ?", symbol)[0]["shares"])
            shares += shares_old
            db.execute("UPDATE display SET shares = ?, time = ? WHERE symbol = ?", shares, time_now, symbol)

        cash = cash - price * shares
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        # Remember in history
        db.execute("INSERT INTO history (user_id, symbol, shares, price, time, type) VALUES(?, ?, ?, ?, ?, ?)",
                   session["user_id"], symbol, shares, price, time_now, "Buy")

        return redirect("/")

    else:
        return render_template("/buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    info = db.execute("SELECT * FROM history")
    return render_template("history.html", info=info)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        username = request.form.get("username")
        if not username:
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Change the current user password"""

    if request.method == "GET":
        return render_template("password.html")

    else:
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check missing input fields
        if not password or not confirmation:
            return apology("Missing input field")

        # Check if passwords match
        if password != confirmation:
            return apology("Passwords do not match")

        # Update database
        db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(password), session["user_id"])

        return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)

        if quote == None:
            return apology("This stock symbol doesn't exist")

        return render_template("quoted.html", quote=quote)
    else:
        # GET
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check missing input fields
        if not username or not password or not confirmation:
            return apology("Missing input field")

        # Check if passwords match
        if password != confirmation:
            return apology("Passwords do not match")

        # Insert new user to database
        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
        except:
            return apology("Username is already taken")

        session["user_id"] = new_user

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    stocks = db.execute("SELECT symbol, shares FROM display WHERE user_id = ?", session["user_id"])

    # Create list of all symbols
    symbols = []
    for symbol in stocks:
        symbols.append(symbol["symbol"])

    if request.method == "POST":

        symbol = request.form.get("symbol")
        if symbol not in symbols:
            return apology("Invalid Symbol", 403)

        shares = int(request.form.get("shares"))
        current_shares = db.execute("SELECT shares FROM display WHERE symbol = ? AND user_id = ?",
                                    symbol, session["user_id"])[0]["shares"]

        if shares > current_shares:
            return apology("You don't have enough shares to do this", 403)
        if shares < 1:
            return apology("You can't sell a negative number of shares", 403)

        # Sell shares
        new_shares = current_shares - shares

        # Calculate cash and price
        current_cash = db.execute("SELECT cash FROM users WHERE id = ?",
                                  session["user_id"])[0]["cash"]
        price = lookup(symbol)["price"]
        cash_received = price * shares
        new_cash = current_cash + cash_received

        # Update shares, stock price and cash
        db.execute("UPDATE display SET shares = ?, price = ? WHERE symbol = ? AND user_id = ?",
                   new_shares, price, symbol, session["user_id"])
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, session["user_id"])

        # Purchase time
        time = datetime.now().strftime("%b %d %H:%M")

        # Remeber in history
        db.execute("INSERT INTO history (user_id, symbol, shares, price, time, type) VALUES(?, ?, ?, ?, ?, ?)",
                   session["user_id"], symbol, shares, price, time, "Sell")

        return redirect("/")

    else:
        # GET
        return render_template("sell.html", symbols=symbols)

