# Auto Fill in Sudoku Solver
# @author Jacob Schmiedl
import pyautogui as pg
import time

board = []

print('Enter blank spaces as 0')

# input for the solve
while True:
    row = list(input('Row: '))
    ints = []

    for num in row:
        ints.append(int(num))
    board.append(ints)

    if len(board) == 9:
        break
    print('Row ' + str(len(board)) + ' Complete')

# creates lag
time.sleep(3)

# checks if the spot is valid
def valid(x, y, num):
    # checks the row
    for i in range(0, 9):
        if board[i][x] == num and i != y:
            return False

    # checks the column
    for i in range(0, 9):
        if board[y][i] == num and i != x:
            return False

    # checks the 3 by 3 square
    x_board = (x // 3) * 3
    y_board = (y // 3) * 3

    for i in range(x_board, x_board + 3):
        for j in range(y_board, y_board + 3):
            if board[j][i] == num:
                return False
    return True

def output(matrix):
    final = []
    str_final = []
    for i in range(9):
        final.append(matrix[i])
    for lists in final:
        for num in lists:
            str_final.append(str(num))
    counter = []

    for num in str_final:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)

        # move down once at col 9
        if len(counter)%9 == 0:
            pg.hotkey('down')
            for i in range(8):
                pg.hotkey('left')


# solves the puzzle
def solve():
    global board

    # loops through every single num to see if it valid
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if valid(j, i, num):
                        board[i][j] = num
                        solve()
                        # resets if not valid
                        board[i][j] = 0
                return 
    output(board)

solve()

