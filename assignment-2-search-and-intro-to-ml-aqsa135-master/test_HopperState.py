#Aqsa Noreen

import unittest
from HopperState import HopperState, hopper1max, hopper2max, hopper3max

class TestHopperState(unittest.TestCase):

    def test_eq(self):
        h1 = HopperState(3, 5, 0)
        h2 = HopperState(3, 5, 0)
        self.assertEqual(h1, h2)

    def test_hash(self):
        h1 = HopperState(3, 5, 0)
        h2 = HopperState(3, 5, 0)
        self.assertEqual(hash(h1), hash(h2))

    def test_lt(self):
        h1 = HopperState(3, 5, 0)
        h2 = HopperState(3, 5, 0)
        h1.cost = 5
        h2.cost = 10
        self.assertTrue(h1 < h2)

    def test_successors(self):
        h = HopperState(3, 2, 0)
        successors = h.successors()

        # Define expected successors and actions
        expected_successors = {
            "Fill Hopper 1": HopperState(hopper1max, 2, 0),
            "Fill Hopper 2": HopperState(3, hopper2max, 0),
            "Fill Hopper 3": HopperState(3, 2, hopper3max),
            "Dump Hopper 1": HopperState(0, 2, 0),
            "Dump Hopper 2": HopperState(3, 0, 0),
            "Pour from 1 to 2": HopperState(0, 5, 0),
            "Pour from 1 to 3": HopperState(0, 2, 3),
            "Pour from 2 to 1": HopperState(5, 0, 0),
            "Pour from 2 to 3": HopperState(3, 0, 2),
        }

        # Check if the successors are correctly generated
        self.assertEqual(len(successors), len(expected_successors))
        for succ in successors:
            self.assertIn(succ.prev_action, expected_successors)
            self.assertEqual(succ, expected_successors[succ.prev_action])


if __name__ == '__main__':
    unittest.main()
