from units.magic_unit import MagicUnit


class MagicGirl(MagicUnit):
    def __init__(self):
        super().__init__()
        self._damage = 25
        self._speed = 20
        self._weapon = None
        self._protection = 5
        self._price = 30

    def attack(self):
        #print('Attack on {}'.format(self.spell))
        self._energy -= 5
        return [self._damage, self._weapon]

    def treat(self):
        pass

    def shield(self):
        pass
