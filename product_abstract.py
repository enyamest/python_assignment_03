from abc import ABC, abstractmethod
from typing import List
from product import Product


class ProductAbstract(ABC):

    @abstractmethod
    def create_product(product: Product):
        pass

    @abstractmethod
    def edit_product(product: Product):
        pass

    @abstractmethod
    def get_product_by_id(id: str) -> str:
        pass

    def get_all_products() -> List[Product]:
        pass

    @abstractmethod
    def upload_product_image(product_id: str):
        pass

    @abstractmethod
    def delete_product(id:str):
        pass