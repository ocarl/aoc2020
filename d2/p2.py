test_data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


class Validator:

    knowns = {}

    def __init__(self, letter, min_lim, max_lim):
        self.min_lim = min_lim
        self.max_lim = max_lim
        self.letter = letter
        Validator.knowns[letter] = self

    @classmethod
    def create(cls, rule_string):
        vals, letter = rule_string.split(' ')
        min_lim, max_lim = [int(x) for x in vals.split('-')]

        #if validator := cls.knowns.get('letter'):
        #    validator.min_lim = min(min_lim, validator.min_lim)
        #    validator.max_lim = max(max_lim, validator.max_lim)
        #else:
        validator = Validator(letter, min_lim, max_lim)
        return validator

    def check(self, password):
        if len(password) < self.max_lim:
            return False
        letter_at_min = password[self.min_lim - 1]
        letter_at_max = password[self.max_lim - 1]
        min_ok = letter_at_min == self.letter
        max_ok = letter_at_max == self.letter
        return (min_ok or max_ok) and not (min_ok and max_ok)


def password_checker_all(data):
    passwords = []
    valids = []
    for line in data[:-1]:
        rule, password = line.split(': ')
        passwords.append(password)
        Validator.create(rule)
    for password in passwords:
        results = []
        for letter, validator in Validator.knowns.items():
            results.append(validator.check(password))
        if all(results):
            valids.append(password)
    
    return valids


def password_checker(data):
    valids = []
    for line in data[:-1].split('\n'):
        rule, password = line.split(': ')
        validator = Validator.create(rule)
        if validator.check(password):
            valids.append(password)
    return valids


#print(password_checker(test_data))
#assert password_checker(test_data) == ['abcde']

with open('d2.txt') as f:
    print(len(password_checker(f.read())))

