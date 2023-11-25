def recursive_game(_p_1, _p_2, tab):
    _player_2 = _p_2
    _player_1 = _p_1

    mem = []
    while len(_player_1) != 0 and len(_player_2) != 0:
        if (_player_1, _player_2) in mem:
            return 1, _player_1
        else:
            mem.append((_player_1.copy(), _player_2.copy()))
        _p1 = _player_1.pop(0)
        _p2 = _player_2.pop(0)
        if len(_player_1) >= _p1 and len(_player_2) >= _p2:
            if recursive_game(_player_1[:_p1].copy(), _player_2[:_p2].copy(), tab + "    ")[0] == 1:
                _player_1 += [_p1, _p2]
            else:
                _player_2 += [_p2, _p1]
        elif _p1 > _p2:
            _player_1 += [_p1, _p2]
        else:
            _player_2 += [_p2, _p1]
    return (1, _player_1) if len(_player_1) > 0 else (2, _player_2)


inp = [line.rstrip() for line in open("input.txt")]
player_1 = [int(x) for x in inp[1:inp.index("")]]
player_2 = [int(x) for x in inp[inp.index("")+2:]]

winner = recursive_game(player_1, player_2, "")[1]

i = 0
res = 0
for w in reversed(winner):
    i += 1
    res += w * i

print(res)
