def part_a():
    with open('input.txt', 'r') as f:
        input = [l.split(' ') for l in f.readlines()]
    x, d = 0, 0
    for inst, amount in input:
        amount = int(amount)
        if inst == 'forward':
            x += amount
        elif inst == 'down':
            d += amount
        elif inst == 'up':
            d -= amount
        else:
            assert False
    print(x*d)


def part_b():
    with open('input.txt', 'r') as f:
        input = [l.split(' ') for l in f.readlines()]
    x, d, aim = 0, 0, 0
    for inst, amount in input:
        amount = int(amount)
        if inst == 'forward':
            x += amount
            d += aim * amount
        elif inst == 'down':
            aim += amount
        elif inst == 'up':
            aim -= amount
        else:
            assert False
    print(x*d)


if __name__ == '__main__':
    part_b()
