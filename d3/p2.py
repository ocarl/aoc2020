import math
test_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


def traverse(data, dx, dy):
    tree_map = []
    for i, line in enumerate(data[:-1].split('\n')):
        tree_map.append([])
        for j, point in enumerate(line):
            tree_map[i].append(point)

    path = []
    y, x = dy, dx
    while y < len(tree_map):
        path.append(tree_map[y][x])
        y += dy
        x = (x + dx) % len(tree_map[0])

    print(path)
    return len([x for x in path if x == '#'])


assert traverse(test_data, 3, 1) == 7


def traverse_dirs(data):
    res = []
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        res.append(traverse(data, dx, dy))
    return math.prod(res)


assert traverse_dirs(test_data) == 336

with open('d3.txt') as f:
    print(traverse_dirs(f.read()))
