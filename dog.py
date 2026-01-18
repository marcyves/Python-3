class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return "Je suis le chien " + self.name

medor = Dog("Medor", 2 , "Labrador")

print(medor)