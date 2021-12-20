import time

import numpy as np


def fetch_input():
    with open('input.txt', 'r') as f:
        inp = f.read().split('\n')
    algo = inp[0].replace('.', '0').replace('#', '1')
    img = inp[2:]
    img = np.array([['1' if x == '#' else '0' for x in row] for row in img])
    return algo, img


def enhance_image(img, algo, step):
    current = np.zeros((img.shape[0]+10, img.shape[1]+10))
    current.fill(algo[(not (step % 2))*511])
    current[5:-5, 5:-5] = img

    new = np.zeros(current.shape)
    for x in range(1, current.shape[0]-1):
        for y in range(1, current.shape[1]-1):
            binary = ''.join([str(int(x)) for x in current[x-1:x+2, y-1:y+2].flatten()])
            i = int(binary, 2)
            new[x, y] = algo[i]
    return new[1:-1, 1:-1]


def part_a():
    t0 = time.time()
    algo, img = fetch_input()
    for i in range(50):
        img = enhance_image(img, algo, i)
        if i == 1:
            print('part a:')
            print(img.sum())
            print(f'{time.time()-t0} seconds')
    print('part b:')
    print(img.sum())
    print(img.shape)
    print(f'{time.time()-t0} seconds')


if __name__ == '__main__':
    part_a()
