# 封装工具类
import random


class Common:

    def test(self):
        return 'Here is the util class'


class Board:
    def __init__(self, row, col):

        self.row_num = row
        self.col_num = col

        self.status = [[random.random() > 0.5 for i in range(col)] for j in range(row)]

    def refactor(self):
        for i in range(self.row_num):
            self.status[i].append(0)
            self.status[i].insert(0, 0)
        self.status.append([0 for i in range(self.col_num + 2)])
        self.status.insert(0, [0 for i in range(self.col_num + 2)])
        return self.status

    def get_single_cell_status(self, row, col):
        if len(self.status) == self.row_num:
            self.refactor()
        row_change = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_change = [-1, 0, 1, -1, 1, -1, 0, 1]
        neighbor_alive_num = 0
        for i in range(8):
            neighbor_alive_num += self.status[1 + row + row_change[i]][1 + col + col_change[i]]
        if neighbor_alive_num == 3:
            return 1
        elif neighbor_alive_num == 2:
            return self.status[1 + row][1 + col]
        else:
            return 0

