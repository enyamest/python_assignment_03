import uuid

class Product:
    _id = ""
    name = ""
    description = ""
    quantity = 0
    price = 0.00
    discount = 0.00
    image_url = ""

    def __init__(self, name, quantity, price) -> None:
        self._id = uuid.uuid4()
        self.name = name
        self.quantity = quantity
        self.price = price

