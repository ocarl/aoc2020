import networkx as nx


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
    G = nx.DiGraph()
    adapters = [0]
    for line in data.split('\n'):
        adapters.append(int(line))
    adapters = sorted(adapters)
    goal = max(adapters) + 3
    adapters.append(goal)
    nbunch = []
    for i, adapter in enumerate(adapters):
        if i == 0:
            continue
        else:
            k = i
            diff = adapters[k] - adapters[i-1]
            while diff < 4:
                adapters[k] = adapters[k] + diff * 10000
                nbunch.append((adapters[i-1], adapters[k], diff))
                k += 1
                if k == len(adapters):
                    break
                diff = adapters[k] - adapters[i - 1]
    G.add_weighted_edges_from(nbunch)
    all_outs = [x for x in G.nodes if G.out_degree(x) == 0 and G.in_degree(x) == 1]
    return len(all_outs) - 1


solve(test_data1)
solve(test_data2)

assert solve(test_data1) == 8
assert solve(test_data2) == 19208

with open('d10.txt') as f:
    print(solve(f.read()))
