from random import choice
from Strategy import pick_spot
from UI import *


def randomizer():
    shape = choice(range(0, 2))
    who_starts_determine = choice(range(0, 2))
    bot, player = "X", "O"
    if shape == 1:
        bot, player = player, bot
    return bot, player, who_starts_determine


def is_row_won(_board, _n):
    for x in range(_n):
        if _n == _board[x].count('X'):
            return _board[x][0]
        if _n == _board[x].count('O'):
            return _board[x][0]
    return False


def is_column_won(_board, _n):
    for y in range(_n):
        count_x, count_o = 0, 0
        for x in range(_n):
            if 'X' == _board[x][y]:
                count_x += 1
            if 'O' == _board[x][y]:
                count_o += 1
            if (count_x and count_o) or _board[x][y] == ' ':
                break
        else:
            return _board[0][y]
    return False


def is_across_won(_board, _n):
    across = [range(_n), range(_n)[::-1]]
    for y in across:
        count_x, count_o = 0, 0
        for idx, x in enumerate(y):
            if 'X' == _board[idx][x]:
                count_x += 1
            if 'O' == _board[idx][x]:
                count_o += 1
            if (count_x and count_o) or _board[idx][x] == ' ':
                break
        if count_x == _n or count_o == _n:
            return _board[_n // 2][_n // 2]
    return False


def is_tie(_board, _row_s):
    for x in range(_row_s):
        if ' ' in _board[x]:
            return False
    return "It's a Tie!"


def is_game_over(_board, _row_s):
    row = is_row_won(_board, _row_s)
    if row:
        return row
    column = is_column_won(_board, _row_s)
    if column:
        return column
    across = is_across_won(_board, _row_s)
    if across:
        return across
    return is_tie(_board, _row_s)


def initialize_game(_row_s):
    board = create_board(_row_s)
    bot_shape, player_shape, who_starts = randomizer()
    if who_starts:
        print_board(board)
    first_turn, second_turn = (pick_spot, bot_shape), (ask_input, player_shape)
    shape_dict = {bot_shape: "Bot", player_shape: "Player"}
    if who_starts:
        first_turn, second_turn = second_turn, first_turn
    game_components = (board, shape_dict, first_turn, second_turn, _row_s)
    return game_components


def run_game(_game_components):
    who_won = False
    board, shape_dict, first_turn, second_turn, row_s = _game_components
    while not who_won:
        first_turn[0](board, first_turn[1], row_s)
        who_won = is_game_over(board, row_s)
        if not who_won:
            second_turn[0](board, second_turn[1], row_s)
            who_won = is_game_over(board, row_s)
    print_result(who_won, shape_dict, board)
    return play_again()
