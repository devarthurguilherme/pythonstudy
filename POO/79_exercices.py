class ListManipulator:
    def __init__(self, userList):
        self.myList = userList
        self.userNumber = None

    # Check Number
    def checkNumber(self):
        while True:
            userInput = input("Digit a number: ")
            try:
                self.userNumber = int(userInput)
                return self.userNumber
            except ValueError:
                print("\nPlease, digit a integer valid number!\n")

    # Show  List
    def showList(self):
        if not self.myList:
            print("Empty list")
            return
        for index, value in enumerate(self.myList):
            print(f"list[{index}] = {value}")

    # Add Element
    def addListElement(self):
        print("Let's add a element\n")
        while True:
            self.userNumber = self.checkNumber()
            if self.userNumber not in self.myList:
                self.myList.append(self.userNumber)
                break
            else:
                print("\nDigit a number that doesn't exist in the list!\n")

    # Remove Element
    def removeElement(self):
        print("Let's remove a element\n")
        if not self.myList:
            print("Empty list")
            return
        while True:
            print("\nDigit a integer element to remove\n")
            self.userNumber = self.checkNumber()
            try:
                self.myList.remove(self.userNumber)
                break
            except ValueError:
                print(f"{self.userNumber} doesn't exist int the list!\n")
                print(f"Try another number!\n")

    # Seek bigger element
    def biggerElement(self):
        if not self.myList:
            print("Empty list")
            return
        result = max(self.myList)
        print(result)

    # Seek smaller element
    def smallerElement(self):
        if not self.myList:
            print("Empty list")
            return
        result = min(self.myList)
        print(result)

    # Average
    def listAverage(self):
        if not self.myList:
            print("Empty list")
            return
        result = sum(self.myList) / len(self.myList)
        print(result)


class ManipulatorMenu:
    def __init__(self, userList):
        self.myList = userList
        # Instance
        self.myListManipulator = ListManipulator(self.myList)

    def showMenu(self):
        menu = """
        ----- LIST MANIPULATOR -----\n
        1. Add Element
        2. Remove Element
        3. Bigger Element
        4. Smaller Element
        5. Average
        6. Show List
        7. Exit
        """
        print(menu)

    def menu(self):
        while True:
            self.showMenu()
            userChoice = self.myListManipulator.checkNumber()
            match userChoice:
                case 1:
                    self.myListManipulator.addListElement()
                case 2:
                    self.myListManipulator.removeElement()
                case 3:
                    self.myListManipulator.biggerElement()
                case 4:
                    self.myListManipulator.smallerElement()
                case 5:
                    self.myListManipulator.listAverage()
                case 6:
                    self.myListManipulator.showList()
                case 7:
                    print("\nExit\n")
                    break
                case _:
                    print("\nDigit a valid option!\n")


myList = []
myManipulator = ManipulatorMenu(myList)
myManipulator.menu()
