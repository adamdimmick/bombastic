import random

# Set global constants
BOARDSIZE = 10
NUM_BOMBS = 5
ASCII_A = 65
CLEAR_UNCHECKED = 0
BOMB_UNCHECKED = 1
CLEAR_CHECKED = 2
BOMB_CHECKED = 3
CELL_SIZE = 3
LEFT_MARGIN = 4
BLOCK_CHAR = "\u2588"
DBLWALL_CHAR = " \u2551"

# Escape character sequences for different colours - see https://pypi.python.org/pypi/colorama
BLUE_TEXT = "\033[34;1m"
RED_TEXT = "\033[31;1m"
RESET_TEXT = "\033[0m"

# Create empty global board dictionary, used to store the values of all cells in the board
board = {}
score = 0

# Formatting procedures
def clearScreen():
    print("\n" * 20)

def setRedText():
    print(RED_TEXT, end="")

def resetText():
    print(RESET_TEXT,end="")

def setBlueText():
    print(BLUE_TEXT, end="")

# Gameplay functions/procedures

def initialiseBoard():

    global board

    blankRow = []

    for row in range(0, BOARDSIZE):
        blankRow.append(0)

    for col in range(0, BOARDSIZE):
        board[chr(ASCII_A+col)] = list(blankRow)


def placeBombs(numBombs):
    # This procedure will randomly place bombs around the board.
    # The numBombs parameter allows us to state how many bombs we want when we call the procedure.
    # A while loop is used to repeat the process of randomly choosing a column and row for as many bombs as are required.
    global board
    placedBombs = 0
    while placedBombs < numBombs:
        randCol = ASCII_A + random.randint(0,BOARDSIZE-1) # This line selects a random number between 0 and the size of the board (usually 10) and adds it to the ASCII/Unicode value of the 'A' character. This means that we can generate a random letter for the column by starting with A and increasing by between 0 and 10 letters.
        randRow = random.randint(0, BOARDSIZE-1)
        if board[chr(randCol)][randRow] != BOMB_UNCHECKED: # Here we check that we haven't already randomly selectled this location to place a bomb.
            board[chr(randCol)][randRow] = BOMB_UNCHECKED # If the randomly chosen location hasn't been marked as containing a bomb, then set it as having a bomb
            placedBombs += 1


# Graphics procedures

def showIntro():
    clearScreen()
    setBlueText()
    print("BBB    BBB   BB BB  BBB    BB    BBB  BBB  BBB    BB".replace("B", BLOCK_CHAR)) # B characters are replaced with a solid block (unicode 2558)
    print("B  B  B   B  B B B  B  B  B  B  B      B    B    B   B".replace("B", BLOCK_CHAR))
    print("B  B  B   B  B B B  B  B  B  B  B      B    B    B".replace("B", BLOCK_CHAR))
    print("BBB   B   B  B B B  BBB   BBBB   BB    B    B    B".replace("B", BLOCK_CHAR))
    print("B  B  B   B  B   B  B  B  B  B     B   B    B    B".replace("B", BLOCK_CHAR))
    print("B  B  B   B  B   B  B  B  B  B     B   B    B    B   B".replace("B", BLOCK_CHAR))
    print("BBB    BBB   B   B  BBB   B  B  BBB    B   BBB    BB".replace("B", BLOCK_CHAR))
    resetText()
    print("\n(C) Copyright 2016 Shiplake Games Ltd.\n")
    input("Press Enter to continue...")

def showBoard():
    global board

    clearScreen()

    # print column headings
    print(" " * LEFT_MARGIN ,end="")
    for col in range(0,BOARDSIZE):
        print(chr(ASCII_A+col).center(CELL_SIZE+1," "), end="")
    print("\n" + "=" * LEFT_MARGIN,end="")
    print("=" * BOARDSIZE * (CELL_SIZE+1))

    for row in range(0, BOARDSIZE):
        print (str(row+1).rjust(LEFT_MARGIN-2," ") + DBLWALL_CHAR ,end="")
        for col in range(0,BOARDSIZE):
            symbol = ""
            if board[chr(ASCII_A + col)][row]==CLEAR_UNCHECKED:
                symbol = " "
            elif board[chr(ASCII_A + col)][row]==BOMB_UNCHECKED:
                #setRedText()
                symbol = "!"
            elif board[chr(ASCII_A + col)][row]==CLEAR_CHECKED:
                symbol = "*"
            elif board[chr(ASCII_A + col)][row]==BOMB_CHECKED:
                symbol = "X"
            #resetText()
            print(symbol.center(CELL_SIZE," "),end="|")

        print("")
        print("-" * (LEFT_MARGIN + (BOARDSIZE * (CELL_SIZE+1))))



showIntro()
initialiseBoard()
placeBombs(NUM_BOMBS)
showBoard()
