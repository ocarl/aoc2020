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
    """
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not."""
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
        if {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}.issubset(set(passport.keys())):
            valids.append(passport)
    real_valids = []
    fake_valids = []
    for valid in valids:
        byr = len(valid['byr']) == 4
        byr = byr and 1920 <= int(valid['byr']) <= 2002
        iyr = len(valid['iyr']) == 4
        iyr = iyr and 2010 <= int(valid['iyr']) <= 2020
        eyr = len(valid['eyr']) == 4
        eyr = eyr and 2020 <= int(valid['eyr']) <= 2030
        if valid['hgt'].find('cm') > 0:
            hgt = 150 <= int(valid['hgt'].split('cm')[0]) <= 193
        elif valid['hgt'].find('in') > 0:
            hgt = 59 <= int(valid['hgt'].split('in')[0]) <= 76
        else:
            hgt = False
        hcl = len(valid['hcl']) == 7 and all([x in {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'} for x in valid['hcl'][1:]])
        ecl = valid['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        pid = len(valid['pid']) == 9
        if all([byr, iyr, eyr, hgt, hcl, ecl, pid]):
            real_valids.append(valid)
        else:
            fake_valids.append(valid)

    print(real_valids)
    return len(real_valids)

invalid_data = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

valid_data = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

#assert validate(invalid_data) == 0
#assert validate(valid_data) == 4

with open('d4.txt') as f:
    print(validate(f.read()))