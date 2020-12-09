import collections

INPUT_PATH = "./input.txt"


def validate_pwd_occ(min, max, char, sequence):
    counter = collections.Counter(sequence)

    found = counter.get(char, None)
    if not found:
        return False

    return min <= found <= max


def validate_pwd_pos(i, j, char, sequence):
    try:
        found_i = sequence[i] == char
    except:
        found_i = False

    try:
        found_j = sequence[j] == char
    except:
        found_j = False

    if found_i and not found_j:
        return True
    elif found_j and not found_i:
        return True
    else:
        return False


def part_1():
    bad_pwds = []
    good_pwds = []
    with open(INPUT_PATH) as f:
        for line in f:
            stripped = line.split(":")
            pattern = stripped[0].split(" ")
            min = int(pattern[0].split("-")[0].strip())
            max = int(pattern[0].split("-")[1].strip())
            char = pattern[1].strip()

            sequence = stripped[1].strip()
            if validate_pwd_occ(min, max, char, sequence):
                good_pwds.append(line)
            else:
                bad_pwds.append(line)

    print(f"good {len(good_pwds)}, bad {len(bad_pwds)}")


def part_2():
    bad_pwds = []
    good_pwds = []
    with open(INPUT_PATH) as f:
        for line in f:
            stripped = line.split(":")
            pattern = stripped[0].split(" ")
            pos_i = int(pattern[0].split("-")[0].strip()) - 1
            pos_j = int(pattern[0].split("-")[1].strip()) - 1
            char = pattern[1].strip()

            sequence = stripped[1].strip()
            if validate_pwd_pos(pos_i, pos_j, char, sequence):
                good_pwds.append(line)
            else:
                bad_pwds.append(line)

    print(f"good {len(good_pwds)}, bad {len(bad_pwds)}")


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
