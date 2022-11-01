import uuid

class Product:
    _id: str = ""
    name = ""
    description = ""
    quantity = 0
    price = 0.00
    discount = 0.00
    image_url = ""

    def __init__(self, name, quantity, price) -> None:
        self._id = str(uuid.uuid4())
        self.name = name
        self.quantity = quantity
        self.price = price

    def get_id(self) -> str:
        return self._id

    def set_image_url(self, image_url: str):
        self.image_url = image_url

