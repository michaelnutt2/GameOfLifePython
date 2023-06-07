import unittest

import life


class TestUniverse(unittest.TestCase):
    def setUp(self) -> None:
        self.universe = [
            0, 0, 0, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 0, 0, 0
        ]

    def test_initial_universe(self):
        self.assertEqual(self.universe, life.initial_universe(135296))


if __name__ == '__main__':
    unittest.main()
