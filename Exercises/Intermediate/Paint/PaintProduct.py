from abc import ABC, abstractmethod


class PaintProduct(ABC):
    def __init__(self, name, litre, price, coverage):
        self.name = name
        self.litre = litre
        self.price = price
        self.coverage = coverage
