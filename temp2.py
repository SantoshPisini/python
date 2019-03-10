# Tic tac toe with random gen

from random import randint as ri

mat = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
p1Name = "A"  # input("Enter player 1 name :\n")
p2Name = "B"  # input("Enter player 2 name :\n")
p1S = 'X'
p2S = 'O'


def place(symbol):
    for i in mat:
        print(i)
    while True:
        r = ri(1, 3)  # int(input("Enter row 1 or 2 or 3 :\n"))
        c = ri(1, 3)  # int(input("Enter column 1 or 2 or 3 :\n"))
        if 0 < r < 4 and 0 < c < 4 and mat[r-1][c-1] == '-':
            mat[r-1][c-1] = symbol
            break
        else:
            print("Invalid input")


def dispwon(s):
    if s == p1S:
        print(p1Name + " Won !!!")
    else:
        print(p2Name + " Won !!!")


def check_r(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if mat[r][c] == symbol:
                count = count + 1
        if count == 3:
            dispwon(symbol)
            return True
    return False


def check_c(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if mat[c][r] == symbol:
                count = count + 1
        if count == 3:
            dispwon(symbol)
            return True
    return False


def check_d(symbol):
    if mat[0][2] == mat[2][0] == mat[1][1] == symbol:
        dispwon(symbol)
        return True
    if mat[2][2] == mat[0][0] == mat[1][1] == symbol:
        dispwon(symbol)
        return True
    return False


def won(symbol):
    return check_r(symbol) or check_c(symbol) or check_d(symbol)


def play():
    for i in range(9):
        if i % 2 == 0:
            print(p1Name+" turn")
            place(p1S)
            if won(p1S):
                break
        else:
            print(p2Name+" turn")
            place(p2S)
            if won(p2S):
                break
    if not(won(p1S)) and not(won(p2S)):
        print("DRAW")


if __name__ == "__main__":
    play()
