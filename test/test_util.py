from util import Board
import unittest


class TestUtil(unittest.TestCase):

    def test_board_initialize_3_3(self):
        board = Board(3, 3)
        self.assertEqual(len(board.status), 3)
        self.assertEqual(len(board.status[0]), 3)

    def test_board_initialize_5_5(self):
        board = Board(5, 5)
        self.assertEqual(len(board.status), 5)
        self.assertEqual(len(board.status[0]), 5)

    def test_get_board_row_and_col(self):
        board = Board(4, 7)
        self.assertEqual(board.row_num, 4)
        self.assertEqual(board.col_num, 7)

    def test_get_random_board_not_all_die(self):
        board = Board(5, 5)
        row_sum = [sum(row) for row in board.status]
        live_cell = sum(row_sum)
        self.assertTrue(live_cell > 1)

    def test_get_random_board_not_all_live(self):
        board = Board(4, 4)
        row_sum = [sum(row) for row in board.status]
        live_ceil = sum(row_sum)
        self.assertTrue(live_ceil < 16)

    def test_refactor_board(self):
        origin_board = Board(5, 8)
        refactor_board = origin_board.refactor()
        self.assertEqual(len(refactor_board), 7)
        self.assertEqual(len(refactor_board[0]), 10)

    def test_get_single_cell_status(self):
        origin_board = Board(3, 3)
        origin_board.status = [
            [0, 1, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]

        self.assertEqual(origin_board.get_single_cell_status(0, 0), 1)
        self.assertEqual(origin_board.get_single_cell_status(2, 2), 0)
        self.assertEqual(origin_board.get_single_cell_status(0, 1), 0)
        self.assertEqual(origin_board.get_single_cell_status(0, 2), 1)
        self.assertEqual(origin_board.get_single_cell_status(1, 0), 1)
        self.assertEqual(origin_board.get_single_cell_status(1, 1), 0)
        self.assertEqual(origin_board.get_single_cell_status(1, 2), 1)
        self.assertEqual(origin_board.get_single_cell_status(2, 0), 0)
        self.assertEqual(origin_board.get_single_cell_status(2, 1), 1)

    def test_get(self):
        pass



if __name__ == '__main__':
    unittest.main()
