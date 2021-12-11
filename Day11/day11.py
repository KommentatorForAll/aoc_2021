import numpy as np


def part_a():
    with open('input.txt', 'r') as f:
        inp = np.array([[int(i) for i in line] for line in f.read().split('\n')])
    step = 0
    flashes = 0
    while step < 1000:
        flashed = np.zeros(inp.shape)
        has_flashed = True
        # increase all points by 1
        inp += 1
        while has_flashed:
            has_flashed = False
            for x in range(len(inp)):
                for y in range(len(inp[1])):
                    if inp[x, y] > 9 and not flashed[x, y]:
                        has_flashed = True
                        flashed[x, y] = True
                        inp[max(x-1, 0):min(x+2, len(inp)), max(y-1, 0):min(y+2, len(inp[1]))] += 1
                        inp[x, y] = 0
                        flashes += 1
        inp[flashed == 1] = 0
        step += 1
        if step == 100:
            print(f'{flashes} after step 100')
        if flashed.all():
            print(f'Sync at step {step}')
            break
        print(inp)
        print(flashed)
        print()


if __name__ == '__main__':
    part_a()
