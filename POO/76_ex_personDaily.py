class Person:
    def __init__(self, name):
        self.name = name
        # Person State
        self.awoken = False
        self.eating = False
        self.driving = False

    def wakeUp(self):
        if self.awoken:
            print(f"{self.name} is awaking!")
        else:
            self.awoken = True
            print(f"{self.name} awake!")

    def sleep(self):
        if self.awoken and not self.driving and not self.eating:
            self.awoken = False
            print(f"{self.name} sleep!")
        elif self.awoken == False:
            print(f"{self.name} is sleeping!")
        else:
            print(f"{self.name} can't sleep!")

    def eat(self):
        if not self.eating:
            if self.awoken == True and self.driving == False:
                print(f"{self.name} eat!")
                self.eating = True
            else:
                print(f"{self.name} can't eat, he is sleeping or driving now!")
        else:
            print(f"{self.name} is eating!")

    def stopEat(self):
        if self.eating:
            print(f"{self.name} stopped eating!")
            self.eating = False
        else:
            print(f"{self.name} was not eating now!")

    def drive(self):
        if not self.driving:
            if self.awoken and not self.eating:
                print(f"{self.name} drive")
                self.driving = True
            else:
                print(f"{self.name} can't drive, he is sleeping or eating now!")
        else:
            print(f"{self.name} is driving now!")

    def stopDrive(self):
        if self.driving:
            print(f"{self.name} stopping drive!")
            self.driving = False
        else:
            print(f"{self.name} is not driving now!")


arthur = Person("Arthur")

arthur.wakeUp()
arthur.wakeUp()
arthur.eat()
arthur.eat()
arthur.stopEat()
arthur.stopEat()
arthur.drive()
arthur.drive()
arthur.stopDrive()
arthur.stopDrive()
arthur.sleep()
arthur.sleep()
arthur.drive()
arthur.sleep()
arthur.wakeUp()
arthur.stopDrive()
arthur.stopEat()
arthur.sleep()
arthur.sleep()
arthur.drive()
arthur.eat()

# Arthur awake!
# Arthur is awaking!
# Arthur eat!
# Arthur is eating!
# Arthur stopped eating!
# Arthur was not eating now!
# Arthur drive
# Arthur is driving now!
# Arthur stopping drive!
# Arthur is not driving now!
# Arthur sleep!
# Arthur is sleeping!
# Arthur can't drive, he is sleeping or eating now!
# Arthur is sleeping!
# Arthur awake!
# Arthur is not driving now!
# Arthur was not eating now!
# Arthur sleep!
# Arthur is sleeping!
# Arthur can't drive, he is sleeping or eating now!
# Arthur can't eat, he is sleeping or driving now!
