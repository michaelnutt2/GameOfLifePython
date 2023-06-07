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
        self.universe = life.Universe(135296, 5, 5)

    def test_initial_universe(self):
        self.assertEqual(self.universe_test, self.universe.universe)

    def test_check_neighbors(self):
        ...


if __name__ == '__main__':
    unittest.main()
