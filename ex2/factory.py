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
    Creature
)


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature: ...
    @abstractmethod
    def create_evolved(self) -> Creature: ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()


class GrassFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class NormalFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
