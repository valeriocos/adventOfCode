INPUT_PATH = "./input.txt"

PREAMBLE_SIZE = 25
TARGET_NUMBER = 15353384


def load():
    numbers = []
    with open(INPUT_PATH, 'r') as f:
        for line in f:
            content = line.strip()
            numbers.append(int(content))

    return numbers


def find_pairs(min_idx, max_idx, next_number):
    numbers = load()[min_idx:max_idx]
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if next_number == numbers[i] + numbers[j]:
                return {'found': True, 'idxs': [i, j], 'target': next_number}

    return {'found': False, 'idxs': [], 'target': next_number}


def part_1():
    numbers = load()
    min_idx = 0
    for i in range(PREAMBLE_SIZE, len(numbers)):
        next_number = numbers[i]
        max_idx = i
        res = find_pairs(min_idx, max_idx, next_number)
        if res['found']:
            continue
            # print(f'Number {res["target"]} is {numbers[res["idxs"][0]]} + {numbers[res["idxs"][1]]}')
        else:
            print(f'Pairs not found for {res["target"]}')

        min_idx += 1


def part_2():
    numbers = load()
    for i in range(0, len(numbers)):
        bucket = []
        bucket_idx = []
        for j in range(i, len(numbers)):
            bucket.append(numbers[j])
            bucket_idx.append(j)
            sum_bucket = sum(bucket)
            if sum_bucket > TARGET_NUMBER:
                bucket.clear()
                bucket_idx.clear()

            if sum_bucket == TARGET_NUMBER and len(bucket) > 1:
                min_num = min(bucket)
                max_num = max(bucket)
                print(f'Sum {sum_bucket} matches the target number, min num {min_num}, max num {max_num}, which sum up to {min_num + max_num}')
                return


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
