from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name: str, id: str, taken: bool):
        self._name = name
        self._id = id
        self._taken = taken

    @abstractmethod
    def to_string(self):
        pass
