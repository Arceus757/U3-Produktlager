import csv
import locale

# Represent a product
class Product:
    def __init__(self, product_id, name, desc, price, quantity):
        self.id = product_id
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} \t {self.desc} \t {locale.currency(self.price, grouping=True)} \t Quantity: {self.quantity}"

# Manage the inventory
class Inventory:
    def __init__(self):
        self.products = []

    def load_data(self, filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(
                    product_id=int(row['id']),
                    name=row['name'],
                    desc=row['desc'],
                    price=float(row['price']),
                    quantity=int(row['quantity'])
                )
                self.products.append(product)

    def get_products(self):
        return "\n".join(str(product) for product in self.products)

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [product for product in self.products if product.id != product_id]

    def update_product_quantity(self, product_id, new_quantity):
        product = self.get_product_by_id(product_id)
        if product:
            product.quantity = new_quantity

# Main program
if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')

    inventory = Inventory()
    inventory.load_data('db_products.csv')
    
    print(inventory.get_products())
    
    # Getting a specific product
    product = inventory.get_product_by_id(2)
    if product:
        print("\nSpecific product:")
        print(product)

    # Testing updating quantity
    inventory.update_product_quantity(2, 10)
    print("\nAfter updating quantity:")
    print(inventory.get_product_by_id(2))

    # Adding a new product
    new_product = Product(11, "New Product", "A brand new product", 199.99, 50)
    inventory.add_product(new_product)
    print("\nAfter adding a new product:")
    print(inventory.get_products())

    # Removing a product
    inventory.remove_product(1)
    print("\nAfter removing a product:")
    print(inventory.get_products())
