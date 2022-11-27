import csv


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # Insert
        with open("data.csv", "a") as data:
            writer = csv.DictWriter(data, ["name", "age"])
            writer.writerow({"name": name, "age": age})

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not age:
            raise ValueError("Missing age")
        elif not age.isdigit():
            raise ValueError("Age is not integer")
        elif int(age) < 0:
            raise ValueError("Negative age")
        self._age = age

    @classmethod
    def new(cls):
        name = input("Name: ")
        age = input("Age: ")

        return cls(name, age)

def menu():
    print(f"{' MENU ':-^20}")
    
    # Options
    options = ["See", "Register", "Unregister", "Quit"]
    
    for k, i in enumerate(options):
        print(k+1,"-", i)
    
    while True:
        action = int(input("Action: "))
        if action > 0 and action < 5:
            return action

def see():
    with open("data.csv", "r") as data:
        reader = csv.DictReader(data)
        print(f'{"Name":<10}{"Age":>5}')
        print("-" * 15)
        for row in reader:
            print(f'{row["name"]:<10}{row["age"]:>5}')

def unregister():
    unregistered = input("Name: ")
    print(f"{unregistered} was unregitered")
    unregistered += ","
    with open("data.csv", "r") as f:
        lines = f.readlines()
    with open("data.csv", "w") as f:
        for line in lines:
            if line.strip("\n").startswith(unregistered):
                pass
            else:
                f.write(line)

def main():
    while True:
        option = menu()
        
        if option == 1:
            see()
        elif option == 2:
            Person.new()
        elif option == 3:
            unregister()
        elif option == 4:
            print("Program Finished")
            break
        

if __name__ == "__main__":
    main()
