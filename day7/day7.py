INPUT_PATH = "./input.txt"

BAGS = {}


def load_bags():
    with open(INPUT_PATH, 'r') as f:
        for line in f:
            content = line.strip()
            splitted = content.split("contain")
            bag_type = splitted[0].replace("bags", "").strip()
            sub_bags = splitted[1].split(",")
            contained_bags = {}
            for sb in sub_bags:
                if "no other bag" in sb:
                    continue
                digested = sb.replace("bags", "").replace("bag", "").strip(".").strip().split(" ")
                num_sub_bag = int(digested[0].strip())
                sub_bag_type = ' '.join(digested[1:]).strip()
                contained_bags[sub_bag_type] = num_sub_bag

            BAGS.update({bag_type: contained_bags})


def find_path(bag, target, path):
    if target in bag:
        return path
    elif target in BAGS.get(bag):
        path.append(target)
        return path
    else:
        for sub_bag in BAGS.get(bag):
            path.append(sub_bag)
            return find_path(sub_bag, target, path)


def find_paths(bag, target):
    all_paths = []
    for sub_bag in BAGS.get(bag):
        p = find_path(sub_bag, target, [sub_bag])
        if p:
            all_paths.append(p)

    return all_paths


def wrong_part_1():
    load_bags()
    target = "shiny gold"

    options = []
    for bag in BAGS:
        paths = find_paths(bag, target)
        if paths:
            options.append((bag, paths))

    print(options)
    print(f"Possible options for {target} is {len(options)}")


def find_ancestors(to_visit):
    visited = []
    while to_visit:
        next_bag = to_visit.pop()
        for bag in BAGS:
            if bag in to_visit:
                continue
            if next_bag in BAGS.get(bag):
                to_visit.append(bag)

        if next_bag not in visited:
            visited.append(next_bag)

    return visited


def find_children(to_visit):
    visited = []
    while to_visit:
        next_bag, qty = to_visit.pop()
        for sub_bag in BAGS.get(next_bag):
            if sub_bag in to_visit:
                continue
            sub_qty = qty * BAGS[next_bag][sub_bag]
            to_visit.append((sub_bag, sub_qty))
        if next_bag not in visited:
            visited.append((next_bag, qty))

    return visited


def part_1():
    load_bags()
    target = "shiny gold"

    ancestors = find_ancestors([target])
    ancestors.remove(target)
    print(f"Number of ancestors for {target} is {len(ancestors)}")


def part_2():
    load_bags()
    target = "shiny gold"
    children = find_children([(target, 1)])
    total_bags = sum([num for c, num in children]) - 1
    print(f"Number of bags for {target} is {total_bags}")


def main():
    # wrong_part_1()
    part_1()
    part_2()


if __name__ == "__main__":
    main()
