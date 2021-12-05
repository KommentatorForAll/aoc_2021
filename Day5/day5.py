import math

import numpy as np


def part_a():
    with open('input.txt', 'r') as f:
        inputs = [pnt.split(' -> ') for pnt in f.read().split('\n')]
    x_max = y_max = 0
    lines = []
    for i, line in enumerate(inputs):
        start, end = line
        start_pnt = [int(x) for x in start.split(',')]
        end_pnt = [int(x) for x in end.split(',')]
        if start_pnt[0] != end_pnt[0] and start_pnt[1] != end_pnt[1]:
            continue
        lines.append((start_pnt, end_pnt))
        if start_pnt[0] > x_max:
            x_max = start_pnt[0]
        if end_pnt[0] > x_max:
            x_max = end_pnt[0]
        if start_pnt[1] > y_max:
            y_max = start_pnt[1]
        if end_pnt[1] > y_max:
            y_max = end_pnt[1]
    ground = np.zeros((x_max+1, y_max+1))
    for line in lines:
        x_inc = -math.floor(math.copysign(1, line[0][0]-line[1][0]))
        for x in range(line[0][0], line[1][0]+x_inc, x_inc):
            y_inc = -math.floor(math.copysign(1, line[0][1] - line[1][1]))
            for y in range(line[0][1], line[1][1] + y_inc, y_inc):
                ground[x, y] += 1
    mask = ground >= 2
    print(mask.sum())


def part_b():
    with open('input.txt', 'r') as f:
        inputs = [pnt.split(' -> ') for pnt in f.read().split('\n')]
    x_max = y_max = 0
    lines = []
    for i, line in enumerate(inputs):
        start, end = line
        start_pnt = [int(x) for x in start.split(',')]
        end_pnt = [int(x) for x in end.split(',')]
        lines.append((start_pnt, end_pnt))
        if start_pnt[0] > x_max:
            x_max = start_pnt[0]
        if end_pnt[0] > x_max:
            x_max = end_pnt[0]
        if start_pnt[1] > y_max:
            y_max = start_pnt[1]
        if end_pnt[1] > y_max:
            y_max = end_pnt[1]
    ground = np.zeros((x_max+1, y_max+1))
    for line in lines:
        x_inc = -math.floor(math.copysign(1, line[0][0]-line[1][0]))
        y_inc = -math.floor(math.copysign(1, line[0][1] - line[1][1]))
        if line[0][0]-line[1][0] == 0 or line[0][1] - line[1][1] == 0:
            print(line)
            for x in range(line[0][0], line[1][0]+x_inc, x_inc):
                for y in range(line[0][1], line[1][1] + y_inc, y_inc):
                    ground[x, y] += 1
        else:
            nx = line[0][0]
            ny = line[0][1]
            while nx != line[1][0] + x_inc:
                ground[nx, ny] += 1
                nx += x_inc
                ny += y_inc
    mask = ground >= 2
    print(ground)
    print(mask.sum())


if __name__ == '__main__':
    part_b()
