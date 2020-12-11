test_data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def find_two(prev_nums, sum):
    for i in prev_nums:
        for j in prev_nums:
            if i+j == sum:
                return i,j
    return None



def solve(data, preamble_len):
    numbers = []
    for line in data.split('\n'):
        numbers.append(int(line))
    for i, num in enumerate(numbers):
        if i < preamble_len + 1:
            continue
        if not find_two(numbers[i-preamble_len:i], num):
            return num


assert solve(test_data, 5) == 127

with open('d9.txt') as f:
    print(solve(f.read(), 25))