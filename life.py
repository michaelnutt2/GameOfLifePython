import os
import random
import time

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
DEBUG_SEED = 392949192399124912499591827432879238798273947502983097286376587293843453


class Universe:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = self.height * self.width
        self.universe = []
        self.update = []

        for i in range(self.size):
            self.universe.append(random.randrange(2))

    def __str__(self):
        """
        Formats the universe list to a grid for printing
        :return: String universe list
        """
        output = ""
        for i in range(self.size):
            if i % self.width == 0:
                output += "\n"

            if self.universe[i] == ALIVE:
                output += '# '
            else:
                output += '_ '

        return output

    def determine_universe_state(self):
        self.update.clear()
        for i in range(self.size):
            if self.check_neighbors(i) != self.universe[i]:
                self.update.append(i)
        self.update_cells()

    def check_neighbors(self, index) -> int:
        """
        Checks the number of neighbors that are alive

        :param index: Cell we are checking neighbors of
        :return: 0 or 1, result for if the cell should be alive or dead after
        the neighbor check.
        """
        is_alive = False
        if self.universe[index] == ALIVE:
            is_alive = True

        num_neighbors = 0
        x, y = self.x_y_conv(index)
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == 0 and j == 0:
                    continue
                if self.universe[self.linear_conv((x - i) % 5, (y - j) % 5)] == ALIVE:
                    num_neighbors += 1
                    if num_neighbors > 3:
                        break
        if is_alive:
            if num_neighbors < 2 or num_neighbors > 3:
                return DEAD
            else:
                return ALIVE
        else:
            if num_neighbors == 3:
                return ALIVE
        return DEAD

    def update_cells(self):
        for i in self.update:
            state = self.universe[i]
            if state == ALIVE:
                self.universe[i] = DEAD
            else:
                self.universe[i] = ALIVE

    def x_y_conv(self, index) -> (int, int):
        x = index % self.width
        y = int(index / self.width)

        return x, y

    def linear_conv(self, x, y) -> int:
        return (self.width * y) + x


if __name__ == "__main__":
    universe = Universe(40, 40)
    while True:
        if 1 not in universe.universe:
            os.system("clear")
            print("The universe has died!")
            exit()
        os.system("clear")
        print(universe)
        universe.determine_universe_state()
        time.sleep(1)
