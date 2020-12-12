INPUT_PATH = "./input.txt"

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

NE = (1, 1)
SE = (1, -1)
SW = (-1, -1)
NW = (-1, 1)

DRTS = [EAST, SOUTH, WEST, NORTH]
SECTORS = [NE, SE, SW, NW]

X = 'x'
Y = 'y'
DRT = 'd'
SCT = 's'


def load():
    instrs = []
    with open(INPUT_PATH, 'r') as f:
        for line in f:
            content = line.strip()
            drt = content[0]
            mv = int(content[1:])
            instrs.append((drt, mv))

    return instrs


def turn(current, side, degrees):
    idx = DRTS.index(current)
    shift = int((degrees / 90)) * (-1 if side == LEFT else 1)
    idx += shift
    idx = idx % 4
    return DRTS[idx]


def relative_turn(waypoint_pos, side, degrees):
    shift = int((degrees / 90)) * (-1 if side == LEFT else 1)
    idx = SECTORS.index(waypoint_pos[SCT]) 
    idx += shift
    idx = idx % 4

    waypoint_pos[SCT] = SECTORS[idx]

    old_pos_x = waypoint_pos[X]
    old_pos_y = waypoint_pos[Y]

    if shift % 2 == 0:
        waypoint_pos[X] = old_pos_x
        waypoint_pos[Y] = old_pos_y
    else:
        waypoint_pos[X] = old_pos_y
        waypoint_pos[Y] = old_pos_x
    

def to_string(pos):
    y_axis = EAST if pos[Y] > 0 else WEST
    x_axis = SOUTH if pos[X] > 0 else NORTH

    print(f'{y_axis} {abs(pos[Y])}, {x_axis} {abs(pos[X])}')
    print(f'sum of abs values is {abs(pos[X]) + abs(pos[Y])}')


def part_1():
    pos = {
        X: 0,
        Y: 0,
        DRT: EAST,
    }
    instrs = load()
    for drt, mv in instrs:
        if drt == FORWARD:
            if pos[DRT] == EAST:
                pos[X] += mv
            elif pos[DRT] == WEST:
                pos[X] -= mv
            elif pos[DRT] == SOUTH:
                pos[Y] -= mv
            elif pos[DRT] == NORTH:
                pos[Y] += mv
        elif drt == EAST:
            pos[X] += mv
        elif drt == WEST:
            pos[X] -= mv
        elif drt == SOUTH:
            pos[Y] -= mv
        elif drt == NORTH:
            pos[Y] += mv
        elif drt in [RIGHT, LEFT]:
            pos[DRT] = turn(pos[DRT], drt, mv)

    to_string(pos)


def part_2():
    waypoint_pos = {
        X: 10,
        Y: 1,
        SCT: NE
    }
    ship_pos = {
        X: 0,
        Y: 0,
    }
    instrs = load()
    for drt, mv in instrs:
        if drt == FORWARD:
            ship_pos[X] += (waypoint_pos[X] * mv * waypoint_pos[SCT][0])
            ship_pos[Y] += (waypoint_pos[Y] * mv * waypoint_pos[SCT][1])
        elif drt == EAST:
            if waypoint_pos[SCT][0] == 1:
                waypoint_pos[X] += mv
            else:
                waypoint_pos[X] -= mv
        elif drt == WEST:
            if waypoint_pos[SCT][0] == 1:
                waypoint_pos[X] -= mv
            else:
                waypoint_pos[X] += mv
        elif drt == SOUTH:
            if waypoint_pos[SCT][1] == 1:
                waypoint_pos[Y] -= mv
            else:
                waypoint_pos[Y] += mv
        elif drt == NORTH:
            if waypoint_pos[SCT][1] == 1:
                waypoint_pos[Y] += mv
            else:
                waypoint_pos[Y] -= mv
        elif drt in [RIGHT, LEFT]:
            relative_turn(waypoint_pos, drt, mv)

    to_string(ship_pos)


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
