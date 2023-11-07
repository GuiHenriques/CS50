class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is quacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is clucking")

class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print(f"The critter was caught")

duck = Duck()
chick = Chicken()
person = Person()

person.catch(chick)
