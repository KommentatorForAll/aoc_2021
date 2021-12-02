import time


def part_a():
    t1 = time.time()
    with open('input.txt', 'r') as f:
        inputs = [int(i) for i in f.readlines()]
    increases = 0
    last_inp = -1
    for i in inputs:
        if last_inp == -1:
            last_inp = i
            continue
        if i > last_inp:
            increases += 1
        last_inp = i
    t2 = time.time()
    print(increases)
    print(f'finished in {t2-t1} seconds')


def part_a_comp():
    with open('input.txt', 'r') as f:
        inputs = [int(i) for i in f.readlines()]
    increases, last_inp = 0, -1
    for i in inputs:
        if -1 != i > last_inp:
            increases += 1
        last_inp = i
    print(increases)



def part_b():
    with open('input.txt', 'r') as f:
        inputs = [int(i) for i in f.readlines()]
    increases = 0
    inps = inputs[:3]
    for i in inputs[3:]:
        last_sum = sum(inps)
        inps = inps[1:] + [i]
        if sum(inps) > last_sum:
            increases += 1
    print(increases)


if __name__ == '__main__':
    part_a()
