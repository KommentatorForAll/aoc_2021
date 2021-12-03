import numpy as np
from bitstring import BitArray


def part_a():
    with open('input.txt', 'r') as f:
        inputs = [[int(c) for c in i if c != '\n'] for i in f.readlines()]
    inputs = np.array(inputs)
    gamma = [a.sum() > len(a)/2 for a in inputs.T]
    epsilon = [not a for a in gamma]
    gamma = BitArray(gamma).uint
    epsilon = BitArray(epsilon).uint
    print(f'gamma: {gamma}, epsilon: {epsilon}')
    print(gamma*epsilon)


def part_b():
    with open('input.txt', 'r') as f:
        inputs = [[int(c) for c in i if c != '\n'] for i in f.readlines()]
    inputs = np.array(inputs)

    def get_oxy(pos, arr):
        if len(arr) == 1:
            return arr[0]
        m = arr.T[pos].sum() >= len(arr.T[0])/2
        return get_oxy(pos+1, np.array([x for x in arr if x[pos] == m]))

    def get_co2(pos, arr):
        if len(arr) == 1:
            return arr[0]
        m = arr.T[pos].sum() >= len(arr.T[0])/2
        return get_co2(pos+1, np.array([x for x in arr if x[pos] != m]))

    oxy = BitArray(get_oxy(0, inputs)).uint
    co2 = BitArray(get_co2(0, inputs)).uint
    print(oxy * co2)


if __name__ == '__main__':
    part_b()
