def part_a(pos: dict, target):
    s = 0
    for i, cnt in pos.items():
        n = (i-target) if i > target else (target - i)
        s += n * cnt
    return s


def part_b(pos: dict, target):
    s = 0
    for i, cnt in pos.items():
        n = (i-target) if i > target else (target - i)
        s += (n*(n+1))/2 * cnt
    return s


def main(fuel_calc):
    with open('input.txt', 'r') as f:
        inp = [int(x) for x in f.read().split(',')]

    pos = dict()
    for i in inp:
        pos.setdefault(i, 0)
        pos[i] += 1

    fuels = []
    for i in range(max(pos.keys())+1):
        fuels.append(fuel_calc(pos, i))
    print(min(fuels))


if __name__ == '__main__':
    main(part_b)
