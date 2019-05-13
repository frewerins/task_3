from units.magic_unit import MagicUnit


class MagicBoy(MagicUnit):
    def __init__(self):
        super().__init__()
        self._damage = 15
        self._speed = 15
        self._weapon = None
        self._protection = 20
        self._price = 30

    def attack(self):
        # print('Attack on {}'.format(self.weapon))
        self._energy -= 3
        return [self._damage, self._weapon]

    def treat(self):
        pass

    def shield(self):
        pass
