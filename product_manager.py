from product import Product
from product_abstract import ProductAbstract
from typing import List


class ProductManager(ProductAbstract):

    products = {} # dictionary collection to hold products

    def create_product(self, product: Product):
        self.products[product._id] = product
        print(f"{product.name} has been created succesfully.")

    def edit_product(self, product: Product):
        self.products[product.get_id()] = product
        return product


    def get_product_by_id(self, id: str) -> str:
        return self.products[id]

    def get_all_products(self) -> List[Product]:
        return self.products.values()

    def upload_product_image(self, product_id: str, product_image: str):
        product: Product = self.products[product_id]
        product.set_image_url(product_image)
        print(self.products)
        print(f"Image upload succesful")

    def delete_product(self, id: str):
        product_name: Product = self.products[id].name ## get product name
        self.products.pop(id) #remove product
        print(f"{product_name} has been removed")


# Example usage of the product manager class
product_manager = ProductManager()

iphone_thirteen_pro = Product("Iphone 13 pro", 10,20000)
product_manager.create_product(iphone_thirteen_pro)

product_manager.edit_product(iphone_thirteen_pro)


product_manager.get_product_by_id(iphone_thirteen_pro._id)

print(product_manager.get_all_products())

product_manager.upload_product_image(iphone_thirteen_pro._id, "image")

product_manager.delete_product(iphone_thirteen_pro._id)
