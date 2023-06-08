import unittest

import life


class TestUniverse(unittest.TestCase):
    def setUp(self) -> None:
        self.universe_test = [
            0, 0, 0, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 0, 0, 0
        ]
        self.universe = life.Universe(5, 5)
        self.universe.universe = self.universe_test

    def test_x_y_conv(self):
        self.assertEqual((4, 4), self.universe.x_y_conv(24))

    def test_linear_conv(self):
        self.assertEqual(24, self.universe.linear_conv(4, 4))

    def test_check_neighbors_start_alive_end_dead(self):
        self.assertEqual(0, self.universe.check_neighbors(7))

    def test_check_neighbors_start_dead_end_alive(self):
        self.assertEqual(1, self.universe.check_neighbors(11))

    def test_check_neighbors_start_alive_end_alive(self):
        self.assertEqual(1, self.universe.check_neighbors(12))

    def test_check_neighbors_start_dead_end_dead(self):
        self.assertEqual(0, self.universe.check_neighbors(0))

    def test_update_cells(self):
        self.universe.update = [0]
        self.universe.update_cells()
        self.assertEqual(1, self.universe.universe[0])


if __name__ == '__main__':
    unittest.main()
