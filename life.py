# Constants
X = 0
Y = 1
WIDTH = 5
HEIGHT = 5
UNIVERSE_SIZE = WIDTH * HEIGHT
ALIVE = 1
DEAD = 0
NEIGHBORS = (-1, 0, 1)
UNIVERSE = []
DEBUG_SEED = 135296


class Universe:
    def __init__(self, seed, width, height):
        self.width = width
        self.height = height
        self.size = self.height * self.width
        self.universe = []

        for i in range(self.size):
            self.universe.append(seed % 2)
            seed = int(seed / 2)

    def __str__(self):
        """
        Formats the universe list to a grid for printing
        :return: String universe list
        """
        output = ""
        for i in range(self.size):
            if i % self.width == 0:
                output += "\n"

            output += f'{self.universe[i]} '

        return output


def initial_universe(seed: int):
    """
    Generates the initial universe state from the given seed
    :param seed: decimal value for binary universe layout
    :return: the generated universe grid
    """
    universe: list = []
    for i in range(UNIVERSE_SIZE):
        universe.append(seed % 2)
        seed = int(seed / 2)
    return universe


def determine_universe_state() -> list:
    to_be_updated = []
    for i in range(UNIVERSE_SIZE):
        if check_neighbors():
            to_be_updated.append(i)
    return to_be_updated


def check_neighbors() -> bool:
    ...


def update_cells():
    ...


if __name__ == "__main__":
    universe = Universe(DEBUG_SEED, 5, 5)
    print(universe)
