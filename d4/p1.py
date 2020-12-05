test_data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

def validate(data: str):
    passports = []
    for passport in data.split('\n\n'):
        passport = passport.replace('\n', ' ')
        pass_dict = {}
        for field in passport.split(' '):
            try:
                key, val = field.split(':')
            except:
                pass
            pass_dict[key] = val
        passports.append(pass_dict)
    valids = []
    for passport in passports:
        if {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'} == set(passport.keys() - {'cid'}):
            valids.append(passport)
    print(valids)
    return len(valids)

assert validate(test_data) == 2

with open('d4.txt') as f:
    print(validate(f.read()))