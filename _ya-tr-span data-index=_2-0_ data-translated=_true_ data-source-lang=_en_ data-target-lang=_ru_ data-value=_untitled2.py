class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.inventory = 0
        
    def add_inventory(self, quantity):
        self.inventory += quantity
        
    def remove_inventory(self, quantity):
        if self.inventory < quantity:
            return False
        self.inventory -= quantity
        return True
        
class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.products = []
        self.total_price = 0
        
    def add_product(self, product, quantity):
        if product.remove_inventory(quantity):
            self.products.append((product, quantity))
            self.total_price += product.price * quantity
            return True
        return False
        
class Store:
    def __init__(self):
        self.products = []
        self.orders = []
        
    def add_product(self, name, price, inventory=0):
        product = Product(name, price)
        product.add_inventory(inventory)
        self.products.append(product)
        
    def add_order(self, customer_name):
        self.orders.append(Order(customer_name))
        
    def get_products(self):
        return self.products
        
    def get_orders(self):
        return self.orders
        
    def get_order_by_customer(self, customer_name):
        for order in self.orders:
            if order.customer_name == customer_name:
                return order
        return None
