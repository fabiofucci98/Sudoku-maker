import numpy as np


class Sudoku(object):

    def __init__(self):
        self.grid = np.zeros((9, 9))
        self.sudoku_solver()

    def sudoku_solver(self, position=(0, 0)):
        guesses = self.get_guesses(position)
        if len(guesses) == 0:
            return False
        num = self.random_guess(guesses)
        self.assign(num, position)
        if(self.end(position)):
            return True
        copy_position = self.increment(position)

        while not self.sudoku_solver(copy_position):
            guesses.remove(num)
            if len(guesses) == 0:
                self.clear(position)
                return False
            num = self.random_guess(guesses)
            self.assign(num, position)
        return True

    def check_solution(self):
        if (self.solution == self.grid).all():
            return True
        return False

    def remove_some_values(self):
        self.solution = self.grid.copy()
        print(self.solution)
        i = 0
        while i < 30:
            row = np.random.randint(0, 9)
            column = np.random.randint(0, 9)
            if self.grid[row, column] != 0:
                self.grid[row, column] = 0
                i += 1

    def clear(self, position):
        self.grid[position[0], position[1]] = 0

    def assign(self, num, position):
        self.grid[position[0], position[1]] = num

    def random_guess(self, guesses):
        index = np.random.randint(0, len(guesses))
        return guesses[index]

    def get_guesses(self, position):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        guesses = []
        for num in numbers:
            if self.cell_can_contain(position, num):
                guesses.append(num)
        return guesses

    def cell_can_contain(self, position, num):
        if not self.row_can_contain(position[0], num):
            return False
        if not self.column_can_contain(position[1], num):
            return False
        if not self.square_can_contain(position[0], position[1], num):
            return False
        return True

    def row_can_contain(self, row, number):
        values = []
        for num in self.grid[row]:
            values.append(num)
        if number in values:
            return False
        return True

    def column_can_contain(self, column, number):
        values = []
        for num in self.grid[:, column]:
            values.append(num)
        if number in values:
            return False
        return True

    def square_can_contain(self, row, column, number):
        row_first_index, row_last_index = self.get_indexes(row)
        column_first_index, column_last_index = self.get_indexes(column)
        sub_grid = self.grid[row_first_index:row_last_index+1,
                             column_first_index: column_last_index+1]

        values = []
        for row in sub_grid:
            for num in row:
                values.append(num)
        if number in values:
            return False
        return True

    def get_indexes(self, index):
        if index < 3:
            return 0, 2
        if index > 2 and index < 6:
            return 3, 5
        else:
            return 6, 8

    def increment(self, position):
        if position[1] == 8:
            return (position[0]+1, 0)
        else:
            return (position[0], position[1]+1)

    def end(self, position):
        if position[0] >= 8 and position[1] >= 8:
            return True
        return False

    def remove(self, num_to_remove):
        for n in range(0, num_to_remove):
            i = np.random.randint(0, 9)
            j = np.random.randint(0, 9)
            while self.grid[i][j] == 0:
                i = np.random.randint(0, 9)
                j = np.random.randint(0, 9)

            self.grid[i][j] = 0

    def __str__(self):
        return str(self.grid)


def main():
	sudoku = Sudoku()
	print(sudoku)

if __name__ == "__main__":
    main()
