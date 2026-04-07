from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name, poketype):
        self.name = name
        self.poketype = poketype

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.poketype} type Creature"


class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self):
        return "Flameling use Ember!"


class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self):
        return "Pyrodon use Flamethrower!"


class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self):
        return "Aquabub use Water Gun!"


class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water")

    def attack(self):
        return "Torragon use Hydro Pump!"
