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

        self.instruction_map = {
            'acc': self.index_add,
            'jmp': self.jump,
            'nop': self.noop
        }

        self.visited = {}

    def index_add(self, x):
        self.acc += x
        self.line_index += 1

    def jump(self, x):
        self.line_index += x

    def noop(self, x):
        self.line_index += 1

    def execute_instruction(self, instr, x):
        if instr+str(self.line_index) in self.visited.keys():
            return self.acc
        self.visited[instr+str(self.line_index)] = self.acc
        self.instruction_map[instr](x)
        return None

    def run(self, data):
        instructions = []
        for line in data.split('\n'):
            instructions.append(line)
        while True:
            line = instructions[self.line_index]
            instr, x = line.split(' ')
            x = x.replace('+', '')
            res = self.execute_instruction(instr, int(x))
            if res:
                return res

def solve(data):
    cpu = Computer()
    return cpu.run(data)




assert solve(test_data) == 5


with open('d8.txt') as f:
    print(solve(f.read()))

