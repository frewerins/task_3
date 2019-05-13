from abc import abstractmethod
from units.magic_unit import MagicUnit


class MagicAnimal(MagicUnit):
    def __init__(self):
        super().__init__()
        self._speed = 10
        self._protection = 30
        self._price = 15

    @abstractmethod
    def treat(self):
        pass

    def attack(self):
        pass

    @abstractmethod
    def shield(self):
        pass
