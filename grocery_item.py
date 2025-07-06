class GroceryItem:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = int(price)

    def discounted_price(self):
        if self.category == "fruit":
            return f"discounted price: {self.price - (self.price * 0.1)}" 
        
        elif self.category == "vegetable":
            return f"discounted price { self.price-(self.price * 0.05)}"
        
        else:
            return "No discount otherwise"
        
price1 = GroceryItem("Bananas", "fruit", 100)

print(price1.discounted_price())