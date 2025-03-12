class Pet:
    def __init__(self):
        self._name = ""
        self._age = 0
        self._weight = 0.0

    def showInfo(self):
        info = f"""
        \n--- Pet Info ---\n
        name: {self._name}
        age: {self._age}
        weight: {self._weight}kg
        """
        print(info)

    # Getters
    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getWeight(self):
        return self._weight

    # Setters
    def setName(self):
        while True:
            strValue = input("Pet Name: ")
            if strValue != "":  # Verifica se não é uma string vazia
                self._name = strValue
                break
            else:
                print("Please, to name you must use string value!")

    def setAge(self):
        while True:
            intValue = input("Pet Age: ")
            try:
                age = int(intValue)
                if age > 0:
                    self._age = intValue
                    break
                else:
                    print("Please, age > 0!")
            except ValueError:
                print("Please, to age you must use integer value!")

    def setWeight(self):
        while True:
            floatValue = input("Pet Weight: ")
            try:
                weight = float(floatValue)
                self._weight = weight
                break
            except ValueError:
                print("Please, to weight you must use integer value!")


class Menu:
    def __init__(self):
        self.myPet = Pet()

    def __showMenu(self):
        menu = """
        ___Menu___
        1. Set Name
        2. Set Age
        3. Set Weight
        4. Show Info
        5. Exit
        """
        print(menu)

    def __checkNumber(self):
        while True:
            userChoose = input("Choose one option:")
            try:
                userChoose = int(userChoose)
                return userChoose
            except ValueError:
                print("Digit a integer number!")

    def app(self):
        while True:
            self.__showMenu()
            userChoose = self.__checkNumber()
            match userChoose:
                case 1:
                    self.myPet.setName()
                case 2:
                    self.myPet.setAge()
                case 3:
                    self.myPet.setWeight()
                case 4:
                    self.myPet.showInfo()
                case 5:
                    print("... Exit of the Application, bye!")
                    break


# myDog = Pet()
# myDog.setName("Simba")
# myDog.setAge(8.1)
# myDog.setWeight(4.8)
# myDog.showInfo()

myMenu = Menu()

if myMenu:
    myMenu.app()
