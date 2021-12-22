from typing import List

import numpy as np


def fetch_input():
    with open('input.txt', 'r') as f:
        inp = f.read().split('\n')
    inp = [x.split(' ') for x in inp]
    instructions = []
    for state, ran in inp:
        state = state == 'on'
        x_ran, y_ran, z_ran = ran.split(',')
        x_ran = range(*[int(x) for x in x_ran.split('=')[1].split('..')])
        y_ran = range(*[int(x) for x in y_ran.split('=')[1].split('..')])
        z_ran = range(*[int(x) for x in z_ran.split('=')[1].split('..')])
        instructions.append((state, x_ran, y_ran, z_ran))

    return instructions


def part_a():
    instructions = fetch_input()
    reactor = np.zeros((102, 102, 102))
    offset = 51
    for instruction in instructions:
        reactor[
        instruction[1].start + offset:instruction[1].stop + 1 + offset,
        instruction[2].start + offset:instruction[2].stop + 1 + offset,
        instruction[3].start + offset:instruction[3].stop + 1 + offset
        ] = instruction[0]
    print(reactor.sum())


class Box:
    def __init__(self, x_ran, y_ran, z_ran):
        self.intersects: List[Box] = []
        self.x_min = x_ran.start
        self.x_max = x_ran.stop
        self.y_min = y_ran.start
        self.y_max = y_ran.stop
        self.z_min = z_ran.start
        self.z_max = z_ran.stop

    def _intersects(self, other):
        if isinstance(other, Box):

            if other.x_min > self.x_max or other.x_max < self.x_min:
                return False
            if other.y_min > self.y_max or other.y_max < self.y_min:
                return False
            if other.z_min > self.z_max or other.z_max < self.z_min:
                return False
            return True
        return self.x_min <= other[0] <= self.x_max \
               and self.y_min <= other[1] <= self.y_max \
               and self.z_min <= other[2] <= self.z_max

    def difference(self, other: "Box"):
        if not self._intersects(other):
            return
        intersection = Box(
            range(max(self.x_min, other.x_min), min(self.x_max, other.x_max)),
            range(max(self.y_min, other.y_min), min(self.y_max, other.y_max)),
            range(max(self.z_min, other.z_min), min(self.z_max, other.z_max))
        )
        for inter in self.intersects:
            inter.difference(intersection)
        self.intersects.append(intersection)

    def get_volume(self):
        return (self.x_max + 1 - self.x_min) *\
               (self.y_max + 1 - self.y_min) *\
               (self.z_max + 1 - self.z_min) \
               - sum([b.get_volume() for b in self.intersects]
                     )


def part_b():
    instructions = fetch_input()
    shapes = []
    for inst in instructions:
        box = Box(inst[1], inst[2], inst[3])
        [b.difference(box) for b in shapes]
        if inst[0]:
            shapes.append(box)
    print(sum([b.get_volume() for b in shapes]))


if __name__ == '__main__':
    part_b()
