"""Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation."""

class car:
    wheels=4
    colour="black"
    material="carbon fiber"
    model="Audi"
    typecar="Wagon"

    def start(self):
        print("Car is starting")

    def accelerate(self):
        print("Car is speeding")

    def stop(self):
        print("Car has stopped")
    

    def __init__(self,model,material,typecar):
        self.model=model
        self.material=material
        self.typecar=typecar

class bmw(car):
    def colour(self):
        return "Blue"
        
class subaru(car):
    def colour(self):
        return "Red"


car1=car("Volvo","Steel","SUV")
print(car1.material)
print(car1.wheels)
car1.start()
car2=car("Toyota","Aluminium","Sedan")
print(car2.typecar)  
for i in [bmw("E30","steel","sedan") , subaru("GC8","Steel","Wagon")]:
    print(i.colour())

"""Activity 2: Polymorphism Challenge! 🎭
Create a program that includes animals or vehicles with the same action (like move()). 
However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️)."""  

class car:
    def move(self):
        print("Moving")

class plane:
    def move(self):
        print("Flying")

car1=car()
car1.move()
plane1=plane()
plane1.move()
    