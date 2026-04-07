from abc import ABC, abstractmethod
from .capability import HealCapability, TransformCapability


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


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self):
        return "Sproutling uses Vine Whip!"

    def heal(self):
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self):
        return "Bloomelle use Petal Dance!"

    def heal(self):
        return "Bloomelle heals itself for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")
        self.evo = 0

    def attack(self):
        if self.evo == 0:
            return "Shiftling attacks normally."
        return "Shiftling performs a boosted strike!"

    def transform(self):
        if self.evo == 0:
            self.evo = 1
            return "Shiftling shifts into a sharper form!"
        else:
            return "Shiftling stabilize its form"

    def revert(self):
        if self.evo == 1:
            self.evo = 0
            return "Shiftling return to normal."
        else:
            return "Shiftling stabilize its form"


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal")
        self.evo = 0

    def attack(self):
        if self.evo == 0:
            return "Morphagon attacks normally."
        return "Morphagon unleashes a devastating morph strike!"

    def transform(self):
        if self.evo == 0:
            self.evo = 1
            return "Morphagon shifts into a sharper form!"
        else:
            return "Morphagon stabilize its form"

    def revert(self):
        if self.evo == 1:
            self.evo = 0
            return "Morphagon return to normal."
        else:
            return "Morphagon stabilize its form"
