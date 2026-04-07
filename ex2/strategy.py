from abc import ABC, abstractmethod
from .capability import HealCapability, TransformCapability
from .creature import Creature
from typing import cast


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        return True

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise ValueError(
                f"Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                f"for this normal strategy"
            )


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(cast(TransformCapability, creature).transform())
            print(creature.attack())
            print(cast(TransformCapability, creature).revert())
        else:
            raise ValueError(
                f"Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(cast(HealCapability, creature).heal())
        else:
            raise ValueError(
                f"Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )
