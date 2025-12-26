class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Для класса Product определите следующие свойства:
        название (name),
        описание (description ),
        цена (price),
        количество в наличии (quantity)."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
