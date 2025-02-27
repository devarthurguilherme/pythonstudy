class Product:
    def __init__(self, productName, price):
        self.name = productName
        self._price = None
        self.setPrice(price)

    # Getters
    def getPrice(self):
        return self._price

    # Setters
    def setPrice(self, valuePrice):
        # Business Rule
        if valuePrice >= 0:
            self._price = valuePrice
        else:
            print("\nPrice must be bigger or equal to zero!\n")

    def discountApply(self, discountPercentage):
        newPrice = self._price * (1 - discountPercentage / 100)
        self.setPrice(newPrice)


product1 = Product("Tshirt", 50)
print(f"Product {product1.name}\nCurrent Price: ${product1.getPrice()}")

product1.setPrice(-15)
print(f"Product {product1.name}\nNew Price: ${product1.getPrice()}")

product1.discountApply(30)
print(f"Product {product1.name}\nNew Price: ${product1.getPrice()}")
