from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, id, colour, base_bill):
        self._id = id
        self._colour = colour
        self._base_bill = base_bill

    @abstractmethod
    def beep(self):
        pass

    def engineOn(self):
        pass
