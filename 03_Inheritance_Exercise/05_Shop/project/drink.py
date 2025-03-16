from project.product import Product

class Drink(Product):
    # def __init__(self, name:str, quantity = 10):
    #     super().__init__(name, quantity)         // ANOTHER WAY TO DO IT
    def __init__(self, name):
        super().__init__(name, 10)




