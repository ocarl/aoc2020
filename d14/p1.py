test_data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""


def combine(data):
    mask = ''
    memory = {}
    for line in data.split('\n'):
        if 'mask' in line:
            mask = line[7:][::-1]
        elif 'mem' in line:
            mem_val = line.split('] = ')
            value = int(mem_val[1])
            mem = int(mem_val[0].split('[')[1])
            bin_val = bin(value)[2:][::-1]
            bin_val_iter = iter(bin_val)
            result = ''
            for i in range(len(mask)):
                if i < len(bin_val):
                    next_char = next(bin_val_iter)
                    result += next_char if mask[i] == 'X' else mask[i]
                else:
                    result += '0' if mask[i] == 'X' else mask[i]
            memory[mem] = result
    return sum(int(v[::-1], 2) for v in memory.values())


assert combine(test_data) == 165

print('###')

with open('d14.txt') as f:
    print(combine(f.read()))
