INPUT_PATH = "./input.txt"

NOP = "nop"
ACC = "acc"
JMP = "jmp"


def load_instrs():
    instrs = []
    with open(INPUT_PATH, 'r') as f:
        for line in f:
            content = line.strip()
            stripped = content.split(" ")
            cmd = stripped[0].strip()
            value = int(stripped[1].strip())

            instrs.append((cmd, value))

    return instrs


def exec(instrs):
    accumulator = 0
    i = 0
    visited = []
    ended = True
    while i < len(instrs):
        cmd, value = instrs[i]

        found = [p for instr, p in visited if p == i]
        if found:
            ended = False
            break

        visited.append((instrs[i], i))

        if cmd == NOP:
            i += 1
            continue
        elif cmd == ACC:
            accumulator = accumulator + value
            i += 1
        elif cmd == JMP:
            i = i + value

    return accumulator, ended


def part_1():
    instrs = load_instrs()
    accumulator, ended = exec(instrs)
    print(f"accumlator is {accumulator}, program ended: {ended}")


def part_2():
    instrs = load_instrs()

    for i in range(0, len(instrs)):
        cmd, value = instrs[i]
        if cmd == NOP:
            instrs_copied = load_instrs()
            instrs_copied[i] = (JMP, value)
            accumulator, ended = exec(instrs_copied)
            if ended:
                print(f"accumlator is {accumulator}, program ended: {ended}")
                break
        elif cmd == JMP:
            instrs_copied = load_instrs()
            instrs_copied[i] = (NOP, value)
            accumulator, ended = exec(instrs_copied)
            if ended:
                print(f"accumlator is {accumulator}, program ended: {ended}")
                break


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
