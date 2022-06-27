from board_entity import Board
from random import randint
from enum import Enum


class GameState(Enum):
    ONGOING = 0
    OVER = 1


class Game:
    def __init__(self):
        self.__board = Board()
        self.__snake = [[2,3], [3,3], [4,3]]
        self.__snake_head = [2,3]


    def place_snake(self):
        middle = self.__board.get_dimension // 2
        self.__board.set_symbol('+', middle, middle)
        self.__board.set_symbol('*', middle-1, middle)
        self.__board.set_symbol('+', middle+1, middle)

    def place_apple(self, row, column):
        self.__board.set_symbol('a', row, column)

    def place_n_apples(self, n):
        for index in range(0, n):
            row = randint(0, self.__board.get_dimension-1)
            column = randint(0, self.__board.get_dimension-1)
            while self.__board.get_symbol(row, column) == '+' or self.__board.get_symbol(row, column) == 'a' or self.__board.get_symbol(row, column) == '*' or self.__board.empty_spaces_around(row,column) != 4 or self.__board.check_if_position_is_in_board(row,column) is not True:
                row = randint(0, self.__board.get_dimension-1)
                column = randint(0, self.__board.get_dimension-1)
            self.place_apple(row, column)

    def place_new_apple(self):
        row = randint(0, self.__board.get_dimension - 1)
        column = randint(0, self.__board.get_dimension - 1)
        while self.__board.get_symbol(row, column) == '+' or self.__board.get_symbol(row,column) == 'a' or self.__board.get_symbol(row, column) == '*' or self.__board.empty_spaces_around(row,column) != 4 or self.__board.check_if_position_is_in_board(row, column) is not True:
            row = randint(0, self.__board.get_dimension - 1)
            column = randint(0, self.__board.get_dimension - 1)
        self.place_apple(row, column)



    def move_up(self):
        snake_head_x = self.__snake_head[0] - 1
        snake_head_y = self.__snake_head[1]
        apple_eaten = 0
        if not self.__board.check_if_position_is_in_board(snake_head_x, snake_head_y):
            return -1
        if self.__board.get_symbol(snake_head_x, snake_head_y) == '+':
            return -1
        if self.__board.get_symbol(snake_head_x, snake_head_y) == 'a':
            apple_eaten = 1

        self.__board.set_symbol('+', self.__snake_head[0], self.__snake_head[1])
        self.__board.set_symbol('*', snake_head_x, snake_head_y)
        self.__snake_head[0] = snake_head_x
        self.__snake_head[1] = snake_head_y
        self.__snake.insert(0, [snake_head_x, snake_head_y])
        if apple_eaten == 0:
            snake_tail = self.__snake[-1]
            snake_tail_x = snake_tail[0]
            snake_tail_y = snake_tail[1]
            self.__board.set_symbol(0, snake_tail_x, snake_tail_y)
            self.__snake.pop(-1)
        if apple_eaten == 1:
            self.place_new_apple()
        return 1

    def move_right(self):
        snake_head_x = self.__snake_head[0]
        snake_head_y = self.__snake_head[1] + 1
        apple_eaten = 0
        if not self.__board.check_if_position_is_in_board(snake_head_x, snake_head_y):
            return -1
        if self.__board.get_symbol(snake_head_x, snake_head_y) == '+':
            return -1
        if self.__board.get_symbol(snake_head_x, snake_head_y) == 'a':
            apple_eaten = 1

        self.__board.set_symbol('+', self.__snake_head[0], self.__snake_head[1])
        self.__board.set_symbol('*', snake_head_x, snake_head_y)
        self.__snake_head[0] = snake_head_x
        self.__snake_head[1] = snake_head_y
        self.__snake.insert(0, [snake_head_x, snake_head_y])
        if apple_eaten == 0:
            snake_tail = self.__snake[-1]
            snake_tail_x = snake_tail[0]
            snake_tail_y = snake_tail[1]
            self.__board.set_symbol(0, snake_tail_x, snake_tail_y)
            self.__snake.pop(-1)
        if apple_eaten == 1:
            self.place_new_apple()
        return 1

    def move_down(self):
        snake_head_x = self.__snake_head[0] + 1
        snake_head_y = self.__snake_head[1]
        apple_eaten = 0
        if not self.__board.check_if_position_is_in_board(snake_head_x, snake_head_y):
            return -1
        if self.__board.get_symbol(snake_head_x, snake_head_y) == '+':
            return -1
        if self.__board.get_symbol(snake_head_x, snake_head_y) == 'a':
            apple_eaten = 1

        self.__board.set_symbol('+', self.__snake_head[0], self.__snake_head[1])
        self.__board.set_symbol('*', snake_head_x, snake_head_y)
        self.__snake_head[0] = snake_head_x
        self.__snake_head[1] = snake_head_y
        self.__snake.insert(0, [snake_head_x, snake_head_y])
        if apple_eaten == 0:
            snake_tail = self.__snake[-1]
            snake_tail_x = snake_tail[0]
            snake_tail_y = snake_tail[1]
            self.__board.set_symbol(0, snake_tail_x, snake_tail_y)
            self.__snake.pop(-1)
        if apple_eaten == 1:
            self.place_new_apple()
        return 1

    def move_left(self):
        snake_head_x = self.__snake_head[0]
        snake_head_y = self.__snake_head[1] - 1
        apple_eaten = 0
        if not self.__board.check_if_position_is_in_board(snake_head_x, snake_head_y):
            return -1
        if self.__board.get_symbol(snake_head_x, snake_head_y) == '+':
            return -1
        if self.__board.get_symbol(snake_head_x, snake_head_y) == 'a':
            apple_eaten = 1

        self.__board.set_symbol('+', self.__snake_head[0], self.__snake_head[1])
        self.__board.set_symbol('*', snake_head_x, snake_head_y)
        self.__snake_head[0] = snake_head_x
        self.__snake_head[1] = snake_head_y
        self.__snake.insert(0, [snake_head_x, snake_head_y])
        if apple_eaten == 0:
            snake_tail = self.__snake[-1]
            snake_tail_x = snake_tail[0]
            snake_tail_y = snake_tail[1]
            self.__board.set_symbol(0, snake_tail_x, snake_tail_y)
            self.__snake.pop(-1)
        if apple_eaten == 1:
            self.place_new_apple()
        return 1


    def board(self):
        return self.__board



# game = Game()
# game.place_snake()
# game.place_n_apples(7)
# print(game.board())
# game.move_up()
# print(game.board())
# game.move_right()
# print(game.board())
