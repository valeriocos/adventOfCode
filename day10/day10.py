INPUT_PATH = "./input.txt"

BUILTIN_ADAPTER_EXTRA = 3
CHARGING_OUTLET = 0
MIN_DIFF = 1
MAX_DIFF = 3


def load():
    jolts = []
    with open(INPUT_PATH, 'r') as f:
        for line in f:
            content = line.strip()
            jolts.append(int(content))

    return jolts


def get_arrangement():
    jolts = load()
    device_adapter = max(jolts) + BUILTIN_ADAPTER_EXTRA

    jolts.sort()
    jolts.insert(0, CHARGING_OUTLET)
    diffs = []
    sequence = [CHARGING_OUTLET]
    for i in range(1, len(jolts)):
        if i == 0:
            continue
        diff = jolts[i] - jolts[i - 1]
        sequence.append(jolts[i])
        diffs.append(diff)

    diffs.append(device_adapter - jolts[-1])
    sequence.append(device_adapter)

    return diffs, sequence


def part_1():
    diffs, _ = get_arrangement()
    one_diffs = len([d for d in diffs if d == MIN_DIFF])
    three_diffs = len([d for d in diffs if d == MAX_DIFF])
    print(f"Found 1-jolt diffs: {one_diffs}, 3-jolt diffs: {three_diffs}, which return {one_diffs * three_diffs}")


def create_graph(lst):
    graph = {}
    for i in range(0, len(lst)):
        graph[lst[i]] = []
        for j in range(i+1, len(lst)):
            if MIN_DIFF <= abs(lst[j] - lst[i]) <= MAX_DIFF:
                next = graph[lst[i]]
                next.append(lst[j])
            else:
                break

    return graph


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return 1
    if start not in graph:
        return 0
    paths = 0
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            paths += newpaths
    return paths


def visit_graph(lst):
    graph = {max(lst) + 3: 1}
    for i in range(max(lst) + 3, -1, -1):
        if i in lst:
            graph[i] = sum(graph.get(i + k, 0) for k in range(1, 4))
    return graph


def inefficient_part_2(lst):
    graph = create_graph(lst)
    paths = find_all_paths(graph, lst[0], lst[-1], [])
    print(f"Unique arrangements: {paths}")


def part_2():
    _, lst = get_arrangement()
    lst.sort()

    # inefficient_part_2(lst)
    paths = visit_graph(lst)[0]
    print(f"Unique arrangements: {paths}")


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
