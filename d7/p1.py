import networkx as nx


test_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


G = nx.DiGraph()


def resolve_rule(line: str):
    neighbors = []
    base_bag_name, inner_bag_names = line.split(' contain ')
    base_bag_name = base_bag_name.replace(' bags', '')
    if inner_bag_names == 'no other bags.':
        return None
    for n_and_type in inner_bag_names.split(', '):
        splits = n_and_type.split(' ')
        n_bags = int(splits[0])
        bagname = ' '.join(splits[1:3])
        neighbors.append((base_bag_name, bagname, n_bags))
    return neighbors


def resolve_input(data):
    rules = []
    for line in data.split('\n'):
        if rule := resolve_rule(line):
            rules.extend(rule)
    G.add_weighted_edges_from(rules)


def count_combos(input, orig_bag):
    resolve_input(input)
    n_bags = 0
    sp = dict(nx.all_pairs_shortest_path(G))
    for start, targets in sp.items():
        if orig_bag in targets:
            n_bags += 1
    return n_bags - 1


assert count_combos(test_data, 'shiny gold') == 4


G.clear()

with open('d7.txt') as f:
    # 102 was too low
    # 561 was too high
    print(count_combos(f.read(), 'shiny gold'))
