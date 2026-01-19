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
        if self.__stamina > 100:
            self.__stamina = 100

    def run(self, distance=10):
        if self.__stamina > 30:
            distance_max = (self.__stamina - 5) * 2
            if distance < distance_max:
                self.__stamina -= distance/2
                return True
            else:
                distance = distance_max
                self.__stamina = 5
                return distance
        else:
            return False

print("\nCréation de Médor")
medor = Dog("Medor", 2 , "Labrador")
print("Nous avons créé le chien {} de race {} et agé de {} ans.".format(medor.name, medor.getBreed(), medor.getAge()))

print("\nCréation de Zéphir")
zephir = Dog("Zéphir", 1, "Cocker")
print("Nous avons créé le chien {} de race {} et agé de {} ans.".format(zephir.name, zephir.getBreed(), zephir.getAge()))

distance = zephir.run()
if (distance):
    if(distance == True):
        print("-- Nouveau stamina {}.".format(zephir.getStamina()))
    else:
        print("-- Nouveau stamina {} après avoir courru {} mètres.".format(zephir.getStamina(), distance))
else:
    print("-- {} a refusé de courir".format(zephir.name))

distance = zephir.run(500)
if (distance):
    print("-- Nouveau stamina {} après avoir courru {} mètres.".format(zephir.getStamina(), distance))
else:
    print("-- {} a refusé de courir".format(zephir.name))

distance = zephir.run(500)
if (distance):
    print("-- Nouveau stamina {}".format(zephir.getStamina()))
else:
    print("-- {} a refusé de courir".format(zephir.name))
