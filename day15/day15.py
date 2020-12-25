INPUT_PATH = "./input.txt"


def load():
    with open(INPUT_PATH) as f:
        content = f.readline().strip()

    return [int(e) for e in content.split(',')]


def find_number(pos):
    numbers_spoken = load()

    stats = {}
    last_spoken = None
    turn = 1
    for spoken in numbers_spoken:
        stats[spoken] = [turn]
        last_spoken = spoken
        turn += 1

    while True:
        spoken_stats = stats.get(last_spoken)
        if len(spoken_stats) == 1:
            last_spoken = 0
        else:
            last_spoken = spoken_stats[-1] - spoken_stats[-2]

        if last_spoken not in stats:
            stats[last_spoken] = [turn]
        else:
            stats[last_spoken].append(turn)

        if turn == pos:
            print(f'{turn}, spoken: {last_spoken}')
            break
        turn += 1


def part_1():
    find_number(2020)


def part_2():
    find_number(30000000)


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
