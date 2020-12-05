def partitionate(max_i, min_i, guide):
    for div in guide:
        diff = max_i - min_i
        if div:
            min_i = min_i
            max_i = min_i + diff // 2
        else:
            min_i = max_i - diff // 2
            max_i = max_i
    if max_i != min_i:
        print(guide)
        print(min_i)
        print(max_i)
        raise Exception
    return max_i


def str_to_bool(input):
    return True if input in ('F', 'L') else False


def translate_to_row_seat(in_str: str):
    row = partitionate(127, 0, map(str_to_bool, in_str[:7]))
    seat = partitionate(7, 0, map(str_to_bool, in_str[7:]))
    return row, seat


def calc_id(row, col):
    return row*8+col


assert translate_to_row_seat('FBFBBFFRLR') == (44, 5)
assert translate_to_row_seat('BFFFBBFRRR') == (70, 7)
assert calc_id(70, 7) == 567
assert translate_to_row_seat('FFFBBBFRRR') == (14, 7)
assert translate_to_row_seat('BBFFBBFRLL') == (102, 4)

with open('d5.txt') as f:
    seats = []
    for line in f.readlines():
        seats.append(translate_to_row_seat(line))
    seats.sort(key=lambda x: (x[0], x[1]))
    seats = seats[3:-4]
    prev_id = 0
    next_id = 0
    for i, seat in enumerate(seats):
        if i == 0:
            continue
        curr_id = calc_id(*seat)
        prev_id = calc_id(*seats[i-1])
        if curr_id - prev_id == 2:
            print(curr_id - 1)
