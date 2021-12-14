import pandas as pd


def part_a():
    with open('input.txt', 'r') as f:
        inp = f.read().split('\n')

        start = list(inp[0])
        rules = {k: v for k, v in [x.split(' -> ') for x in inp[2:]]}

    step = 0
    while step < 40:
        print(len(start))
        new = []
        for i, v in enumerate(start[:-1]):
            new.append(v)
            new.append(rules[v+start[i+1]])
        new.append(start[-1])
        start = new
        step += 1
    # print(start)
    series = pd.Series(start).value_counts()
    print(series[0] - series[-1])


def part_b():
    with open('input.txt', 'r') as f:
        inp = f.read().split('\n')

        start = list(inp[0])
        rules = {k: v for k, v in [x.split(' -> ') for x in inp[2:]]}

    counts = pd.Series(start).value_counts()
    adjs = {}
    for i, v in enumerate(start[:-1]):
        k = v + start[i+1]
        if k not in adjs:
            adjs.setdefault(k, 0)
        adjs[k] += 1

    step = 0
    while step < 40:
        new = {}
        for k, v in adjs.items():
            itm = rules[k]
            nk_a = k[0] + itm
            nk_b = itm + k[1]
            if nk_a not in new:
                new.setdefault(nk_a, 0)
            if nk_b not in new:
                new.setdefault(nk_b, 0)
            new[nk_a] += v
            new[nk_b] += v
            print(counts)
            try:
                counts.loc[itm] += v
            except KeyError:
                print(itm)
                counts = counts.append(pd.Series({itm: v}))
        adjs = new
        step += 1
    print(counts)


if __name__ == '__main__':
    part_b()
