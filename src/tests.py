import unittest 
from core.maze import Maze
from core.gui import Window
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_draw_cell(self):
        num_cols = 15
        num_rows = 13
        m1 = Maze(Window(800, 600),0, 0, num_rows, num_cols, 20, 30)
        """
        The logic is :
        x1 = self._x1 + i * self._cell_size_x # Calculate the x-coordinate of the top left corner of the cell
        y1 = self._y1 + j * self._cell_size_y # Calculate the y-coordinate of the top left corner of the cell
        x2 = x1 + self._cell_size_x # Calculate the x-coordinate of the bottom right corner of the cell
        y2 = y1 + self._cell_size_y # Calculate the y-coordinate of the bottom right corner of the cell
        self._cells[i][j].draw(x1, x2, y1, y2)
        self._animate()
        """
        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                x1 = 0 + i * 20 # Calculate the x-coordinate of the top left corner of the cell
                y1 = 0 + j * 30 # Calculate the y-coordinate of the top left corner of the cell
                x2 = x1 + 20 # Calculate the x-coordinate of the bottom right corner of the cell
                y2 = y1 + 30 # Calculate the y-coordinate of the bottom right corner of the cell
                self.assertEqual(
                    m1._cells[i][j]._x1,
                    x1,
                )
                self.assertEqual(
                    m1._cells[i][j]._y1,
                    y1,
                )
                self.assertEqual(
                    m1._cells[i][j]._x2,
                    x2,
                )
                self.assertEqual(
                    m1._cells[i][j]._y2,
                    y2,
                )
    
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )
    
    def test_maze_break_walls_r(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_walls_r(0, 0)
        self.assertEqual(
            m1._cells[0][0].visited,
            True,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].visited,
            True,
        )


if __name__ == '__main__':
    unittest.main()