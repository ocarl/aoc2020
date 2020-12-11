test_data="""abc

a
b
c

ab
ac

a
a
a
a

b

"""

def count(input):
    groups = []
    for group in input.split('\n\n'):
        group_set = set(group) - {'\n'}
        groups.append(group_set)
    counts = [len(x) for x in groups]
    return sum(counts)

assert count(test_data) == 11

with open('d6.txt') as f:
    print(count(f.read()))
