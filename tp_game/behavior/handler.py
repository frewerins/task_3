from abc import ABC, abstractmethod
from factories.air_element_factory import AirElementFactory
from factories.water_element_factory import WaterElementFactory
from factories.fire_element_factory import FireElementFactory
from factories.earth_element_factory import EarthElementFactory
from structure.component import Composite, Leaf


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request, factory=None):
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None
    _factory = None

    def set_next(self, handler: Handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request, factory=None):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class CreateElementHandler(AbstractHandler):
    elements = {'air': AirElementFactory(),
                'earth': EarthElementFactory(),
                'fire': FireElementFactory(),
                'water': WaterElementFactory()
                }

    def handle(self, request):
        if request == 'Q':
            print("Good bye, good luck!")
            return None
        else:
            try:
                return self.elements[request.lower()]
            except KeyError:
                print('Please, write element correctly')
                request = input()
                self.handle(request)


class CreateUnitsHandler(AbstractHandler):
    """units = {
         'girl': factory.create_magic_girl,
         'boy': factory.create_magic_boy,
         'animal': factory.create_magic_animal,
         'creating_unit': factory.can_create_magic_unit,
         'price_girl': MagicGirl.price,
         'price_boy': MagicBoy.price,
         'price_animal': MagicAnimal.price,
         'message': factory.return_message
     }"""
    units = {}

    def __init__(self, factory):
        self.factory = factory

    def handle(self, request):
        if request == 'Q':
            print("Finish")
            return CreateElementHandler()
        else:
            check = self.factory.can_create_magic_unit(request)
            if check is None:
                print('Please write name of unit correctly!')
                request = input()
                self.handle(request)
            elif check:
                new_unit = None
                if request == 'girl':
                    new_unit = self.factory.create_magic_girl()
                elif request == 'boy':
                    new_unit = self.factory.create_magic_boy()
                if request == 'animal':
                    new_unit = self.factory.create_magic_animal()
                if new_unit:
                    print('Write a name of new unit')  # добавляю юнита в базу
                    name = input()
                    self.units[name] = new_unit
                    new_unit.name = name
                    print(self.factory.return_message())
                    print("Choose a magic unit: girl(30 coins), boy(30 coins) or animal(15 coins)")
                    request = input()
                    self.handle(request)
                else:
                    print('Please write name of unit correctly!')
                    request = input()
                    self.handle(request)
            else:
                print("Sorry, you don't have enough money, let's create an army!")
            return self.units


class CreateArmyHandler(AbstractHandler):
    def __init__(self, units):
        self._army = Composite('main')
        self.units = units

    def handle(self, request):
        if request.lower() == 'yes':
            print("Please, write name of your squad")
            request = input()
            new_squad = super().handle(request)
            self._army.add(new_squad)
        elif request.lower() == 'no':
            also_units = super().handle('also')
            for unit in also_units:
                self._army.add(unit)
            return self._army
        else:
            print("Please write 'yes' or 'no'")
            request = input()
            self.handle(request.lower())


class CreateSquadHandler(AbstractHandler):
    def __init__(self, units):
        self._units = units

    def handle(self, request):
        if request == 'also':
            also = []
            for unit in self._units.keys():
                also.append(Leaf(self._units[unit]))
            return also
        else:
            self._squad = Composite(request)
            self.name = request
            print("Please, write units that will be in {} squad".format(self.name))
            request = input()
            units = request.split(' ')
            print(units)
            print(self._units)
            for unit in units:
                try:
                    new_unit = Leaf(self._units[unit])
                except KeyError:
                    print("{} isn't found")
                self._units.pop(unit)
                self._squad.add(new_unit)
            print("Do you want to add somebody else?")
            request = input()
            if request.lower() == 'yes':
                self.handle(request)
            else:
                return self._squad

