from collections import defaultdict
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
    counts = []
    for group in input.split('\n\n'):
        group_list = []
        for person in group.split('\n'):
            person_set = set(person)
            group_list.append(person_set)
        group_len = len(set.intersection(*group_list))
        counts.append(group_len)
    return sum(counts)

assert count(test_data) == 6

with open('d6.txt') as f:
    print(count(f.read()))
