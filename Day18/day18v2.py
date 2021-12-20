import math
import re


digit = re.compile('\\d')


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().split('\n')


def add(a, b):
    current = f'[{a},{b}]'
    pnt = 0
    opens = 0
    exploded = False
    exploded_last = False
    while pnt < len(current):
        if pnt == len(current) - 1:
            exploded_last = exploded
            exploded = False
            if not exploded and not exploded_last:
                break
            pnt = 0
        print(current)
        print(' '*pnt + '^')
        print(opens)
        if current[pnt] == ']':
            opens -= 1
        elif current[pnt] == '[':
            opens += 1
            if opens == 5:
                exploded = True
                # print(f'{pnt}pnt; start exploding')
                # print(current)
                # print(' '*pnt + '^')
                j = pnt
                for i in range(2):
                    # if i:
                    #     print('exploding right')
                    # else:
                    #     print('exploding left')
                    while (not i and j > 0) or (i and j < len(current)):
                        # print(i, j)
                        if digit.match(current[j]):
                            to_add = int(current[pnt+1]) if not i else int(current[pnt+3])
                            try:
                                new = to_add + int(current[j-1:j+1] if not i else current[j:j+2])
                            except ValueError:
                                new = to_add + int(current[j])

                            # print(f'found digit at {j}')
                            # print(current)
                            # print(' '*j + '^')
                            # print(f'new value: {new}')
                            current = current[:j] + str(new) + current[j+1:]
                            if new >= 10:
                                pnt += 1
                            break
                        j += 1 if i else -1
                    j = pnt + 4
                current = current[:pnt] + '0' + current[pnt+5:]
                opens -= 1
            if not exploded and exploded_last:
                exploded = False
                pnt = -1
                opens = 0
                split = True
                while split:
                    split = False
                    j = 0
                    while j < len(current):
                        if digit.match(current[j]) and digit.match(current[j+1]):
                            print('splitting')
                            new = int(current[j:j+2])
                            current = f'{current[:j]}[{new//2},{math.ceil(new/2)}]{current[j+2:]}'
                            split = True
                        j += 1

        pnt += 1
    print(current)
    return current


def part_a():
    inp = read_input()
    current = inp[0]
    for line in inp[1:]:
        current = add(current, line)
        print('did line')
    print(current)


if __name__ == '__main__':
    part_a()
