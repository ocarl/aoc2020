test_data = "0,3,6"


from collections import defaultdict


def game(data):
    firsts = defaultdict(list)
    turns = {}
    turn = 1
    for num in data.split(','):
        firsts[int(num)].append(turn)
        turns[turn] = int(num)
        turn += 1
    mrsn = list(firsts.keys())[-1]
    while turn <= 30000000:
        if turns[turn-1] == mrsn and len(firsts.get(mrsn)) == 1:
            mrsn = 0
        elif mrsn in firsts.keys() and len(firsts[mrsn]) > 1:
            next_latest = firsts[mrsn][-2]
            latest = firsts[mrsn][-1]
            mrsn = latest - next_latest
        turns[turn] = mrsn
        firsts[mrsn].append(turn)
        turn += 1
    return mrsn


assert game(test_data) == 175594


data = "11,18,0,20,1,7,16"
print(game(data))
