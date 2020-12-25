import math

INPUT_PATH = "./input.txt"


def load():
    constraints = {}
    your = []
    nearby = []
    with open(INPUT_PATH, 'r') as f:
        your_ticket = False
        nearby_tickets = False
        for line in f:
            content = line.strip()
            if not content:
                your_ticket = False
                nearby_tickets = False
                continue

            if 'your' in content:
                your_ticket = True
                continue
            elif 'nearby' in content:
                nearby_tickets = True
                continue

            if your_ticket:
                your.extend([int(e) for e in content.split(',')])
            elif nearby_tickets:
                nearby.append([int(e) for e in content.split(',')])
            else:
                stripped = content.split(":")
                attribute = stripped[0].strip()
                values = stripped[1].strip()
                pairs = []
                for pair in values.split('or'):
                    aux = pair.strip().split('-')
                    min = int(aux[0].strip())
                    max = int(aux[1].strip())
                    pairs.append((min, max))
                constraints[attribute] = pairs

    return your, nearby, constraints


def find_invalids(values, constraints):
    valids = []
    for v in values:
        for c in constraints:
            conditions = constraints[c]
            for cond in conditions:
                if cond[0] <= v <= cond[1]:
                    valids.append(v)

    return list(set(values) - set(valids))


def update_valid_positions(values, constraints, valid_positions):
    positions = {}

    for c in constraints:
        conditions = constraints[c]
        for cond in conditions:
            for i in range(0, len(values)):
                if cond[0] <= values[i] <= cond[1]:
                    if c in positions:
                        positions[c].append(i)
                    else:
                        positions[c] = [i]

    for p in positions:
        valid_positions[p] = valid_positions[p].intersection(set(positions[p]))


def find_unique_positions(positions):
    unique_pos = []
    for p in positions:
        aux = positions[p]
        if len(aux) == 1:
            unique_pos.append(list(aux)[0])

    return unique_pos


def resolve_positions(valid_positions, target_len):
    while True:
        unique_pos = find_unique_positions(valid_positions)

        if len(unique_pos) == target_len:
            break

        for u in unique_pos:
            for v in valid_positions:
                positions = valid_positions[v]
                if len(positions) == 1:
                    continue
                if u in positions:
                    positions.remove(u)


def part_1():
    your, nearby, constraints = load()
    invalids = []
    for t in nearby:
        found = find_invalids(t, constraints)
        if found:
            invalids.extend(found)

    print(f'sum invalids: {sum(invalids)}')


def part_2():
    your, nearby, constraints = load()
    valid_positions = {}

    for c in constraints:
        valid_positions[c] = set([i for i in range(0, len(your))])

    for t in nearby:
        found = find_invalids(t, constraints)
        if found:
            continue

        update_valid_positions(t, constraints, valid_positions)

    update_valid_positions(your, constraints, valid_positions)
    resolve_positions(valid_positions, len(your))

    total = math.prod([your[valid_positions[v].pop()] for v in valid_positions if v.startswith('departure')])
    print(f'total: {total}')


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
