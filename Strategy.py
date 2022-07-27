from UI import print_board

BLOCK_PRIORITY = (10,)
NEXT_BLOCK_PRIORITY = (5,)
LOCATION_PRIORITY = (1, 2)


def scheme_update(_ver, _hor, _scheme, _priority):
    if (_ver, _hor) in _scheme:
        _scheme[(_ver, _hor)] += _priority
    else:
        _scheme[(_ver, _hor)] = _priority


def check_row(_board, _shape, _row_s, _scheme):
    for ver in range(_row_s):
        if (_board[ver].count(_shape) == (_row_s - 1)) and ' ' in _board[ver]:
            hor = _board[ver].index(' ')
            scheme_update(ver, hor, _scheme, BLOCK_PRIORITY[0])


def check_column(_board, _shape, _row_s, _scheme):
    ver_result, hor_result = 0, 0
    for hor in range(_row_s):
        count = 0
        for ver in range(_row_s):
            if _board[ver][hor] == _shape:
                count += 1
                continue
            elif _board[ver][hor] == ' ':
                ver_result, hor_result = ver, hor
            else:
                break
        if count == _row_s - 1 and _board[ver_result][hor_result] == ' ':
            scheme_update(ver_result, hor_result, _scheme, BLOCK_PRIORITY[0])


def check_across(_board, _shape, _row_s, _scheme):
    ver_result, hor_result = 0, 0
    across = [range(_row_s), range(_row_s)[::-1]]
    for direction in across:
        count = 0
        for idx, hor in enumerate(direction):
            if _shape == _board[idx][hor]:
                count += 1
                continue
            elif _board[idx][hor] == ' ':
                ver_result, hor_result = idx, hor
            else:
                break
        if count == _row_s - 1 and _board[ver_result][hor_result] == ' ':
            scheme_update(ver_result, hor_result, _scheme, BLOCK_PRIORITY[0])


def win_game(_board, _shape, _row_s):
    scheme = {}
    check_row(_board, _shape, _row_s, scheme)
    if scheme:
        return scheme
    check_column(_board, _shape, _row_s, scheme)
    if scheme:
        return scheme
    check_across(_board, _shape, _row_s, scheme)
    return scheme


def block_player(_board, _shape, _row_s, _scheme):
    player_shape = 'O' if _shape == 'X' else 'X'
    check_row(_board, player_shape, _row_s, _scheme)
    check_column(_board, player_shape, _row_s, _scheme)
    check_across(_board, player_shape, _row_s, _scheme)


def middle_handler(_board, _row_s, _scheme):
    if _board[_row_s // 2][_row_s // 2] == ' ':
        for x in range(_row_s):
            if _board[x].count(' ') != _row_s:
                scheme_update(_row_s // 2, _row_s // 2, _scheme, LOCATION_PRIORITY[1])
                return True
    return False


def offence(_board, _row_s, _shape, _scheme):
    if not middle_handler(_board, _row_s, _scheme):
        # Upper Left Corner
        if _board[0][0] == ' ':
            scheme_update(0, 0, _scheme, LOCATION_PRIORITY[0])
        elif _board[0][0] == _shape:
            # Bottom Right Corner
            if _board[_row_s - 1][_row_s - 1] == ' ':
                scheme_update(_row_s - 1, _row_s - 1, _scheme, LOCATION_PRIORITY[0])
                return
        # Upper Right Corner
        if _board[0][_row_s - 1] == ' ':
            scheme_update(0, _row_s - 1, _scheme, LOCATION_PRIORITY[0])
        # Bottom Left Corner
        if _board[_row_s - 1][0] == ' ':
            scheme_update(_row_s - 1, 0, _scheme, LOCATION_PRIORITY[0])


def whatever(_board, _row_s):
    for ver in range(_row_s):
        if ' ' in _board[ver]:
            hor = _board[ver].index(' ')
            return ver, hor


def the_missing_piece(_board, _player_shape, _row_s, _scheme):
    if _board[0][0] == _player_shape == _board[_row_s - 1][_row_s // 2]:
        scheme_update(_row_s - 1, 0, _scheme, NEXT_BLOCK_PRIORITY[0])
    if _board[0][_row_s - 1] == _player_shape == _board[_row_s - 1][_row_s // 2] or \
            _board[_row_s - 1][0] == _player_shape == _board[_row_s // 2][_row_s - 1]:
        scheme_update(_row_s - 1, _row_s - 1, _scheme, NEXT_BLOCK_PRIORITY[0])


def defence(_board, _shape, _row_s, _scheme):
    if _board[_row_s // 2][_row_s // 2] == _shape:
        player_shape = 'O' if _shape == 'X' else 'X'
        if _board[0][0] == player_shape == _board[_row_s - 1][_row_s - 1] or \
                _board[0][_row_s - 1] == player_shape == _board[_row_s - 1][0]:
            if _board[_row_s // 2].count(' ') == _row_s - 1:
                scheme_update(_row_s // 2, 0, _scheme, NEXT_BLOCK_PRIORITY[0])
            if _board[0][_row_s // 2] == ' ' and _board[_row_s - 1][_row_s // 2] == ' ':
                scheme_update(0, _row_s // 2, _scheme, NEXT_BLOCK_PRIORITY[0])
        # This Function Completes The Algorithm:
        # else:
            # the_missing_piece(_board, player_shape, _row_s, _scheme)


def pick_spot(_board, _shape, _row_s):
    scheme = win_game(_board, _shape, _row_s)
    if scheme:
        spot = (scheme.popitem())[0]
    else:
        block_player(_board, _shape, _row_s, scheme)
        if not scheme:
            if _row_s == 3:
                defence(_board, _shape, _row_s, scheme)
            if not scheme:
                offence(_board, _row_s, _shape, scheme)
        spot = max(scheme, key=scheme.get) if scheme else whatever(_board, _row_s)
    _board[spot[0]][spot[1]] = _shape
    print_board(_board)
