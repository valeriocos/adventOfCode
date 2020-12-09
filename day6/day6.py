import collections

INPUT_PATH = "./input.txt"


def get_groups():
    groups = []

    group = []
    with open(INPUT_PATH, 'r') as f:
        for line in f:
            content = line.strip()
            if not content:
                groups.append(group)
                group = []
            else:
                group.append(content)

    if group:
        groups.append(group)

    return groups


def part_1():
    groups = get_groups()
    total_answers = 0
    for g in groups:
        flatten_g = ''.join(g)
        num_answers = len(list(set(flatten_g)))
        total_answers = total_answers + num_answers

    print(f"total answers: {total_answers}")


def part_2():
    groups = get_groups()
    all_common_answers = []
    for g in groups:
        num_respondents = len(g)
        answers = ''.join(g)
        stats_answers = collections.Counter(answers)
        common_answers = []
        for a in stats_answers:
            if stats_answers.get(a) == num_respondents:
                common_answers.append(a)
        all_common_answers.append(common_answers)

    total_common_answers = 0
    for a in all_common_answers:
        total_common_answers += len(a)

    print(f"Total common answers: {total_common_answers}")


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
