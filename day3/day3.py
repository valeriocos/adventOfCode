import collections

INPUT_PATH = "./input.txt"


def calculate_trees_shift_down_2(right_shift):
    path = []
    with open(INPUT_PATH) as f:
        num_line = 1
        pos = 0
        for line in f:
            content = line.strip()
            if num_line == 1:
                num_line += 1
                continue

            if num_line % 2 == 0:
                num_line += 1
                continue

            pos = (pos + right_shift) % len(content)
            path.append([num_line, pos, content[pos]])
            num_line += 1

    num_trees = 0
    for p in path:
        if p[2] == '#':
            num_trees += 1

    return num_trees


def calculate_trees(right_shift):
    path = []
    with open(INPUT_PATH) as f:
        num_line = 1
        pos = 0
        for line in f:
            content = line.strip()
            if num_line == 1:
                num_line += 1
                continue

            pos = (pos + right_shift) % len(content)
            path.append([num_line, pos, content[pos]])
            num_line += 1

    num_trees = 0
    for p in path:
        if p[2] == '#':
            num_trees += 1

    return num_trees


def part_1():
    num_trees = calculate_trees(3)
    print(f"{num_trees} trees found")


def part_2():
    right_shifts = [1, 3, 5, 7]
    all_num_trees = []
    for shift in right_shifts:
        num_trees = calculate_trees(shift)
        all_num_trees.append(num_trees)

    all_num_trees.append(calculate_trees_shift_down_2(1))

    total = 1
    for num in all_num_trees:
        total *= num

    print(f"total {total}")


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
