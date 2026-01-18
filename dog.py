class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.__age = age
        self.__breed = breed
        self.__stamina = 100

    def __str__(self):
        return "Je suis le chien " + self.name

    def getBreed(self):
        return self.__breed

    def getAge(self):
        return self.__age

    def grow_old(self, years=1):
        if years > 0:
            self.__stamina -= 5*years
            self.__age += years
    
    def isAlive(self):
        if self.__stamina > 0:
            return True
        else:
            return False

    def getStamina(self):
        return self.__stamina

    def rest(self):
        self.__stamina += 5

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

zephir.grow_old()
print("\tNouvel age: {} et stamina {}".format(zephir.getAge(), zephir.getStamina()))

zephir.grow_old(-1)
print("\tNouvel age: {} et stamina {}".format(zephir.getAge(), zephir.getStamina()))

zephir.grow_old(4)
print("\tNouvel age: {} et stamina {}".format(zephir.getAge(), zephir.getStamina()))
zephir.rest()
print("\tNouvel age: {} et stamina {}".format(zephir.getAge(), zephir.getStamina()))
