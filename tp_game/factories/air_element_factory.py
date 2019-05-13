from factories.element_factory import ElementFactory
from units.magic_girl import MagicGirl
from units.magic_boy import MagicBoy
from units.magic_animal import MagicAnimal


class AirElementFactory(ElementFactory):
    def create_magic_girl(self):
        return AirMagicGirl()

    def create_magic_boy(self):
        return AirMagicBoy()

    def create_magic_animal(self):
        return AirMagicAnimal()


class AirMagicGirl(MagicGirl):
    _weapon = 'huuuuricane!'


class AirMagicBoy(MagicBoy):
    _weapon = 'air sword'


class AirMagicAnimal(MagicAnimal):

    def treat(self):
        AirMagicBoy._health += 5
        AirMagicGirl._health += 5
        AirMagicAnimal._health += 5
        return 'Treatment Air Army!'

    def shield(self):
        AirMagicBoy._protection += 1
        AirMagicGirl._protection += 1
        AirMagicAnimal._protection += 1
        return 'Protect Air Army!'
