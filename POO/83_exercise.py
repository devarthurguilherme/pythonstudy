class DigitalThermometer:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if -100 < value < 100:
            self._temperature = value
            return self._temperature
        else:
            print("\n*Temperature must be between -100 and 100 Celsius Degree!")


t = DigitalThermometer(32)
print(t.temperature)  # 32

t.temperature = 50
print(t.temperature)  # 50

t.temperature = -101
# *Temperature must be between -100 and 100 Celsius Degree! 50
print(t.temperature)
