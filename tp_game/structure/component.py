from abc import ABC, abstractmethod
from units.magic_unit import MagicUnit


class Component(MagicUnit):
    def __init__(self):
        super().__init__()

    @property
    def parent(self):
        return self._parent

    # @property.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def info_health(self):
        pass

    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def treat(self, points):
        pass

    @abstractmethod
    def attack(self):
        pass

    def shield(self):
        pass


class Leaf(Component):
    def __init__(self, unit):
        self._unit = unit

    def info_health(self):
        return self._unit._health

    def damage(self, loss):
        print('{} fight!'.format(self._unit.name))
        self._unit._health -= loss

    def treat(self, points):
        self._unit._health += points

    def attack(self):
        print(self._unit)
        print('{} attacked with {}!'.format(self._unit.name, self._unit._weapon))
        return self._unit._damage


class Composite(Component):
    def __init__(self, name):
        super().__init__()
        self._children: list[Component] = []
        self._name = name

    def add(self, component: Component):
        self._children.append(component)
        component.parent(self)

    def remove(self, component: Component):
        self._children.remove(component)
        component.parent = None

    def is_composite(self):
        return True

    def info_health(self):
        self._health = 0
        for child in self._children:
            self._health += child.info_health()
        self._health = self._health / len(self._children)
        return int(self._health)

    def damage(self, loss):
        for child in self._children:
            child.damage(loss)

    def treat(self, points):
        for child in self._children:
            child.treat(points)

    def attack(self):
        sum_attack = 0
        for child in self._children:
            sum_attack += child.attack()
        return sum_attack

    def die(self):
        for child in self._children:
            died_units = []
            if child.info_health() == 0:
                self.remove(child)
                died_units.append(child.name)

    def shield(self):
        pass
