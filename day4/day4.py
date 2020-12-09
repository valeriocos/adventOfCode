import re

INPUT_PATH = "./input.txt"

MANDATORY_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
OPTIONAL_FIELDS = ["cid"]


def load_passport(passport_data):
    passport = {}
    for attr in passport_data:
        kv = attr.split(":")
        k = kv[0].strip()
        v = kv[1].strip()

        passport[k] = v

    return passport


def load_passports():
    passports = []
    passport_data = []
    with open(INPUT_PATH, 'r') as f:
        for line in f:
            content = line.strip()
            if not content:
                passports.append(load_passport(passport_data))
                passport_data = []
                continue

            passport_data.extend(content.split(" "))

    if passport_data:
        passports.append(load_passport(passport_data))

    return passports


def check_range(value, min_v, max_v):
    return min_v <= value <= max_v


def check_pattern(pattern, value):
    return re.match(pattern, value) is not None


def valid_passport(passport, check_attrs=False):
    valid = True
    for field in MANDATORY_FIELDS:
        if field not in passport.keys():
            return False

    if check_attrs:
        byr = int(passport.get("byr"))
        byr_valid = check_range(byr, 1920, 2002)

        iyr = int(passport.get("iyr"))
        iyr_valid = check_range(iyr, 2010, 2020)

        eyr = int(passport.get("eyr"))
        eyr_valid = check_range(eyr, 2020, 2030)

        hgt = passport.get("hgt")
        if not hgt.endswith("cm") and not hgt.endswith("in"):
            hgt_valid = False
        else:
            hgt_value = int(hgt[:-2])
            hgt_dim = hgt[-2:]
            if hgt_dim == "cm":
                hgt_valid = check_range(hgt_value, 150, 193)
            elif hgt_dim == "in":
                hgt_valid = check_range(hgt_value, 59, 76)
            else:
                hgt_valid = False

        hcl = passport.get("hcl")
        if not hcl.startswith("#"):
            hcl_valid = False
        else:
            hcl_stripped = hcl[1:]
            hcl_valid = check_pattern("^[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$", hcl_stripped)

        ecl = passport.get("ecl")
        ecl_valid = ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        pid = passport.get("pid")
        pid_valid = check_pattern("^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$", pid)

        valid = byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid

    return valid


def part_1():
    good_passports = []
    bad_passports = []
    passports = load_passports()
    for passport in passports:
        if valid_passport(passport):
            good_passports.append(passport)
        else:
            bad_passports.append(passport)

    print(f"{len(good_passports)} valid passports")


def part_2():
    good_passports = []
    bad_passports = []
    passports = load_passports()
    for passport in passports:
        if valid_passport(passport, check_attrs=True):
            good_passports.append(passport)
        else:
            bad_passports.append(passport)

    print(f"{len(good_passports)} valid passports")


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
