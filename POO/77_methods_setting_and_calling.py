class Termostato:
    # Start Class
    def __init__(self, currentTemperature=20):
        self.currentTemperature = currentTemperature

    # Start of the Methods
    def increaseTemperature(self, value):
        self.currentTemperature += value
        print(
            f"Temperature increased at {value}º, new temperature is {self.currentTemperature}º.")

    def decreaseTemperature(self, value):
        self.currentTemperature -= value
        print(
            f"Temperature decreased at {value}º, new temperature is {self.currentTemperature}º.")

    def configTemperature(self, newTemperature):
        oldTemperature = self.currentTemperature
        self.currentTemperature = newTemperature
        print(
            f"The temperature was setted from {oldTemperature}º to {newTemperature}º")

    def showTemperature(self):
        print(f"Current temperature is {self.currentTemperature}º!")
    # End of the Methods


myTermostato = Termostato()
myTermostato.increaseTemperature(15)
myTermostato.decreaseTemperature(8)
myTermostato.configTemperature(20)
myTermostato.showTemperature()
myTermostato.increaseTemperature(22)
myTermostato.configTemperature(2)
myTermostato.showTemperature()
