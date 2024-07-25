class product_inventory_system:
    def __init__(self):
        self.products={
            'books':4,
            'pen':1,
            'stapler':2,
            'cello tape':7
        }
    def display_available_products(self):
        for product,count in self.products.items():
            print(f'{product}:{count}')
            
    def add_products(self,product,count):
        if product in self.products and self.products[product]>0:
            self.products[product]+=count
        else:
            self.products[product]=count
        return self.products

prod=product_inventory_system()
prod.display_available_products()

prod.add_products('medicine',30)
prod.display_available_products()

prod.add_products('files',1000)
prod.display_available_products()

prod.add_products('cello tape',2)
prod.display_available_products()
