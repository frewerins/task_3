from factories.element_factory import ElementFactory
from units.magic_girl import MagicGirl
from units.magic_boy import MagicBoy
from units.magic_animal import MagicAnimal


class WaterElementFactory(ElementFactory):
    def create_magic_girl(self):
        return WaterMagicGirl()

    def create_magic_boy(self):
        return WaterMagicBoy()

    def create_magic_animal(self):
        return WaterMagicAnimal()


class WaterMagicGirl(MagicGirl):
    _weapon = 'flooood!'


class WaterMagicBoy(MagicBoy):
    _weapon = 'sharp knife'


class WaterMagicAnimal(MagicAnimal):

    def treat(self):
        WaterMagicBoy._health += 5
        WaterMagicGirl._health += 5
        WaterMagicAnimal._health += 5
        return 'Treatment Water Army!'

    def shield(self):
        WaterMagicBoy._protection += 1
        WaterMagicGirl._protection += 1
        WaterMagicAnimal._protection += 1
        return 'Protect Water Army!'
