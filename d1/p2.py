test_data = """1721
979
366
299
675
1456
"""

def do_calc(data):
    numbers = [int(x) for x in data.split('\n')[:-1]]
    for num1 in numbers:
        for num2 in [x for x in numbers]:
            for num3 in [x for x in numbers]:
                if num1+num2+num3 == 2020:
                    return num1*num2*num3
    return None

assert do_calc(test_data) == 241861950

with open('d1.txt') as f:
    print(do_calc(f.read()))

