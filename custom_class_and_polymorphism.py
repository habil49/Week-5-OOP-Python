# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def show_identity(self):
        print(f"I am {self.name}, from {self.origin}, and my power is {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power} 💥")

# Inherited class (demonstrating polymorphism or encapsulation)
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadget):
        super().__init__(name, power, origin)
        self.gadget = gadget

    def use_power(self):
        print(f"{self.name} hacks systems using the {self.gadget} 🤖")

# Create objects
hero1 = Superhero("Stormbringer", "Lightning Control", "Sky Realm")
hero2 = TechHero("CyberKnight", "Tech Manipulation", "Neo City", "CyberGlove")

# Demonstrate behavior
hero1.show_identity()
hero1.use_power()

hero2.show_identity()
hero2.use_power()



# Base class
class Vehicle:
    def move(self):
        pass  # Abstract behavior

# Subclasses with their own move() implementation
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
