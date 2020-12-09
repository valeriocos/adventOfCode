INPUT_PATH = "./input.txt"


def part_1():
    numbers = []
    with open(INPUT_PATH) as f:
        for line in f:
            numbers.append(int(line))

    candidates = []

    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                candidates.append((numbers[i], numbers[j]))

    if len(candidates) != 1:
        print("too many results")

    total = candidates[0][0] * candidates[0][1]
    print(f"total {total}")


def part_2():
    numbers = []
    with open(INPUT_PATH) as f:
        for line in f:
            numbers.append(int(line))

    candidates = []

    for i in range(0, len(numbers) - 2):
        for j in range(i + 1, len(numbers) - 1):
            for z in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[z] == 2020:
                    candidates.append([numbers[i], numbers[j], numbers[z]])

    if len(candidates) != 1:
        print("too many results")

    total = candidates[0][0] * candidates[0][1] * candidates[0][2]
    print(f"total {total}")


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()

