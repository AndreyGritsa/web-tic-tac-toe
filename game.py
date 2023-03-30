import sys, os
import pyautogui
import random

class Game:

    def __init__(self, side):
        self.symbols = {
            11: " ",
            12: " ",
            13: " ",
            21: " ",
            22: " ",
            23: " ",
            31: " ",
            32: " ",
            33: " ",
        }
        self.winning_positions = (
            (11, 12, 13),
            (21, 22, 23),
            (31, 32, 33),
            (11, 21, 31),
            (12, 22, 32),
            (13, 23, 33),
            (13, 22, 31),
            (11, 22, 33)
        )
        self.platform = "pycharm"
        self.side = side
        self.ai_side = ""

    def game_situation_update(self):
        # if self.platform == "pycharm":
        #     pyautogui.click(591, 797)
        #     pyautogui.hotkey("ctrl", "alt", "g")
        # else:
        #     self.clean_terminal()
        game_sit = f"""
                    {self.symbols[11]}|{self.symbols[12]}|{self.symbols[13]}
                     -----
                    {self.symbols[21]}|{self.symbols[22]}|{self.symbols[23]}
                     -----
                    {self.symbols[31]}|{self.symbols[32]}|{self.symbols[33]}
                """
        print(game_sit)
        print(self.symbols)

    # main engine
    def run(self):
        # self.side = input("Choose your side, 'X' or 'O': ")
        # self.side = self.side.title()

        # ai side
        if self.side == "X":
            self.ai_side = 'O'
        else:
            self.ai_side = "X"

        is_game = self.check_win()
        while is_game:
            if self.side == "X" or self.side == "O":
                self.location()
                draw = self.check_draw()
                if draw:
                    self.game_situation_update()
                    is_game = False
                    print("DRAW")
                else:
                    self.ai_step()
                    self.game_situation_update()
                    is_game = self.check_win()
            else:
                print("Only X and O are available, try again!")
                self.run()

    # check every step if there is a winner
    def check_win(self):
        for tup in self.winning_positions:
            for_check = f"{self.symbols[tup[0]]}{self.symbols[tup[1]]}{self.symbols[tup[2]]}"
            if for_check == "XXX":
                print("Here's is our winner, congratulations to X!")
                return False
            elif for_check == "OOO":
                print("Here's is our winner, congratulations to O!")
                return False
        return True

    def check_draw(self):
        for_check = [key for key in self.symbols if self.symbols[key] == " "]
        if for_check == []:
            return True
        else:
            return False

    # logic for choosing position
    def location(self):
        line = input("Choose line: ")
        if line in "123" and len(line) == 1: # line should be between 1 and 3
            is_not_correct = True
            while is_not_correct: # position should be between 1 and 3
                position = input("Choose position: ")
                if position in "123" and len(position) == 1:
                    is_not_correct = False
                else:
                    print("Position should be between 1 and 3, try again!")

            loc = int(f"{line}{position}")

            # check if position is already occupied
            if self.symbols[loc] != " ":
                loc = " "
                print("Place is occupied, try again!")
                self.location()

            print(f"Side: {self.side}, location: {loc}")
            print(f"Location where is should place the side: {loc} and the type is: {type(loc)}")
            self.symbols[loc] = self.side
        else:
            print("Line should be from 1 to 3, try again.")
            self.location()

    # clean terminal, should work on windows, mac and linux
    def clean_terminal(self):
        if sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clean")

    # -------- AI LOGIC --------

    def ai_step(self):
        free_spot = [key for key in self.symbols if self.symbols[key] == " "]
        # first go to the center
        if self.symbols[22] == " ":
            ai_go = 22
            count = "1"
        else:
            # occupied = [key for key in self.symbols if self.symbols[key] == f"{self.side}"]
            for tup in self.winning_positions:
                count = [value for value in tup if self.symbols[value] != f"{self.side}" and
                         (self.symbols[value] == " ")]
                check_for_ai = [value for value in tup if self.symbols[value] == f"{self.ai_side}"]
                if len(count) == 1 and not check_for_ai:
                    # self.symbols[count[0]] = self.ai_side
                    ai_go = count[0]
                    break
                else:
                    count = "long"

        print(f"count: {count}")
        if len(count) > 1:
            ai_go = random.choice(free_spot)

        if free_spot:
            self.symbols[ai_go] = self.ai_side


