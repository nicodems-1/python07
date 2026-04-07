from ex1 import GrassFactory, NormalFactory


def battle_script():
    grass = GrassFactory()
    normal = NormalFactory()
    healing_creation(grass)
    print()
    transform_creation(normal)


def healing_creation(creaturefactory) -> None:
    print("Testing Creature with healing capacity")
    pokemon = creaturefactory.create_base()
    pokemon_evo = creaturefactory.create_evolved()
    print(" base:")
    print(pokemon.describe())
    print(pokemon.attack())
    print(pokemon.heal())
    print(" evolved")
    print(pokemon_evo.describe())
    print(pokemon_evo.attack())
    print(pokemon_evo.heal())


def transform_creation(creaturefactory) -> None:
    print("Testing Creature with transform capability")
    pokemon = creaturefactory.create_base()
    pokemon_evo = creaturefactory.create_evolved()
    print(" base:")
    print(pokemon.describe())
    print(pokemon.attack())
    print(pokemon.transform())
    print(pokemon.attack())
    print(pokemon.revert())
    print(" evolved")
    print(pokemon_evo.describe())
    print(pokemon_evo.attack())
    print(pokemon_evo.transform())
    print(pokemon_evo.attack())
    print(pokemon_evo.transform())


if __name__ == "__main__":
    battle_script()
