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


def traverse(data):
    tree_map = []
    for i, line in enumerate(data[:-1].split('\n')):
        tree_map.append([])
        for j, point in enumerate(line):
            tree_map[i].append(point)

    path = []
    y, x = 1, 3
    while y < len(tree_map):
        path.append(tree_map[y][x])
        y += 1
        x = (x + 3) % len(tree_map[0])

    print(path)
    return len([x for x in path if x == '#'])


assert traverse(test_data) == 7

with open('d3.txt') as f:
    print(traverse(f.read()))
