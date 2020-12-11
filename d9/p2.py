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


def find_set(num, numbers):
    for i in range(len(numbers)):
        n = i
        num_set = numbers[i:n]
        set_sum = sum(num_set)
        while num >= set_sum:
            if num == set_sum:
                return num_set
            n += 1
            num_set = numbers[i:n]
            set_sum = sum(num_set)
    return None


def find_two(prev_nums, sum):
    for i in prev_nums:
        for j in prev_nums:
            if i+j == sum:
                return i,j
    return None


def solve(data, preamble_len):
    numbers = []
    shitty = 0
    for line in data.split('\n'):
        numbers.append(int(line))
    for i, num in enumerate(numbers):
        if i < preamble_len + 1:
            continue
        if not find_two(numbers[i-preamble_len:i], num):
            shitty = num
    num_set_sorted = sorted(find_set(shitty, numbers))
    return num_set_sorted[0] + num_set_sorted[-1]


assert solve(test_data, 5) == 62

print('###')

with open('d9.txt') as f:
    # 130080137 too low
    # 178080586 too high
    print(solve(f.read(), 25))