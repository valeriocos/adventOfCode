import itertools

INPUT_PATH = "./input.txt"


def load():
    blocks = []

    with open(INPUT_PATH, 'r') as f:
        block = {}
        for line in f:
            content = line.strip()
            if content.startswith('mask'):
                if block:
                    blocks.append(block)
                    block = {}

                mask = content.split('=')[1].strip()
                block['mask'] = mask
                block['instrs'] = []
            else:
                splitted = content.split('=')
                mem_pos = splitted[0].strip().strip('mem[').strip(']')
                mem_value = splitted[1].strip()
                block['instrs'].append((int(mem_pos), int(mem_value)))

        if block:
            blocks.append(block)

    return blocks


def part_1():
    memory = {}
    blocks = load()

    for b in blocks:
        mask = b['mask']
        instrs = b['instrs']
        for pos, value in instrs:
            bits = '{0:036b}'.format(value)
            masked = ''

            for i in range(0, len(bits)):
                if mask[i] == 'X':
                    masked += bits[i]
                elif mask[i] in ['0', '1']:
                    masked += mask[i]

            memory[pos] = masked

    total = sum([int(memory[p], 2) for p in memory])
    print(f'{total}')


def expand(floating_address):
    addresses = []
    vars = len([f for f in floating_address if f == 'X'])
    combs = list(itertools.product(['0', '1'], repeat=vars))

    for comb in combs:
        address = ''
        occ_x = 0
        for i in floating_address:
            if i != 'X':
                address += i
            else:
                address += comb[occ_x]
                occ_x += 1
        addresses.append(address)

    return addresses


def part_2():
    memory = {}
    blocks = load()

    for b in blocks:
        mask = b['mask']
        instrs = b['instrs']
        for pos, value in instrs:
            pos_bits = '{0:036b}'.format(pos)
            value_bits = '{0:036b}'.format(value)
            masked = ''

            for i in range(0, len(pos_bits)):
                if mask[i] == 'X':
                    masked += mask[i]
                elif mask[i] == '0':
                    masked += pos_bits[i]
                elif mask[i] == '1':
                    masked += mask[i]

            addresses = expand(masked)
            for a in addresses:
                memory[a] = value_bits

    total = sum([int(memory[p], 2) for p in memory])
    print(f'{total}')


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
