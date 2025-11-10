class Product:

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def apply_discount(self, discount):
        discount_amount = self.price * discount / 100
        self.price -= discount_amount
        return self.price

    def get_category_initial(self):
        return self.category[0]
    
    def __repr__(self):
        return f'name: {self.name}, category: {self.category}, price: {self.price}'
    
class PremiumProduct(Product):

    def __init__(self, name, category, price):
        super().__init__(name, category, price)

    def apply_discount(self, discount):
        return super().apply_discount(discount - 5)
    
