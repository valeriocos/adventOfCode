INPUT_PATH = "./input.txt"

BUS_NOT_AVAILABLE = 'x'
BUS_DEPARTURE = 'D'
LAST_DEPARTURE = 100


def load_info(remove_x=True):
    with open(INPUT_PATH, 'r') as f:
        content = f.readlines()
        start = int(content[0].strip())
        if remove_x:
            lines = [int(line) for line in content[1].split(',') if remove_x and line != BUS_NOT_AVAILABLE]
        else:
            lines = [line for line in content[1].split(',')]

    return start, lines


def create_schedule(start, lines):
    buses = {}
    for l in lines:
        departures = []
        t = 0
        while t <= start + LAST_DEPARTURE:
            t += l

            if t < start:
                continue

            departures.append(t)

        buses[l] = departures

    return buses


def find_next_departure(schedule):
    next_departure = None
    for b in schedule:
        t = schedule[b][0]
        if not next_departure:
            next_departure = (b, t)
            continue

        if t < next_departure[1]:
            next_departure = (b, t)

    return next_departure


def part_1():
    start, lines = load_info()
    schedule = create_schedule(start, lines)
    bus, t = find_next_departure(schedule)

    print(f'Next departure bus {bus}, time {t}, total: {bus * (t - start)}')


def create_t_schedule(lines):
    buses = {}
    t = -1
    for l in lines:
        t += 1
        try:
            line = int(l)
            buses[line] = t
        except:
            continue

    return buses


def part_2():
    _, lines = load_info(remove_x=False)
    schedule = create_t_schedule(lines)

    diffs = [(b, schedule[b]) for b in schedule]
    delta, time = 1, 100000000000000

    for bus, offset in diffs:
        while (time + offset) % bus != 0:
            time += delta
        delta *= bus

    print(f"Part 2: {time}")


def part_2_not_efficient():
    _, lines = load_info(remove_x=False)
    schedule = create_t_schedule(lines)

    buses = len(schedule)
    t = 1
    a = 1
    flag = True

    while flag:
        ok = 0
        for freq in schedule:
            ok += 1
            if (t + schedule[freq]) % freq != 0:
                t = ((freq * a) - schedule[freq])
                a += 1
                ok = 0
                continue

        if buses == ok:
            print(f'Min t is {t}')
            break


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
