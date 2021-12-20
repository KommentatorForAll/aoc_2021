class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.points_left = True

    def left(self):
        if self.points_left:
            return None
        self.points_left = True
        return self.a

    def right(self):
        if not self.points_left:
            return None
        self.points_left = False
        return self.b

    def add(self, p: "Pair"):
        ret = Pair(self, p)
        trace = []
        finished = False
        current = ret
        while not finished:
            if isinstance(current.a, Pair) and current.points_left:
                trace.append(current)
                current.points_left = False
                current = current.a
            elif isinstance(current.b, Pair) and current.points_left is not None:
                trace.append(current)
                current.points_left = None
                current = current.b
            else:
                trace.pop()
            if len(trace) == 5:
                pass



    def get_magnitude(self):
        a = self.a.get_magnitude() if isinstance(self.a, Pair) else self.a
        b = self.b.get_magnitude() if isinstance(self.b, Pair) else self.b
        return 3 * a + 2 * b

    def __str__(self):
        return f'({self.a}, {self.b})'

    def __repr__(self):
        return self.__str__()


def parse_input():
    with open('input.txt', 'r') as f:
        inp = f.read().split('\n')
    lines = []
    elements = []
    for ln in inp:
        cur_ele = None
        num = ''
        for i, char in enumerate(ln):
            if char == '[':
                cur_ele = 'pair'
            elif char == ',':
                if cur_ele == 'num':
                    elements.append(int(num))
                    num = ''
                    cur_ele = ''
            elif char == ']':
                if cur_ele == 'num':
                    elements.append(int(num))
                    num = ''
                    cur_ele = ''
                b, a = elements.pop(), elements.pop()
                elements.append(Pair(a, b))
            else:
                cur_ele = 'num'
                num += char
        print(elements)
        lines.append(elements[0])
    return lines


def part_a():
    lines = parse_input()
    current = lines[0]
    for ln in lines[1:]:
        current.add(ln)
    print(current.get_magnitude())


if __name__ == '__main__':
    part_a()
