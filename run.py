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

# Sets
player_guesses = set()

computer_guess_hit = set()

computer_hit = set()

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
while computer_ships > 0:
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

# Prompt the player for user input until a valid input is accepted
    while True:
        try:
            x = int(input("Choose Row: "))
            y = int(input("Choose Column: "))
            if x < 0 or x > 4 or y < 0 or y > 4:
                raise ValueError("Choose a number betweeb 0 and 4!")
            elif (x, y) in player_guesses:
                raise ValueError("You already guessed that combination")
            else:
                break
        except ValueError as error:
            print("invalid input:", error)

    player_guesses.add((x, y))

# Checks player guess for valide coordinates within range
    if x < board_size and y < board_size:
        if computer_board[x][y] == 1:
            print("Hit!")
            computer_board[x][y] = 0
        else:
            print("Miss.")

# This statement checks if the computer hits a ship
# storing its coordinates in a set

    while True:
        if len(computer_guess_hit) > 0:
            (x, y) = computer_guess_hit.pop()
            if player_board[x][y] == 1:
                print("The computer hit your ship!")
                player_board[x][y] = 0
            else:
                print("The computer missed")
                if len(computer_guess_hit) == 0:
                    break
        else:
            x = random.randint(0, board_size - 1)
            y = random.randint(0, board_size - 1)
            if (x, y) not in computer_hit:
                computer_hit.add((x, y))
                if player_board[x][y] == 1:
                    print("The computer hit your ship")
                    player_board[x][y] = 0
                    computer_hit.add((x, y))
                else:
                    print("The computer missed")
                break

# Check if the game is over by seeing if the rows and columns all = 0

    if sum(sum(row) for row in player_board) == 0:
        print("The computer wins")
        break
    elif sum(sum(row) for row in computer_board) == 0:
        print("You win!")
        break
