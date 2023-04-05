import random


class Game:

    def __init__(self, side, dif):
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
        self.side = side
        self.ai_side = ""
        self.ai_go = ""
        self.is_game = True
        self.draw = False
        self.dif = dif
        self.winner = ""
        self.winner_pos = False
        self.x_points = 0
        self.o_points = 0

    # print out position
    def game_situation_update(self):
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

        # ai side
        if self.side == "X":
            self.ai_side = 'O'
        else:
            self.ai_side = "X"

        self.is_game = self.check_win()
        if self.is_game:

            draw = self.check_draw()
            if draw:
                self.game_situation_update()
                self.is_game = False
                self.draw = True
                return False
            else:
                if self.dif == "very_easy":
                    self.ai_step_very_easy()
                else:
                    self.ai_step()
                self.game_situation_update()
                self.is_game = self.check_win()
        else:
            return False

    # check every step if there is a winner
    def check_win(self):
        for tup in self.winning_positions:
            for_check = f"{self.symbols[tup[0]]}{self.symbols[tup[1]]}{self.symbols[tup[2]]}"
            if for_check == "XXX":
                print("Here's is our winner, congratulations to X!")
                self.winner = "X"
                self.x_points += 1
                self.winner_pos = tup
                return False
            elif for_check == "OOO":
                print("Here's is our winner, congratulations to O!")
                self.winner = "O"
                self.o_points += 1
                self.winner_pos = tup
                return False
        return True

    # check if draw
    def check_draw(self):
        for_check = [key for key in self.symbols if self.symbols[key] == " "]
        if not for_check:
            return True
        else:
            return False

    # -------- AI LOGIC --------

    def ai_step_very_easy(self):
        free_spot = [key for key in self.symbols if self.symbols[key] == " "]
        for tup in self.winning_positions:
            count = [value for value in tup if self.symbols[value] != f"{self.side}" and
                     (self.symbols[value] == " ")]
            check_for_ai = [value for value in tup if self.symbols[value] == f"{self.ai_side}"]
            if len(count) == 1 and not check_for_ai:
                self.ai_go = count[0]
                break
            else:
                count = "long"

        print(f"count: {count}")
        if len(count) > 1:
            self.ai_go = random.choice(free_spot)

        if free_spot:
            self.symbols[self.ai_go] = self.ai_side

    def ai_step(self):
        free_spot = [key for key in self.symbols if self.symbols[key] == " "]
        # first go to the center
        if self.symbols[22] == " ":
            self.ai_go = 22
            count = "1"
        else:
            for tup in self.winning_positions:
                count = [value for value in tup if self.symbols[value] != f"{self.side}" and
                         (self.symbols[value] == " ")]
                check_for_ai = [value for value in tup if self.symbols[value] == f"{self.ai_side}"]
                if len(count) == 1 and not check_for_ai:
                    self.ai_go = count[0]
                    break
                else:
                    count = "long"

        print(f"count: {count}")
        if len(count) > 1:
            self.ai_go = random.choice(free_spot)

        if free_spot:
            self.symbols[self.ai_go] = self.ai_side


