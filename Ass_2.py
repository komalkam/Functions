class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, special_skill):
        super().__init__(name, age, coat_color)
        self.special_skill = special_skill

    def special_skill_info(self):
        print(f"{self.name} has a special skill: {self.special_skill}")

    def description(self):  # Overriding the description method from the parent class
        print(f"Jack Russell Terrier: Name: {self.name}, Age: {self.age}")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def strength_info(self):
        print(f"{self.name} is a Bulldog with a strength level of {self.strength}")


if __name__ == "__main__":
    # Create objects of the Dog class
    dog1 = Dog("Buddy", 4, "Golden")
    dog2 = Dog("Max", 2, "Black")

    # Perform the operations on the Dog class objects
    dog1.description()  # Output: Name: Buddy, Age: 4
    dog1.get_info()     # Output: Coat Color: Golden

    dog2.description()  # Output: Name: Max, Age: 2
    dog2.get_info()     # Output: Coat Color: Black

    # Create objects of the JackRussellTerrier class
    jack_russell = JackRussellTerrier("Rocky", 3, "White and Brown", "Digging")

    # Perform the operations on the JackRussellTerrier class object
    jack_russell.description()       # Output: Jack Russell Terrier: Name: Rocky, Age: 3
    jack_russell.get_info()          # Output: Coat Color: White and Brown
    jack_russell.special_skill_info()  # Output: Rocky has a special skill: Digging

    # Create objects of the Bulldog class
    bulldog = Bulldog("Spike", 5, "Brown", "High")

    # Perform the operations on the Bulldog class object
    bulldog.description()     # Output: Name: Spike, Age: 5
    bulldog.get_info()        # Output: Coat Color: Brown
    bulldog.strength_info()   # Output: Spike is a Bulldog with a strength level of High
