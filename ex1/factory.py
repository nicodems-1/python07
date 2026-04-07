from abc import ABC, abstractmethod
from .creature import (
    Flameling,
    Pyrodon,
    Aquabub,
    Torragon,
    Sproutling,
    Bloomelle,
    Shiftling,
    Morphagon,
)


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self): ...
    @abstractmethod
    def create_evolved(self): ...


class FlameFactory(CreatureFactory):
    def create_base(self):
        return Flameling()

    def create_evolved(self):
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self):
        return Aquabub()

    def create_evolved(self):
        return Torragon()


class GrassFactory(CreatureFactory):
    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()


class NormalFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()
