from typing import List
from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        return next((p for p in self.products if p.name == product_name), None)

    def remove(self, product_name):
        p = self.find(product_name)
        if p:
            self.products.remove(p)

    def __repr__(self):
        return "\n".join([f'{p.name}: {p.quantity}' for p in self.products])