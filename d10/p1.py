test_data1 = """16
10
15
5
1
11
7
19
6
12
4"""

test_data2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

def solve(data):
    adapters = []
    for line in data.split('\n'):
        adapters.append(int(line))
    adapters = sorted(adapters)
    ones = []
    threes = []
    goal = max(adapters) + 3
    curr_jolt = 0
    adapters.append(goal)
    diffs = []
    for i, adapter in enumerate(adapters):
        if i == 0:
            diff = adapter
        else:
            diff = adapter - adapters[i-1]
        if diff == 3:
            threes.append(diff)
        if diff == 1:
            ones.append(diff)
        diffs.append(diff)
    return len(threes)*len(ones)


assert solve(test_data1) == 7*5
assert solve(test_data2) == 22*10

with open('d10.txt') as f:
    print(solve(f.read()))



