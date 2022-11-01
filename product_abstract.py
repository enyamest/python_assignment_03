from abc import ABC, abstractmethod
from typing import List
from product import Product


class ProductAbstract(ABC):

    @abstractmethod
    def create_product(self, product: Product):
        pass

    @abstractmethod
    def edit_product(self, product: Product):
        pass

    @abstractmethod
    def get_product_by_id(self, id: str) -> str:
        pass

    def get_all_products(self) -> List[Product]:
        pass

    @abstractmethod
    def upload_product_image(self,product_id: str, product_image:str):
        pass

    @abstractmethod
    def delete_product(self, id:str):
        pass