class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.__age = age
        self.__breed = breed

    def __str__(self):
        return "Je suis le chien " + self.name

    def getBreed(self):
        return self.__breed

    def getAge(self):
        return self.__age

print("\nCréation de Médor")
medor = Dog("Medor", 2 , "Labrador")

print(medor)

print("Nous avons créé le chien {} de race {} et agé de {} ans.".format(medor.name, medor.getBreed(), medor.getAge()))

print("\nCréation de Zéphir")
zephir = Dog("Zéphir", 1, "Cocker")

print("Nous avons créé le chien {} de race {} et agé de {} ans.".format(zephir.name, zephir.getBreed(), zephir.getAge()))

zephir.name = "Riféz"
# Comment interdire zephir.breed = "Epagneul" ?
print("Nous avons créé le chien {} de race {} et agé de {} ans.".format(zephir.name, zephir.getBreed(), zephir.getAge()))
