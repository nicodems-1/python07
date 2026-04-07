from ex0 import FlameFactory, AquaFactory, CreatureFactory


def battle_script() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    verify_creation(aqua)
    print()
    verify_creation(flame)
    print()
    creature_fight(aqua, flame)


def verify_creation(creaturefactory: CreatureFactory) -> None:
    print("Testing factory")
    pokemon = creaturefactory.create_base()
    pokemon_evo = creaturefactory.create_evolved()
    deck = [pokemon, pokemon_evo]
    for card in deck:
        print(card.describe())
        print(card.attack())


def creature_fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    fighter1 = factory1.create_base()
    fighter2 = factory2.create_base()
    print(f"{fighter1.describe()}\n vs\n{fighter2.describe()}")
    print("fight!")
    print(fighter1.attack())
    print(fighter2.attack())


if __name__ == "__main__":
    battle_script()
