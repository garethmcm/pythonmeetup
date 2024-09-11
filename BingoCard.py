import random

class BingoCard:
    def __init__(self):
        self.bingo_card_rows = self.generate_bingo_card()
        self.bingo_card_cols = self.pivot_bingo_card(self.bingo_card_rows)
        self.rows_hit = [0] * 5
        self.cols_hit = [0] * 5
        self.row_hit_count = 0
        self.col_hit_count = 0

    def generate_bingo_card(self):
        # Define the bingo card structure as a 2D array
        bingo_card = [[0] * 5 for _ in range(5)]
        
        # Populate the bingo card with random numbers
        for col, (start, end) in enumerate([(1, 15), (16, 30), (31, 45), (46, 60), (61, 75)]):
            column_numbers = random.sample(range(start, end + 1), 5)
            for row in range(5):
                bingo_card[row][col] = column_numbers[row]
        
        # The center space is a free space
        bingo_card[2][2] = 'FREE'
        
        return bingo_card

    def pivot_bingo_card(self, bingo_card):
        # Pivot the 2D array (transpose the card)
        return [[bingo_card[row][col] for row in range(5)] for col in range(5)]

    def print_bingo_card(self, bingo_card):
        for row in bingo_card:
            print(row)

    def bingo_hit(self, n: int):
        # Check rows
        for row_index, row in enumerate(self.bingo_card_rows):
            if n in row:
                self.rows_hit[row_index] += 1
                if self.rows_hit[row_index] == 5:
                    print("Bingo row!")
                    return "R"

        # Check columns
        for col_index, col in enumerate(self.bingo_card_cols):
            if n in col:
                self.cols_hit[col_index] += 1
                if self.cols_hit[col_index] == 5:
                    print("Bingo column!")
                    return "C"

        return None

    def play_bingo(self):
        bingo_numbers = random.sample(range(1, 76), 75)
        for bingo_number in bingo_numbers:
            hit = self.bingo_hit(bingo_number)
            if hit == "R":
                self.row_hit_count += 1
                return "R"
            elif hit == "C":
                self.col_hit_count += 1
                return "C"

# Create a BingoCard instance and play the game
bingo_game = BingoCard()
bingo_game.print_bingo_card(bingo_game.bingo_card_rows)
bingo_game.print_bingo_card(bingo_game.bingo_card_cols)

# Simulate multiple games
for i in range(50):
    win = bingo_game.play_bingo()
    print(bingo_game.row_hit_count, bingo_game.col_hit_count)
