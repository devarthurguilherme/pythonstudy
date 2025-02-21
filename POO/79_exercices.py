class ListManipulator:
    def __init__(self, userList):
        self.myList = userList
        self.userNumber = None

    # Check Number
    def checkNumber(self):
        while True:
            userInput = input("Digit a integer number: ")
            try:
                self.userNumber = int(userInput)
                return self.userNumber
            except ValueError:
                print("\nPlease, digit a valid number!\n")

    # Show  List
    def showList(self):
        if not self.myList:
            print("Empty list")
            return
        for index, value in enumerate(self.myList):
            print(f"list[{index}] = {value}")

    # Add Element
    def addListElement(self):
        self.userNumber = self.checkNumber()
        self.myList.append(self.userNumber)
        self.showList()

    # Remove Element
    def removeElement(self):
        self.userNumber = self.checkNumber()
        while True:
            try:
                self.myList.remove(self.userNumber)
                self.showList()
                break
            except ValueError:
                print(f"{self.userNumber} doesn't exist!\n")
                print(f"Try another number!\n")

    # Seek bigger element
    def biggerElement(self):
        return max(self.myList)

    # Seek smaller element
    def smallerElement(self):
        return min(self.myList)

    # Average
    def listAverage(self):
        if not self.myList:
            print("Empty list")
            return
        return sum(self.myList) / len(self.myList)


testList = []
myTest = ListManipulator(testList)
myTest.addListElement()
print(testList)
