from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod
    def go(self):
        print("What you doing")
    @abstractclassmethod
    def stop(self):
        print("This vehicle is stopped")
    

class Car(Vehicle):
    
    def go(self):
        print("You're driving the car")
    def stop(self):
        print("This car is stopped")

class Bike(Vehicle):
    
    def go():
        pass
    def stop(self):
        print("This bike is stopped")   
    def ride(self):
        print("You're riding the bike")


car = Car()
car.go()
car.stop()

bike = Bike()
bike.ride()
bike.stop()