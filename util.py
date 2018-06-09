# 封装工具类
import random
import copy


class Common:

    def test(self):
        return 'Here is the util class'


class Board:
    def __init__(self, row, col):

        self.row_num = row
        self.col_num = col

        self.status = [[int(random.random() > 0.5) for i in range(col)] for j in range(row)]
        self.history = []

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

    def rollback(self):
        self.status.pop(0)
        self.status.pop()
        for i in range(self.row_num):
            self.status[i].pop(0)
            self.status[i].pop()

    def get_next_time_status(self):
        next_time_status = copy.deepcopy(self.status)
        self.refactor()
        for row in range(0, self.row_num):
            for col in range(0, self.col_num):
                next_time_status[row][col] = self.get_single_cell_status(row, col)
        self.rollback()
        self.history.append(self.status.copy())
        self.status = next_time_status

    def iter_n(self, n=50):
        for i in range(n):
            self.get_next_time_status()


