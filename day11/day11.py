import copy

INPUT_PATH = "./input.txt"

EMPTY = "L"
OCCUPIED = "#"
FLOOR = '.'


def load():
    matrix = {}
    with open(INPUT_PATH, 'r') as f:
        row = 0
        for line in f:
            content = line.strip()
            matrix[row] = [e for e in content]
            row += 1

    return matrix


def get_visible_seats(matrix, i, j):
    visble = {
        'n': FLOOR,
        'ne': FLOOR,
        'e': FLOOR,
        'se': FLOOR,
        's': FLOOR,
        'sw': FLOOR,
        'w': FLOOR,
        'nw': FLOOR
    }

    directions = [('w', -1, 0), ('e', 1, 0), ('s', 0, 1), ('n', 0, -1), ('sw', -1, 1), ('nw', -1, -1), ('ne', 1, -1), ('se', 1, 1)]

    for d, increment_i, increment_j in directions:
        x = i
        y = j

        while 0 <= y < len(matrix[i]) and 0 <= x < len(matrix):
            x += increment_i
            y += increment_j

            if x < 0 or y < 0:
                continue
            if x > len(matrix) or y > len(matrix[i]):
                continue

            try:
                if matrix[x][y] == OCCUPIED:
                    visble[d] = OCCUPIED
                    break
                elif matrix[x][y] == EMPTY:
                    visble[d] = EMPTY
                    break
            except:
                continue

    return {EMPTY: sum([1 for v in visble.values() if v == EMPTY]), OCCUPIED: sum([1 for v in visble.values() if v == OCCUPIED])}


def get_adj_seats(matrix, i, j):
    empty = 0
    occupied = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x == i and j == y:
                continue

            if x < 0 or y < 0:
                continue

            try:
                if matrix[x][y] == EMPTY:
                    empty += 1
                elif matrix[x][y] == OCCUPIED:
                    occupied += 1
            except:
                continue

    return {EMPTY: empty, OCCUPIED: occupied}


def count(matrix):
    total = 0
    empty = 0
    occupied = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            total += 1
            if matrix[i][j] == EMPTY:
                empty += 1
            elif matrix[i][j] == OCCUPIED:
                occupied += 1

    return {EMPTY: empty, OCCUPIED: occupied, 'total': total}


def part_1():
    matrix = load()
    while True:
        new_matrix = copy.deepcopy(matrix)
        changes = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                seat = matrix[i][j]
                adjs = get_adj_seats(matrix, i, j)
                if seat == EMPTY and adjs[OCCUPIED] == 0:
                    new_matrix[i][j] = OCCUPIED
                    changes += 1
                elif seat == OCCUPIED and adjs[OCCUPIED] >= 4:
                    new_matrix[i][j] = EMPTY
                    changes += 1

        if changes == 0:
            info = count(matrix)
            print(f"Total seats {info['total']}, occupied {info[OCCUPIED]}, empty {info[EMPTY]}")
            break

        matrix = copy.deepcopy(new_matrix)


def part_2():
    matrix = load()
    while True:
        new_matrix = copy.deepcopy(matrix)
        changes = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                seat = matrix[i][j]
                adjs = get_visible_seats(matrix, i, j)
                if seat == EMPTY and adjs[OCCUPIED] == 0:
                    new_matrix[i][j] = OCCUPIED
                    changes += 1
                elif seat == OCCUPIED and adjs[OCCUPIED] >= 5:
                    new_matrix[i][j] = EMPTY
                    changes += 1

        if changes == 0:
            info = count(matrix)
            print(f"Total seats {info['total']}, occupied {info[OCCUPIED]}, empty {info[EMPTY]}")
            break

        matrix = copy.deepcopy(new_matrix)


def main():
    # part_1()
    part_2()


if __name__ == "__main__":
    main()
