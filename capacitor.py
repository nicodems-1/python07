from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    CreatureFactory,
    HealCapability,
    TransformCapability,
)
from typing import cast


def battle_script() -> None:
    grass = HealingCreatureFactory()
    normal = TransformCreatureFactory()
    healing_creation(grass)
    print()
    transform_creation(normal)


def healing_creation(creaturefactory: CreatureFactory) -> None:
    print("Testing Creature with healing capacity")
    pokemon = creaturefactory.create_base()
    pokemon_evo = creaturefactory.create_evolved()
    print(" base:")
    print(pokemon.describe())
    print(pokemon.attack())
    print(cast(HealCapability, pokemon).heal)
    print(" evolved")
    print(pokemon_evo.describe())
    print(pokemon_evo.attack())
    print(cast(HealCapability, pokemon_evo).heal)


def transform_creation(creaturefactory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    pokemon = creaturefactory.create_base()
    pokemon_evo = creaturefactory.create_evolved()
    print(" base:")
    print(pokemon.describe())
    print(pokemon.attack())
    print(cast(TransformCapability, pokemon).transform())
    print(pokemon.attack())
    print(cast(TransformCapability, pokemon).revert())
    print(" evolved")
    print(pokemon_evo.describe())
    print(pokemon_evo.attack())
    print(cast(TransformCapability, pokemon_evo).transform())
    print(pokemon_evo.attack())
    print(cast(TransformCapability, pokemon_evo).transform())


if __name__ == "__main__":
    battle_script()
