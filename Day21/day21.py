def part_a():
    with open('input.txt', 'r') as f:
        players = f.read().split('\n')
    players = [int(p.split(' ')[-1]) for p in players]
    score = [0]*len(players)
    i = 1
    rolls = 0
    while max(score) < 1000:
        for j, player in enumerate(players):
            val = (i % 10 + (i+1) % 10 + (i+2) % 10) % 10
            players[j] = (player + val) % 10
            score[j] += players[j] if players[j] else 10
            print(f'{j} {players[j]=}; {score[j]=}')
            i += 3
            rolls += 3
    p = min(zip(score, players))
    print(f'{p[0]=} {p[1]=} {p[0]-p[1]=} {rolls=}')
    print((p[0] - p[1])*(rolls - 3))


def part_b():
    with open('input.txt', 'r') as f:
        players = f.read().split('\n')
    players = [int(p.split(' ')[-1]) for p in players]
    score = [0]*len(players)
    cache = {}

    def create_universe(p1, ps, scrs, p1_cnt):
        ret = [0, 0]
        if (p1, *ps, *scrs, p1_cnt) in cache:
            return cache[(p1, *ps, *scrs, p1_cnt)]
        for i in range(1, 4):
            p_cpy = ps.copy()
            pos = (p_cpy[p1] + i) % 10
            p_cpy[p1] = pos
            sc_cpy = scrs.copy()
            if p1_cnt == 3:
                sc_cpy[p1] += pos if pos else 10
            if sc_cpy[p1] >= 21:
                ret[1] += p1
                ret[0] += 1
            else:
                res = create_universe(p1 if p1_cnt < 3 else not p1, p_cpy, sc_cpy, (p1_cnt+1) if p1_cnt < 3 else 0)
                ret = [sum(x) for x in zip(ret, res)]
        cache[(p1, *ps, *scrs, p1_cnt)] = ret
        return ret

    print(create_universe(0, players, score, 0))


def part_b_v2():
    with open('input.txt', 'r') as f:
        players = f.read().split('\n')
    players = [int(p.split(' ')[-1]) for p in players]
    scores = [0]*len(players)
    cache = {}
    throws = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

    def create_universe(p1, ps, scrs):
        if (p1, *ps, *scrs) in cache:
            return cache[(p1, *ps, *scrs)]

        ret = [0, 0]
        for k, v in throws.items():
            pos = ps.copy()
            p = (pos[p1] + k) % 10
            pos[p1] = p
            score = scrs.copy()
            score[p1] += p if p else 10
            if score[p1] >= 21:
                ret[0] += v
                ret[1] += v if p1 else 0
            else:
                res = create_universe(not p1, pos, score)
                res = res[0] * v, res[1] * v
                ret = [ret[0]+res[0], ret[1]+res[1]]
        cache[(p1, *ps, *scrs)] = ret
        print(ret)
        return ret

    uni_count, p1_wins = create_universe(False, players, scores)
    print(max(p1_wins, uni_count-p1_wins))
    print(f'{len(cache)=}')


if __name__ == '__main__':
    part_b_v2()
