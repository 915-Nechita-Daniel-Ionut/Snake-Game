from game import Game,GameState



class GameUI:
    def __init__(self):
        self.__game = Game()

    @staticmethod
    def read_move():
        print("Movement commands: move, move up, move down, move left, move right, move [n], and at move[n] n cant be more than 9")
        move = input()
        if move == "move":
            return 0
        if move == "move up":
            return 1
        if move == "move down":
            return 2
        if move == "move left":
            return 3
        if move == "move right":
            return 4
        if len(move) == 8:
            if move[5] == '[' and move[7] == ']':
                try:
                    number_of_spaces = int(move[6])
                except ValueError:
                    return -1
                if number_of_spaces == 1 or number_of_spaces > 9:
                    return -1
                else:
                    return 50 + number_of_spaces

        return -1

    @staticmethod
    def read_apples():
        print("How many apples do you want to start with, however it cant be more than 5")
        apples = int(input())
        if apples > 5:
            raise ValueError
        return apples


    def game_start(self):
        while True:
            try:
                apples = self.read_apples()
                break
            except ValueError:
                print("Invalid data")

        self.__game.place_snake()
        self.__game.place_n_apples(apples)
        print(self.__game.board())
        last_move = 1
        while True:

            while True:
                move = self.read_move()
                if move != -1:
                    break
                else:
                    print("Invalid data")

            if move == 0:
                move = last_move
            if move == 1:
                state = self.__game.move_up()
                if state == -1 or last_move == 2:
                    break
                last_move = 1
            elif move == 2:
                state = self.__game.move_down()
                if state == -1 or last_move == 1:
                    break
                last_move = 2
            elif move == 3:
                state = self.__game.move_left()
                if state == -1 or last_move == 4:
                    break
                last_move = 3
            elif move == 4:
                state = self.__game.move_right()
                if state == -1 or last_move == 3:
                    break
                last_move = 4
            else:
                move_times = move % 10
                move = last_move
                for index in range(0, move_times):
                    if move == 1:
                        state = self.__game.move_up()
                        if state == -1 or last_move == 2:
                            break
                        last_move = 1
                    elif move == 2:
                        state = self.__game.move_down()
                        if state == -1 or last_move == 1:
                            break
                        last_move = 2
                    elif move == 3:
                        state = self.__game.move_left()
                        if state == -1 or last_move == 4:
                            break
                        last_move = 3
                    elif move == 4:
                        state = self.__game.move_right()
                        if state == -1 or last_move == 3:
                            break
                        last_move = 4
            print(self.__game.board())





ui= GameUI()
ui.game_start()