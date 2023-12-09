import unittest
from optimizer import super_shopping_optimizer

class TestSuperShoppingOptimizer(unittest.TestCase):

    def test_example_case(self):
        n = 3
        distances = [[0, 10, 15], [10, 0, 20], [15, 20, 0]]
        items = [[5, 10], [20, 30], [15, 25]]
        travel_cost = 2
        expected_output = 50
        self.assertEqual(super_shopping_optimizer(n, distances, items, travel_cost), expected_output)

    def test_case_with_no_items(self):
        n = 3
        distances = [[0, 10, 15], [10, 0, 20], [15, 20, 0]]
        items = [[], [], []]
        travel_cost = 2
        expected_output = 30
        self.assertEqual(super_shopping_optimizer(n, distances, items, travel_cost), expected_output)

    def test_case_with_one_department(self):
        n = 1
        distances = [[0]]
        items = [[5, 10]]
        travel_cost = 2
        expected_output = 5
        self.assertEqual(super_shopping_optimizer(n, distances, items, travel_cost), expected_output)

    def test_case_with_high_travel_cost(self):
        n = 3
        distances = [[0, 10, 15], [10, 0, 20], [15, 20, 0]]
        items = [[5, 10], [20, 30], [15, 25]]
        travel_cost = 1000
        expected_output = 30000
        self.assertEqual(super_shopping_optimizer(n, distances, items, travel_cost), expected_output)

if __name__ == "__main__":
    unittest.main()
