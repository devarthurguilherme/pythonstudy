class Person:
    def __init__(self, name, age):
        self.name = name  # Public Attribute
        self._age = age  # Protected Attribute
        self.__balance = 0  # Private Attribute

    def showName(self):
        return self.name

    def showAge(self):
        return self._age

    def _inscreaseAge(self):
        self._age += 1

    def __inscreaseBalance(self, quantity):
        self.__balance += quantity

    def deposit(self, quantity=0):
        self.__inscreaseBalance(quantity)
        return self.__balance


me = Person("Arthur Guilherme", 32)
# Public Methods
print("\nPublic Methods\n")
print(me.showName())
print(me.showAge())
print("\n")
print(me.deposit(50))
print(me.deposit(50))
print(me.deposit(50))

# Protected Methods
print("\nProtected Methods\n")
me._inscreaseAge()  # This is not recommended!
print(me.showAge())

# Private Methods
print("\nPrivate Methods\n")
me._Person__inscreaseBalance(100)
print(me.deposit())

me._age = 40  # Don't do this##############
print(me.showAge())
