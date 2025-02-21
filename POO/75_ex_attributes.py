class Fruit:
    def __init__(self, fruitName, fruitPriceKg, fruitStock):
        self.fruitName = fruitName
        self.fruitPriceKg = fruitPriceKg
        self.fruitStock = fruitStock

    def showInfo(self):
        print(f"""
            Fruit Name: {self.fruitName}
            Price (KG): ${self.fruitPriceKg:.2f}
            Quantity: {self.fruitStock}
            """)


fruit1 = Fruit("Apple", 1.8, 10)
fruit2 = Fruit("Orange", 3.5, 6)

fruit1.showInfo()
fruit2.showInfo()
