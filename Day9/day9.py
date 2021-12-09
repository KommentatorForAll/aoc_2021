import numpy as np
from scipy import signal


def part_a():
    with open('input.txt') as f:
        inp = np.array([[int(a) for a in list(x)] for x in f.read().split('\n')])
    pad = np.zeros((len(inp)+2, len(inp[0])+2))
    pad.fill(9)
    pad[1:len(inp)+1, 1:len(inp[0])+1] = inp
    pad[pad == 0] = -1
    kernel = np.array([0, 1]*4 + [0]).reshape((3, 3))
    mask = np.zeros(inp.shape)
    for x in range(len(inp)):
        for y in range(len(inp[0])):
            sel: np.ndarray = pad[x:x+3, y:y+3] * kernel
            sel[sel == 0] = 9
            mask[x, y] = not (sel.flatten() <= inp[x, y]).any()
            # print(f'sel: {sel}; {inp[x, y]}; mask: {mask[x, y]}')
    # print(inp)
    # print(mask)
    # print(inp*mask)
    inp = inp + 1
    print((inp * mask).sum())

    adj = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def get_basin(x, y, pad, used):
        if pad[x, y] == 9:
            return 0
        v = 1
        val = pad[x, y]
        for a in adj:
            coords = x+a[0], y+a[1]
            if pad[coords[0], coords[1]] > val and not used[coords[0], coords[1]]:
                used[coords[0], coords[1]] = True
                v += get_basin(*coords, pad, used)
        return v

    l = [0, 0, 0]
    for x in range(len(mask)):
        for y in range(len(mask[1])):
            if mask[x, y]:
                l.append(get_basin(x+1, y+1, pad, np.zeros(pad.shape)))
                print(l[-1])
                l.sort()
                l = l[1:]
    print(l)

    # print(get_basin(1, 2, pad))

if __name__ == '__main__':
    part_a()
