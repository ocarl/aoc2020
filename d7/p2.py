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
        for _ in range(n_bags - 1):
            neighbors.append((base_bag_name, bagname, 1))
    return neighbors


def resolve_input(data):
    rules = []
    for line in data.split('\n'):
        if rule := resolve_rule(line):
            rules.extend(rule)
    G.add_weighted_edges_from(rules)


def add_bags(G, bag, acc):
    if not nx.descendants(G, bag):
        return acc
    for des in nx.descendants(G, bag):
        dl = list(des)
        acc += int(dl[2])
        add_bags(G, dl[0])


def count_combos(input, orig_bag):
    resolve_input(input)
    acc = add_bags(G, orig_bag, 0)
    return acc


assert count_combos(test_data, 'shiny gold') == 32


G.clear()
H.clear()

test_data = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


assert count_combos(test_data, 'shiny gold') == 126

G.clear()


with open('d7.txt') as f:
    # 102 was too low
    # 247 was too low
    # 561 was too high
    print(count_combos(f.read(), 'shiny gold'))
