import unittest
from NaitasLuksys_kursinis import Smartphones, Laptops, Inventory, ProductFactory, add_product_from_file, add_new_product

class TestProductMethods(unittest.TestCase):
    def setUp(self):
        self.factory = ProductFactory.get_instance()
        add_product_from_file(self.factory, "Smartphones.txt", "smartphone")
        add_product_from_file(self.factory, "Laptops.txt", "laptop")
        self.assertEqual(len(self.factory._products), 12)
    
    def test_product_creation(self):
        self.assertIsInstance(self.factory._products[0], Smartphones)
        self.assertIsInstance(self.factory._products[-1], Laptops)
    
    def test_discount_application(self):
        product = self.factory._products[0]
        product.apply_discount(0.1)
        self.assertAlmostEqual(product._discounted_price, 450.0)
    
    def test_inventory_singleton(self):
        inventory1 = Inventory.get_instance()
        inventory2 = Inventory.get_instance()
        self.assertIs(inventory1, inventory2)
    
    def test_add_product_from_file(self):
        # Debugging
        print("Products after adding from files:")
        for product in self.factory._products:
            print(product._product_id, product._name)
        self.assertEqual(len(self.factory._products), 12)
        
    def test_get_product_info_smartphones(self):
        product = Smartphones("ID12345", "iPhone", 1000.0, 10, "64GB", "12", "White")
        expected_info = ["ID12345", "iPhone", "64GB", "12", "White", "1000.0 €", 10]
        self.assertEqual(product.get_product_info(), expected_info)
    
    def test_get_product_info_laptops(self):
        product = Laptops("ID54321", "Lenovo", 800.0, 5)
        expected_info = ["ID54321", "Lenovo", "800.0 €", 5]
        self.assertEqual(product.get_product_info(), expected_info)
    
    def test_apply_discount_smartphones(self):
        product = Smartphones("ID12345", "iPhone", 1000.0, 10, "64GB", "12", "White")
        product.apply_discount(0.2)
        self.assertAlmostEqual(product._discounted_price, 800.0)
    
    def test_apply_discount_laptops(self):
        product = Laptops("ID54321", "Lenovo", 800.0, 5)
        product.apply_discount(0.15)
        self.assertAlmostEqual(product._discounted_price, 680.0)
    
    def test_create_smartphone_product(self):
        product = ProductFactory.get_instance().create_product("smartphone", "ID54321", "Samsung", 900.0, 8, "128GB", "S20", "Black")
        self.assertIsInstance(product, Smartphones)
        self.assertEqual(product._product_id, "ID54321")
        self.assertEqual(product._name, "Samsung")
        self.assertEqual(product._price, 900.0)
        self.assertEqual(product._quantity, 8)
        self.assertEqual(product._gb, "128GB")
        self.assertEqual(product._model, "S20")
        self.assertEqual(product._color, "Black")
    
    def test_create_laptop_product(self):
        product = ProductFactory.get_instance().create_product("laptop", "ID98765", "HP", 1200.0, 12)
        self.assertIsInstance(product, Laptops)
        self.assertEqual(product._product_id, "ID98765")
        self.assertEqual(product._name, "HP")
        self.assertEqual(product._price, 1200.0)
        self.assertEqual(product._quantity, 12)
    
    def test_add_product_to_inventory(self):
        product = Smartphones("ID12345", "iPhone", 1000.0, 10, "64GB", "12", "White")
        inventory = Inventory.get_instance()
        inventory.add_product(product)
        self.assertIn(product, inventory._products)
    
    def test_write_products_to_file(self):
        products = [Smartphones("ID12345", "iPhone", 1000.0, 10, "64GB", "12", "White")]
        Inventory.get_instance().write_products_to_file("test_products.txt", products)
    
    def test_read_from_file_smartphones(self):
        products = Smartphones.read_from_file("Smartphones.txt", Smartphones)
        self.assertIsInstance(products[0], Smartphones)
        self.assertEqual(len(products), 8)

    def test_read_from_file_laptops(self):
        products = Laptops.read_from_file("Laptops.txt", Laptops)
        self.assertIsInstance(products[0], Laptops)

    def test_apply_discount_to_selected_products(self):
        inventory = Inventory.get_instance()
        product = Smartphones("ID12345", "iPhone", 1000.0, 10, "64GB", "12", "White")
        inventory.add_product(product)
        inventory.apply_discount_to_selected_products(product)
        self.assertAlmostEqual(product._price, product._discounted_price)
        
    def test_create_product_smartphone(self):
        product = ProductFactory.get_instance().create_product("smartphone", "ID54321", "Samsung", 900.0, 8, "128GB", "S20", "Black")
        self.assertIsInstance(product, Smartphones)

    def test_create_product_laptop(self):
        product = ProductFactory.get_instance().create_product("laptop", "ID98765", "HP", 1200.0, 12)
        self.assertIsInstance(product, Laptops)

    def test_add_new_product_duplicate_id(self):
        # Test handling duplicate product IDs in add_new_product function
        factory = ProductFactory.get_instance()
        # Add a product with ID that already exists
        with self.assertRaises(ValueError):
            add_new_product(factory, "smartphone")

if __name__ == '__main__':
    unittest.main()
