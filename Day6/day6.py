def part_a():
    with open('input.txt', 'r') as f:
        inp = [int(x) for x in f.read().split(',')]
    day = 0
    while day < 256:
        to_add = []
        for i, fish in enumerate(inp):
            inp[i] -= 1
            if inp[i] < 0:
                to_add.append(8)
                inp[i] = 6
        inp.extend(to_add)
        day += 1
    print(len(inp))


if __name__ == '__main__':
    part_a()
