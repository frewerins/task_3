from factories.element_factory import ElementFactory
from units.magic_girl import MagicGirl
from units.magic_boy import MagicBoy
from units.magic_animal import MagicAnimal


class FireElementFactory(ElementFactory):
    def create_magic_girl(self):
        return FireMagicGirl()

    def create_magic_boy(self):
        return FireMagicBoy()

    def create_magic_animal(self):
        return FireMagicAnimal()


class FireMagicGirl(MagicGirl):
    _weapon = 'fffire!'


class FireMagicBoy(MagicBoy):
    _weapon = 'torch'


class FireMagicAnimal(MagicAnimal):

    def treat(self):
        FireMagicBoy._health += 5
        FireMagicGirl._health += 5
        FireMagicAnimal._health += 5
        return "Treatment Fire Army!"

    def shield(self):
        FireMagicBoy._protection += 1
        FireMagicGirl._protection += 1
        FireMagicAnimal._protection += 1
        return 'Protect Fire Army!'
