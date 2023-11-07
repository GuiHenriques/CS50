questions = {"When the first-ever soccer World Cup happend? ": "C",
             "Which country won the first-ever soccer World Cup? ": "C",
             "Which country has won the world cup five times? ": "B",
             }

options = [["A. 1926", "B. 1928", "C. 1930", "D. 1934"],
           ["A. England", "B. Italy", "C. Uruguay", "D. Brazil"],
           ["A. Argentina", "B. Brazil", "C. Germany", "D. France"],]

for key, question in enumerate(questions):
    score = 0
    print(question)
    for option in options[key]:
        print(option)
    answer = input("Answer: ").upper()
    
    if answer != questions[question]:
        score += 1
print(f"Score: {score}")
