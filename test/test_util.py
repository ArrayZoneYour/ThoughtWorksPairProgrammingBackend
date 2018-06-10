from util import Board
import unittest


class TestUtil(unittest.TestCase):

    def test_board_initialize_3_3(self):
        board = Board(3, 3)
        self.assertIsNot(board.status[0][0], True)
        self.assertIsNot(board.status[0][0], False)
        self.assertEqual(len(board.status), 3)
        self.assertEqual(len(board.status[0]), 3)

    def test_board_initialize_5_5(self):
        board = Board(5, 5)
        self.assertIsNot(board.status[0][0], True)
        self.assertIsNot(board.status[0][0], False)
        self.assertEqual(len(board.status), 5)
        self.assertEqual(len(board.status[0]), 5)

    def test_get_board_row_and_col(self):
        board = Board(4, 7)
        self.assertEqual(board.row_num, 4)
        self.assertEqual(board.col_num, 7)

    def test_get_random_board_all_die(self):
        board = Board(5, 5, random_alive_cell_prop=0)
        row_sum = [sum(row) for row in board.status]
        live_cell = sum(row_sum)
        self.assertEqual(live_cell, 0)

    def test_get_random_board_all_live(self):
        board = Board(4, 4, random_alive_cell_prop=1)
        row_sum = [sum(row) for row in board.status]
        live_ceil = sum(row_sum)
        self.assertEqual(live_ceil, 16)

    def test_refactor_board(self):
        origin_board = Board(5, 8)
        refactor_board = origin_board.add_zero_padding()
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
        self.assertEqual(origin_board.get_single_cell_status(0, 1), 0)
        self.assertEqual(origin_board.get_single_cell_status(0, 2), 1)
        self.assertEqual(origin_board.get_single_cell_status(1, 0), 1)
        self.assertEqual(origin_board.get_single_cell_status(1, 1), 0)
        self.assertEqual(origin_board.get_single_cell_status(1, 2), 1)
        self.assertEqual(origin_board.get_single_cell_status(2, 0), 0)
        self.assertEqual(origin_board.get_single_cell_status(2, 1), 1)
        self.assertEqual(origin_board.get_single_cell_status(2, 2), 0)

    def test_rollback_to_origin_board(self):
        origin_board = Board(3, 3)
        origin_status = origin_board.status.copy()
        origin_board.add_zero_padding()
        origin_board.remove_zero_padding()
        self.assertEqual(origin_board.status, origin_status)

    def test_get_next_time_status(self):
        board = Board(3, 3)
        board.status = [
            [0, 1, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        board_copy = board.status.copy()
        board.get_next_status()
        self.assertEqual(board.history, [board_copy])
        self.assertEqual(board.status, [
            [1, 0, 1],
            [1, 0, 1],
            [0, 1, 0]
        ])

    def test_iter_n(self):
        board = Board(3, 3)
        board.status = [
            [0, 1, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        board.iter_n(3)
        self.assertEqual(board.history, [
            [
                [0, 1, 1],
                [1, 1, 1],
                [0, 0, 0]
            ],
            [
                [1, 0, 1],
                [1, 0, 1],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 0, 1],
                [0, 1, 0]
            ]
        ])


if __name__ == '__main__':
    unittest.main()
