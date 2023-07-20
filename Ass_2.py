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

    def description(self):  
        print(f"Jack Russell Terrier: Name: {self.name}, Age: {self.age}")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def strength_info(self):
        print(f"{self.name} is a Bulldog with a strength level of {self.strength}")


if __name__ == "__main__":
   
    dog1 = Dog("Buddy", 4, "Golden")
    dog2 = Dog("Max", 2, "Black")

    dog1.description()  
    dog1.get_info()     

    dog2.description()  
    dog2.get_info()     

  
    jack_russell = JackRussellTerrier("Rocky", 3, "White and Brown", "Digging")

   
    jack_russell.description()       
    jack_russell.get_info()         
    jack_russell.special_skill_info() 

   
    bulldog = Bulldog("Spike", 5, "Brown", "High")

    bulldog.description()     
    bulldog.get_info()        
    bulldog.strength_info()   
