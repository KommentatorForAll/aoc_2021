import bisect
import time

import numpy as np


class Node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return f'{self.x}, {self.y}: {self.val}'


def main(part_a=False):
    t0 = time.time()
    with open('input.txt', 'r') as f:
        inp = np.array([[int(i) for i in x] for x in f.read().split('\n')])
    field = np.zeros((inp.shape[0]*5, inp.shape[1]*5))
    tmp = inp - 1
    if not part_a:
        for x in range(9):
            tmp += 1
            tmp = np.array([[int(str(a)[0] or str(a)[-1]) for a in row] for row in tmp])
            for i in range(5):
                for j in range(5):
                    if i+j == x:
                        field[i*inp.shape[0]:(i+1)*inp.shape[0], j*inp.shape[1]:(j+1)*inp.shape[1]] = tmp
    else:
        field = inp
    print(field)
    path = [Node(0, 0, 0)]
    used = {(0, 0): 0}
    stopped = False
    while not stopped:
        node = path[0]
        npos = node.x-1, node.y

        if node.x > 0:
            nval = node.val + field[node.x-1, node.y]
            if npos not in used or used[npos] > nval:
                used[npos] = nval
                bisect.insort(path, Node(node.x-1, node.y, nval))
        npos = node.x+1, node.y

        if node.x < field.shape[0] - 1:
            nval = node.val + field[node.x+1, node.y]
            if npos not in used or used[npos] > nval:
                used[npos] = nval
                bisect.insort(path, Node(node.x+1, node.y, nval))
        npos = node.x, node.y-1

        if node.y > 0:
            nval = node.val + field[node.x, node.y-1]
            if npos not in used or used[npos] > nval:
                used[npos] = nval
                bisect.insort(path, Node(node.x, node.y-1, nval))
        npos = node.x, node.y+1

        if node.y < field.shape[1] - 1:
            nval = node.val + field[node.x, node.y+1]
            if npos not in used or used[npos] > nval:
                used[npos] = nval
                bisect.insort(path, Node(node.x, node.y+1, nval))
        path.remove(node)
        if path[0].x == field.shape[0] - 1 and path[0].y == field.shape[1] - 1:
            stopped = True
    print(str(path[0]))
    print(time.time()-t0)


if __name__ == '__main__':
    main(False)
