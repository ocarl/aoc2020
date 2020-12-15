test_data = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""


def memory_adresser(address, out: list):
    new_address = ''
    for i, c in enumerate(address):
        if c == 'X':
            base_address = new_address
            zero_address = base_address + '0'
            zero_address += address[i+1:]
            memory_adresser(zero_address, out)
            one_address = base_address + '1'
            one_address += address[i+1:]
            memory_adresser(one_address, out)
        else:
            new_address += c
    if len(new_address) == 36:
        out.append(new_address)


def apply_mask(mask, bin_val, orig_val=None):
    orig_val = orig_val or '0'*36
    result = ''
    bin_val_iter = iter(bin_val)
    for i in range(len(mask)):
        if i < len(bin_val):
            next_char = next(bin_val_iter)
            result += next_char if mask[i] == '0' else mask[i]
        else:
            result += orig_val[i] if mask[i] == '0' else mask[i]
    return result


def combine(data):
    mask = ''
    memory = {}
    for line in data.split('\n'):
        if 'mask' in line:
            mask = line[7:][::-1]
        elif 'mem' in line:
            addresses = []
            mem_val = line.split('] = ')
            value = int(mem_val[1])
            address = apply_mask(mask, bin(int(mem_val[0].split('[')[1]))[2:][::-1])
            memory_adresser(address, addresses)
            for mem in addresses:
                memory[int(mem[::-1], 2)] = value
    return sum([v for v in memory.values()])


assert combine(test_data) == 208

print('###')

with open('d14.txt') as f:
    print(combine(f.read()))
