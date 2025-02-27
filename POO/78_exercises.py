class Event:
    def __init__(self, totalPlaces=10):
        self.totalPlaces = totalPlaces
        self.reservedPlaces = 0

    # Methods
    # Available Places
    def availablePlaces(self):
        print(f"Available places = {self.totalPlaces - self.reservedPlaces}")

    # Reserve
    def reserve(self):
        if self.reservedPlaces == self.totalPlaces:
            print("\nDoesn't exist available places!\n")
            return
        self.reservedPlaces += 1
        print(f"Reserves = {self.reservedPlaces}")
        print(f"Reserve was done!")
        self.availablePlaces()
        return

    # Cancel
    def cancel(self):
        if self.reservedPlaces == 0:
            print(f"\nReserves done so far = {self.reservedPlaces}\n")
            return

        self.reservedPlaces -= 1
        print(f"Reserve was canceled!")
        self.availablePlaces()
        return


startEvent = Event(20)
startEvent.availablePlaces()
print("*"*30)
startEvent.reserve()
print("*"*30)
startEvent.cancel()

for _ in range(21):
    startEvent.reserve()

for _ in range(21):
    startEvent.cancel()
