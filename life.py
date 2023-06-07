# Constants
X = 0
Y = 1
WIDTH = 5
HEIGHT = 5
ALIVE = 1
DEAD = 0
NEIGHBORS = (-1, 0, 1)
UNIVERSE = []
DEBUG_SEED = 135296


def print_universe(universe) -> None:
    """
    Prints out a representation of the universe state

    :param universe: List of values that make up the universe
    :return: None
    """
    for i in range(WIDTH * HEIGHT):
        if i % WIDTH == 0:
            print("\n", end="")
        print(universe[i], end="")


def initial_universe(seed: int):
    """
    Generates the initial universe state from the given seed
    :param seed: decimal value for binary universe layout
    :return: the generated universe grid
    """
    universe: list = []
    for i in range(WIDTH * HEIGHT):
        universe.append(seed % 2)
        seed = int(seed / 2)
    return universe


def check_neighbors():
    ...


def update_cells():
    ...


if __name__ == "__main__":
    universe = initial_universe(DEBUG_SEED)
    print_universe(universe)
