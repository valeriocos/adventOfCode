INPUT_PATH = "./input.txt"
MAX_ROW = 127
MAX_COLUMN = 7


def find_pos(data, lower_half_code, upper_half_code, max_range):
    current_interval = (0,  max_range)
    for e in data:
        sum_interval = current_interval[1] - current_interval[0] + 1
        if e == lower_half_code:
            current_interval = (current_interval[0], int(current_interval[1] - sum_interval/2))
        elif e == upper_half_code:
            current_interval = (int(current_interval[0] + sum_interval/2), current_interval[1])

    if current_interval[0] != current_interval[1]:
        print("Something is wrong")

    return current_interval[0]


def get_seats():
    seats = []

    with open(INPUT_PATH, 'r') as f:
        for line in f:
            content = line.strip()
            row = find_pos(content[:-3], "F", "B", MAX_ROW)
            column = find_pos(content[-3:], "L", "R", MAX_COLUMN)

            seats.append((row, column))

    return seats


def part_1():
    seats = get_seats()

    seat_ids = []
    for s in seats:
        seat_id = (s[0] * 8) + s[1]
        seat_ids.append(seat_id)

    print(f"Max seat ID: {max(seat_ids)}")


def part_2():
    seats = get_seats()

    seats_dict = {}
    for r, c in seats:
        if r in seats_dict:
            columns = seats_dict.get(r)
            columns.append(c)
        else:
            seats_dict.update({r: [c]})

    missing_seats = []
    for r in range(0, MAX_ROW):
        for c in range(0, MAX_COLUMN):
            if seats_dict.get(r):
                if c not in seats_dict.get(r):
                    missing_seats.append((r, c))
            else:
                print(f"row {r} is missing")

    if len(missing_seats) != 1:
        print("Too many missing seats")

    missing_seat_id = (missing_seats[0][0] * 8) + missing_seats[0][1]

    next_seats = []
    for s in seats:
        seat_id = (s[0] * 8) + s[1]
        if seat_id == missing_seat_id + 1 or seat_id == missing_seat_id - 1:
            next_seats.append((s[0], s[1], seat_id))

    if len(next_seats) != 2:
        print("Too many next seats")

    print(f"Missing seat ID: {missing_seat_id}")



def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
