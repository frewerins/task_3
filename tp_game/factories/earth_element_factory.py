from factories.element_factory import ElementFactory
from units.magic_girl import MagicGirl
from units.magic_boy import MagicBoy
from units.magic_animal import MagicAnimal


class EarthElementFactory(ElementFactory):
    def create_magic_girl(self):
        return EarthMagicGirl()

    def create_magic_boy(self):
        return EarthMagicBoy()

    def create_magic_animal(self):
        return EarthMagicAnimal()


class EarthMagicGirl(MagicGirl):
    _weapon = 'ssswamp!'


class EarthMagicBoy(MagicBoy):
    _weapon = 'wooden nunchuck'


class EarthMagicAnimal(MagicAnimal):

    def treat(self):
        EarthMagicBoy._health += 5
        EarthMagicGirl._health += 5
        EarthMagicAnimal._health += 5
        return 'Treatment Earth Army!'

    def shield(self):
        EarthMagicBoy._protection += 1
        EarthMagicGirl._protection += 1
        EarthMagicAnimal._protection += 1
        return 'Protect Earth Army!'
