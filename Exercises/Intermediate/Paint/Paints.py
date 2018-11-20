import PaintProduct


class CheapoMax(PaintProduct.PaintProduct):
    def __init__(self):
        super().__init__("Cheapo Max", 20, 19.99, 10)


class AverageJoes(PaintProduct.PaintProduct):
    def __init__(self):
        super().__init__("Average Joes", 15, 17.99, 11)


class DuluxourousPaints(PaintProduct.PaintProduct):
    def __init__(self):
        super().__init__("Duluxourous Paints", 10, 25, 20)

# cheap = CheapoMax()
# print(cheap.name)

# CHEAPO_MAX = {"litre": 20, "price": 19.99, "coverage": 10}
# AVERAGE_JOES = {"litre": 15, "price": 17.99, "coverage": 11}
# DULUXOUROUS_PAINTS = {"litre": 10, "price": 25, "coverage": 20}
