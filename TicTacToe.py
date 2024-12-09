import random

# ANSI escape codes for colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

print("Welcome To Tic Tac Toe \nWelcome To XoXo ^ - ^")
print("=========================")

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3],[4,5,6],[7,8,9]]
rows = 3
cols = 3

def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            cell = gameBoard[x][y]
            if cell == 'X':
                print(f" {GREEN}{cell}{RESET}", end=" |")
            elif cell == 'O':
                print(f" {YELLOW}{cell}{RESET}", end=" |")
            else:
                print(f" {cell}", end=" |")
    print("\n+---+---+---+")

def modifyArray(num, turn):
    num -= 1
    if num == 0:
        gameBoard[0][0] = turn
    elif num == 1:
        gameBoard[0][1] = turn
    elif num == 2:
        gameBoard[0][2] = turn
    elif num == 3:
        gameBoard[1][0] = turn
    elif num == 4:
        gameBoard[1][1] = turn
    elif num == 5:
        gameBoard[1][2] = turn
    elif num == 6:
        gameBoard[2][0] = turn
    elif num == 7:
        gameBoard[2][1] = turn
    elif num == 8:
        gameBoard[2][2] = turn

def CheckWinner(gameBoard):
    # Check rows
    for row in gameBoard:
        if row[0] == row[1] == row[2]:
            print(f"{row[0]} has won!")
            return row[0]
    # Check columns
    for col in range(3):
        if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col]:
            print(f"{gameBoard[0][col]} has won!")
            return gameBoard[0][col]
    # Check diagonals
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]:
        print(f"{gameBoard[0][0]} has won!")
        return gameBoard[0][0]
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0]:
        print(f"{gameBoard[0][2]} has won!")
        return gameBoard[0][2]
    return "L"

def playerTurn(turn):
    printGameBoard()
    numberPicked = input(f"\n{turn}'s turn. Choose a number [1-9] or 'q' to quit: ")
    if numberPicked.lower() == 'q':
        print("\nGame over! Thank you for playing :)")
        exit()
    numberPicked = int(numberPicked)
    if 1 <= numberPicked <= 9:
        modifyArray(numberPicked, turn)
        possibleNumbers.remove(numberPicked)
    else:
        print("Invalid input. Please try again.")
        playerTurn(turn)

def cpuTurn():
    while True:
        cpuChoice = random.choice(possibleNumbers)
        print("\nCpu choice: ", cpuChoice)
        if cpuChoice in possibleNumbers:
            modifyArray(cpuChoice, 'O')
            possibleNumbers.remove(cpuChoice)
            break

def main():
    mode = input("Choose mode: \n1 for Player vs Player, \n2 for Player vs Computer: ")
    leaveLoop = False
    turnCounter = 0

    while not leaveLoop:
        if turnCounter % 2 == 0:
            playerTurn('X')
        else:
            if mode == '1':
                playerTurn('O')
            elif mode == '2':
                cpuTurn()
        turnCounter += 1

        winner = CheckWinner(gameBoard)
        if winner != "L":
            printGameBoard()
            print("\nGame over! Thank you for playing :)")
            break

if __name__ == "__main__":
    main()
