from ex2 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    FlameFactory,
    AquaFactory,
)
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def tournament_script() -> None:
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()
    grass_fac = HealingCreatureFactory()
    normal_fac = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    print("Tournament 0 (basic)")
    battle([(flame_fac, normal), (grass_fac, defensive)])
    print("Tournament 1 (error)")
    battle([(flame_fac, aggressive), (grass_fac, defensive)])
    print("Tournament 2 (multiple)")
    battle(
        [(aqua_fac, normal), (grass_fac, defensive), (normal_fac, aggressive)]
    )


def battle(opponents: list) -> None:
    creatures = []
    strategies = []
    status = []
    for opponent in opponents:
        factory, strategy = opponent
        creatures.append(factory.create_base())
        strategies.append(strategy)
    r = 0
    while r < len(creatures):
        status.append(f"({creatures[r].name}+{type(strategies[r]).__name__})")
        r += 1
    print(f"[{', '.join(status)}]")

    print("*** Tournament ***")
    print(f"{len(creatures)} opponents involved")
    u = 0
    try:
        while u < len(creatures) - 1:
            i = u + 1
            while i < len(creatures):
                print("\n* Battle *")
                print(creatures[u].describe())
                print("vs.")
                print(creatures[i].describe())
                print(" now fight!")
                strategies[u].act(creatures[u])
                strategies[i].act(creatures[i])
                print()
                i += 1
            u += 1
        print()
    except ValueError as e:
        print(f"{e}\n")


if __name__ == "__main__":
    tournament_script()
