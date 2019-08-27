import unittest
from NumberOfPaths import recursive_solution, iterative_solution

class TestKPair(unittest.TestCase):

    def setUp(self):
        pass

    def test_1_cell_grid(self):
        row = 1
        col = 1
        grid = [[0 for i in range(col)] for j in range(row)]

        self.assertEqual(recursive_solution(0, 0, grid), 0)
        self.assertEqual(iterative_solution(grid), 0)

    def test_1_cell_grid_with_1(self):
        row = 1
        col = 1
        grid = [[0 for i in range(col)] for j in range(row)]
        grid[0][0] = 1

        self.assertEqual(recursive_solution(0, 0, grid), 0)
        self.assertEqual(iterative_solution(grid), 0)

    def test_row_vector(self):
        row = 1
        col = 4
        grid = [[0 for i in range(col)] for j in range(row)]

        self.assertEqual(recursive_solution(0, 0, grid), 1)
        self.assertEqual(iterative_solution(grid), 1)

        grid[0][2] = 1

        self.assertEqual(recursive_solution(0, 0, grid), 0)
        self.assertEqual(iterative_solution(grid), 0)

    def test_col_vector(self):
        row = 4
        col = 1
        grid = [[0 for i in range(col)] for j in range(row)]

        self.assertEqual(recursive_solution(0, 0, grid), 1)
        self.assertEqual(iterative_solution(grid), 1)

        grid[2][0] = 1

        self.assertEqual(recursive_solution(0, 0, grid), 0)
        self.assertEqual(iterative_solution(grid), 0)

    def test_unequal_sides(self):
        row = 4
        col = 2

        grid = [[0 for i in range(col)] for j in range(row)]

        self.assertEqual(recursive_solution(0, 0, grid), 4)
        self.assertEqual(iterative_solution(grid), 4)

        grid[2][0] = 1

        self.assertEqual(recursive_solution(0, 0, grid), 2)
        self.assertEqual(iterative_solution(grid), 2)

        grid[0][0] = 1

        self.assertEqual(recursive_solution(0, 0, grid), 0)
        self.assertEqual(iterative_solution(grid), 0)

    def test_equal_sides(self):
        row = 4
        col = 4

        grid = [[0 for i in range(col)] for j in range(row)]

        self.assertEqual(recursive_solution(0, 0, grid), 20)
        self.assertEqual(iterative_solution(grid), 20)

        grid[2][0] = 1

        self.assertEqual(recursive_solution(0, 0, grid), 16)
        self.assertEqual(iterative_solution(grid), 16)

        grid[0][0] = 1

        self.assertEqual(recursive_solution(0, 0, grid), 0)
        self.assertEqual(iterative_solution(grid), 0)

if __name__ == "__main__":
    unittest.main()