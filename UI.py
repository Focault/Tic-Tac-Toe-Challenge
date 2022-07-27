import shutil


def hello():
    width = shutil.get_terminal_size((80, 20))[0]
    print("", "*** Welcome! This Tic Tac Toe Bot Has One Flaw in it's Strategy! ***".center(width), sep="\n")
    print("", "Only One Strategy Executed in One of 3 Ways Can Beet Him!".center(width), sep="\n")
    print("", "Do You Think You Can?".center(width), sep="\n")


def create_board(_row_s):
    board = [[' ' for i in range(_row_s)] for x in range(_row_s)]
    return board


def print_board(_board):
    width = shutil.get_terminal_size((80, 20))[0]
    n = len(_board)
    line_format = ""
    indexes = [str(x) for x in range(1, n+1)]
    for x in range(n):
        if not x:
            line_format += "{0}  {" + str(x+1) + ":^5}" + "{" + str(n+1) + "}"
        elif x != (n-1):
            line_format += "{" + str(x+1) + ":^5}" + "{" + str(n+1) + "}"
        else:
            line_format += "{" + str(x+1) + ":^5}"
    print("\n")
    print(line_format.format(" ", *indexes, "**").center(width))
    for x in range(n):
        print(line_format.format(str(x+1), *(_board[x]), "||").center(width))
        if x != (n-1):
            print(("*  " + ("=" * (n * 5 + (n - 1) * 2))).center(width))


def ask_input(_board, _shape, _row_s):
    while True:
        ver = input("\nPlease Insert Vertical Index: ")
        hor = input("Please Insert Horizontal Index: ")
        if ver.isnumeric() and hor.isnumeric() and 0 < int(ver) <= _row_s and 0 < int(hor) <= _row_s:
            ver, hor = int(ver) - 1, int(hor) - 1
            if _board[ver][hor] == ' ':
                break
            else:
                print("Spot Taken I'm Afraid...")
        else:
            print("Wrong! Try Again!")
    _board[ver][hor] = _shape


def play_again():
    while True:
        resume = input("\nPlay Again? (y/n) - ").lower()
        if resume == 'y':
            return True
        if resume == 'n':
            return False
        print("Wrong Input.")


def print_result(_who_won, _shape_dict, _board):
    width = (shutil.get_terminal_size((80, 20))[0])
    if _who_won != 'O' and _who_won != 'X':
        print("", _who_won.center(width), sep="\n")
    else:
        if _shape_dict[_who_won] == "Player":
            print_board(_board)
            print("", "Congratulations! You've Found The Algorithm's Blind Spot!".center(width),
                  "Did You Peaked in the Code?".center(width), sep="\n")
        else:
            print("", "The Bot Have Won! You Have Really Messed Up...".center(width),
                  "That's like... Never Happens...".center(width), sep="\n")
