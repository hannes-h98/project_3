import random


# Welcome message and rules
def print_rules():
    """Function to print out the rules"""
    print("Let's play Battleships!.")
    print("You and the computer each have 3 ships.")
    print("The computer's ships are hidden.")
    print("Your ships are marked with a 1.")
    print("You have to guess a row and column between 0-4 (0 indexing).")
    print("You can not guess the same number combination twice.")


print_rules()

# Set up the board as a 5x5 grid using two lists where
# 0 represents the spaces on the board
board_size = 5
player_board = [[0 for x in range(board_size)] for y in range(board_size)]
computer_board = [[0 for x in range(board_size)] for y in range(board_size)]

# Generate random coordinates and loop untill all 3 ships are placed on board
player_ships = 3
while player_ships > 0:
    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)
    if player_board[x][y] == 0:
        player_board[x][y] = 1
        player_ships -= 1

# Generate the computers ships in the same way
computer_ships = 3
while player_ships > 0:
    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)
    if computer_board[x][y] == 0:
        computer_board[x][y] = 1
        computer_ships -= 1

# Print the boards with a loop that continues untill game ends
while True:
    print("player's board:")
    for row in player_board:
        board_string = ""
        for value in row:
            board_string += str(value)
            print(board_string)

    # Print computer board with hidden ships disguised as 0s
    print("computer's board:")
    for row in computer_board:
        board_string = ""
        for value in row:
            if value == 1:
                board_string += "0"
            else:
                board_string += str(value)
        print(board_string)
