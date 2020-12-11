test_data="""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


class Computer:
    def __init__(self):
        self.acc = 0
        self.line_index = 0
        self.replace_index = 0
        self.replace_total = 0

        self.visited = []
        self.finished = False

        self.instruction_map = {
            'acc': self.index_add,
            'jmp': self.jump,
            'nop': self.noop
        }
        self.data = ''
        self.instructions = []

    def index_add(self, x):
        self.acc += x
        self.line_index += 1

    def jump(self, x):
        self.line_index += x

    def noop(self, x):
        self.line_index += 1

    def fix(self):
        n_hits = 0
        for i, instr in enumerate(self.instructions):
            if 'jmp' in instr:
                n_hits += 1
            if 'nop' in instr:
                n_hits += 1
            if n_hits > self.replace_total:
                self.replace_total += 1
                self.replace_index = i
                break

        self.line_index = 0
        self.acc = 0
        self.visited = []
        self.instructions = []
        self.load(self.data)
        if 'jmp' in self.instructions[self.replace_index]:
            self.instructions[self.replace_index] = self.instructions[self.replace_index].replace('jmp', 'nop')
        elif 'nop' in self.instructions[self.replace_index]:
            self.instructions[self.replace_index] = self.instructions[self.replace_index].replace('nop', 'jmp')

    def execute_instruction(self, instr, x):
        if instr+str(self.line_index) in self.visited:
            self.fix()
            return 'error'
        self.visited.append(instr+str(self.line_index))
        self.instruction_map[instr](x)

    def load(self, data):
        self.data = data
        for line in data.split('\n'):
            self.instructions.append(line)

    def run(self):
        for _ in range(len(self.instructions)):
            if self.line_index == len(self.instructions):
                self.finished = True
                break
            line = self.instructions[self.line_index]
            instr, x = line.split(' ')
            x = x.replace('+', '')
            res = self.execute_instruction(instr, int(x))
            if res == 'error':
                break
        return self.acc


def solve(data):
    cpu = Computer()
    cpu.load(data)
    while not cpu.finished:
        res = cpu.run()
    return res


assert solve(test_data) == 8

print('###')

with open('d8.txt') as f:
    # 1782 too high
    print(solve(f.read()))

