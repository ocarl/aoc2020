test_data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


class Solver:
    def __init__(self):
        self.old_map = {}
        self.new_map = {}
        self.occupied_seats = 0
        self.max_col = 0
        self.max_row = 0

    def look(self, i, j, direction):
        direction_map = {
            'N': (-1, 0),
            'S': (1, 0),
            'E': (0, 1),
            'W': (0, -1),
            'NE': (-1, 1),
            'SW': (1, -1),
            'SE': (1, 1),
            'NW': (-1, -1),
        }
        pos = i + direction_map[direction][0], j + direction_map[direction][1]
        if pos[0] < 0 or pos[0] > self.max_row or pos[1] < 0 or pos[1] > self.max_col:
            return 'L'
        if self.old_map[pos] == '#':
            return '#'
        if self.old_map[pos] == '.':
            return self.look(pos[0], pos[1], direction)

    def resolve_seat(self, i, j):
        surrounding_seats = [
            self.look(i, j, 'N'),
            self.look(i, j, 'S'),
            self.look(i, j, 'E'),
            self.look(i, j, 'W'),
            self.look(i, j, 'NE'),
            self.look(i, j, 'NW'),
            self.look(i, j, 'SE'),
            self.look(i, j, 'SW'),
        ]
        n_taken = len([x for x in surrounding_seats if x == '#'])
        if self.old_map[(i, j)] == 'L' and n_taken == 0:
            self.new_map[(i, j)] = '#'
            self.occupied_seats = self.occupied_seats + 1
        elif self.old_map[(i, j)] == '#' and n_taken >= 5:
            self.new_map[(i, j)] = 'L'
            self.occupied_seats = self.occupied_seats - 1
        else:
            self.new_map[(i, j)] = self.old_map[(i, j)]

    def show_seats(self):
        for i in range(self.max_row + 1):
            row = []
            for j in range(self.max_col + 1):
                row.append(self.new_map[(i, j)])
            print(''.join(row))
        print('\n')
        print('\n')

    def solve(self, data):
        for i, row in enumerate(data.split('\n')):
            for j, col in enumerate(row):
                self.old_map[(i, j)] = col
                self.max_col = j
                self.max_row = i
        while True:
            prev_occ = self.occupied_seats
            for i in range(self.max_row + 1):
                for j in range(self.max_col + 1):
                    self.resolve_seat(i, j)
            #self.show_seats()
            if prev_occ == self.occupied_seats:
                break
            self.old_map.clear()
            self.old_map = {k: v for k, v in self.new_map.items()}
        return self.occupied_seats


s1 = Solver()
assert s1.solve(test_data) == 26

print('####')

s2 = Solver()
with open('d11.txt') as f:
    print(s2.solve(f.read()))
