from abc import ABC, abstractmethod
from factories.element_factory import ElementFactory

"""Передаем в инвокер команду, если она сложная, ее выполняет 
ресиевер. Сложная - это если имеет несколько возможных реализаций."""


class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass


class SimpleCommand(Command):
    def __init__(self):
        self._a = '0'

    def execute(self):
        print("ssss")


class ComplexCommand(Command):
    def __init__(self, reciever):
        self._reciever = reciever

    def execute(self, *args):
        return self._reciever.do(*args)


class AttackReceiver(ABC):
    def do(self, component_victim, component_rapist):
        loss = component_rapist.attack()
        component_victim.damage(loss)
        return [component_victim, component_rapist]


class TreatReceiver(ABC):
    def do(self, component_1, component_2):
        component_1.treat(5)
        return [component_1, component_2]


class HealthReceiver(ABC):
    def do(self, component_1, component_2):
        component_1.info_health()
        component_1.die()
        return [component_1, component_2]


class Invoker(ABC):
    command = {}

    def set_command(self, command, name):
        self.command[name] = command

    def do(self, name_of_command, *args):
        return self.command[name_of_command].execute(*args)
            #print('Please write a command correctly')

