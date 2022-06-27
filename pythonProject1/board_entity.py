

class Board:
    def __init__(self):
        self.__board = [[0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]
        self.__dimension = 7

    def set_symbol(self, symbol, row, column):
        self.__board[row][column] = symbol


    def make_board(self):
        for row in range(0, self.__dimension):
            for column in range(0, self.__dimension):
                self.__board[row][column] = 0
    @property
    def get_dimension(self):
        return self.__dimension

    def get_symbol(self, row, column):
        return self.__board[row][column]

    def __str__(self):
        board_str = ""
        for row in range(0, self.__dimension ):
            for column in range(0, self.__dimension ):
                board_str += " " + str(self.__board[row][column])
            board_str += "\n"
        return board_str

    @staticmethod
    def check_if_position_is_in_board(row, column):
        "Check if the position given is in the board"
        if row < 0 or row > 6 or column < 0 or column > 6:
            return False
        return True

    def empty_spaces_around(self, row, column):
        row_directions = [0, 1, 0, -1]
        column_directions = [1, 0, -1, 0]
        empty_spaces_around = 4
        for direction_index in range(4):
            next_x_position = row + row_directions[direction_index]
            next_y_position = column + column_directions[direction_index]
            if self.check_if_position_is_in_board(next_x_position, next_y_position) and self.get_symbol(next_x_position, next_y_position) == 'a':
                empty_spaces_around -= 1
        return empty_spaces_around



#board = Board(7)
#board.make_board()
#board.set_symbol('a', 3, 5)
#print(board)
#print(board.get_dimension)
#print(board.empty_spaces_around(2,5))