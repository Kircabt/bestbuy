
class Product:
    def __init__(self, name:str, price:float, quantity:int):
        if not name:
            raise ValueError("Name is empty, please set a name.")
        if price < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = input("Please set the quantity: ")
        if self.quantity == 0:
            self.active = False
    def is_active(self) -> bool:
        return self.active
    def activate(self):
        if self.active == True:
            print("The product is active")
        else:
            self.active = True
            print("The product is activated.")
    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity:{self.quantity}")
    def buy(self, quantity) -> float:
        if not self.active: # product deactivated
            raise ValueError(f"Cannot buy '{self.name}' because it is inactive.")
        if quantity <= 0: # invalid purchase
            raise ValueError("Purchase quantity must be greater than zero.")
            # Problem 3: Insufficient stock available
        if quantity > self.quantity:
            raise ValueError(f"Not enough stock. Available: {self.quantity}, Requested: {quantity}")
        self.quantity -= quantity # update remaining stock and calculate cost
        total_price = quantity * self.price

        return float(total_price)
