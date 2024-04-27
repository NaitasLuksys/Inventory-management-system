from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, quantity):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity = quantity

    @abstractmethod
    def get_product_info(self):
        pass

    @abstractmethod
    def apply_discount(self, discount):
        pass

    @staticmethod
    def read_from_file(filename, product_class):
        try:
            products = []
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split(', ')
                    if len(parts) >= 4 + len(product_class.additional_properties):
                        product_id, name = parts[:2]
                        additional_properties = parts[2:len(parts)-2]
                        price_and_quantity = parts[-3:]
                        price_index = len(parts) - 3 - len(product_class.additional_properties)
                        price_value = float(price_and_quantity[price_index].replace('€', ''))
                        quantity = int(price_and_quantity[-1])
                        product = product_class(product_id, name, price_value, quantity, *additional_properties)
                        products.append(product)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []
        except Exception as e:
            print(f"Error reading from file '{filename}': {e}")
            return []
        return products
    
    @staticmethod
    def write_products_to_file(filename, products):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for product in products:
                    product_info = product.get_product_info()
                    file.write(", ".join(map(str, product_info)) + "\n")
                    file.write("\n")
        except Exception as e:
            print(f"Error writing to file '{filename}': {e}")

class Laptops(Product):
    additional_properties = []

    def get_product_info(self):
        base_info = [self._product_id, self._name, f"{self._price} €", self._quantity]
        return base_info

    def apply_discount(self, discount):
        self._discounted_price = self._price - (self._price * discount)
    
class Smartphones(Product):
    additional_properties = ['gb', 'model', 'color']

    def __init__(self, product_id, name, price, quantity, gb=None, model=None, color=None):
        super().__init__(product_id, name, price, quantity)
        self._gb = gb
        self._model = model
        self._color = color
        self._discounted_price = None
    def get_product_info(self):
        base_info = [self._product_id, self._name, self._gb, self._model, self._color, f"{self._price} €", self._quantity]
        return base_info
    
    def apply_discount(self, discount):
        self._discounted_price = self._price - (self._price * discount)

class Inventory:
    _instance = None

    def __init__(self):
        if not Inventory._instance:
            Inventory._instance = self
            self._products = []
            self._discounted_products = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def add_product(self, product):
        self._products.append(product)

    def write_products_to_file(self, filename, products):
        Product.write_products_to_file(filename, products)
    
    def apply_discount_to_selected_products(self, product):
        product._price = product._discounted_price
        self._discounted_products.append(product)

class ProductFactory:
    _instance = None

    def __init__(self):
        if not ProductFactory._instance:
            ProductFactory._instance = self
            self._products = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def create_product(self, product_type, *args, **kwargs):
        if product_type == "smartphone":
            product = Smartphones(*args, **kwargs)
        elif product_type == "laptop":
            product = Laptops(*args, **kwargs)
        else:
            raise ValueError("Invalid product type")
        return product

    def add_product(self, product):
        self._products.append(product)

    def write_products_to_file(self, filename, products):
        Product.write_products_to_file(filename, products)

def add_product_from_file(factory, filename, product_type):
    products = Product.read_from_file(filename, Smartphones if product_type == 'smartphone' else Laptops)
    for product in products:
        if not any(existing_product._product_id == product._product_id for existing_product in factory._products):
            factory.add_product(product)

def add_new_product(factory, product_type):
    while True:
        product_id = input("Enter product ID: ")
        if any(product._product_id == product_id for product in factory._products):
            print("Product with this ID already exists. Please enter a different ID.")
        else:
            break
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = input("Enter product quantity: ")
    additional_properties = []
    if product_type == 'smartphone':
        gb = input("Enter GB: ")
        model = input("Enter model: ")
        color = input("Enter color: ")
        additional_properties.extend([gb, model, color])
    product = factory.create_product(product_type, product_id, name, price, quantity, *additional_properties)
    factory.add_product(product)

inventory = Inventory.get_instance()
factory = ProductFactory.get_instance()

add_product_from_file(factory, "Smartphones.txt", "smartphone")
add_product_from_file(factory, "Laptops.txt", "laptop")

while True:
    print("Which operation do you want to perform?")
    print("1. Add a new product")
    print("2. Apply discount to existing products")
    print("3. Exit")
    operation_choice = input("Enter operation number: ")
    if operation_choice == '1':
        while True:
            product_type = input("Enter product type (smartphone/laptop) or 'exit' to quit: ")
            if product_type == 'exit':
                break
            elif product_type not in ['smartphone', 'laptop']:
                print("Invalid product type. Please enter 'smartphone' or 'laptop'.")
                continue
            add_new_product(factory, product_type)

        inventory.write_products_to_file("AllProducts.txt", factory._products)
        smartphones = [product for product in factory._products if isinstance(product, Smartphones)]
        inventory.write_products_to_file("Smartphones.txt", smartphones)
        laptops = [product for product in factory._products if isinstance(product, Laptops)]
        inventory.write_products_to_file("Laptops.txt", laptops)

    elif operation_choice == '2':
        while True:
            product_id = input("Enter the product ID to apply discount or 'exit' to quit: ")
            if product_id == 'exit':
                break
            else:
                discount = float(input("Enter discount (in decimal, e.g., 0.1 for 10%): "))
            selected_product = None
            for product in factory._products:
                if product._product_id == product_id:
                    selected_product = product
                    break
            if selected_product is not None:
                selected_product.apply_discount(discount)
                print("Discount applied successfully!")
                inventory.apply_discount_to_selected_products(selected_product)
            else:
                print("Product not found!")

    elif operation_choice == '3':
        if inventory._discounted_products:
            print("Discounted Products:")
            for product in inventory._discounted_products:
                if isinstance(product, Smartphones):
                    print(f"Product ID: {product._product_id}, Name: {product._name}, GB: {product._gb}, Model: {product._model}, Color: {product._color}, Discount: {discount*100} %, Discounted Price: {product._discounted_price} €, Quantity: {product._quantity}\n")
                elif isinstance(product, Laptops):
                    print(f"Product ID: {product._product_id}, Name: {product._name}, Discount: {discount*100} %, Discounted Price: {product._discounted_price}, Quantity: {product._quantity}\n")
        print("Exiting the program.")
        break