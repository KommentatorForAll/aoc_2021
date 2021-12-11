def part_a():
    with open('input.txt', 'r') as f:
        inp = f.read().split('\n')
    opening = '([{<'
    closing = ')]}>'
    scores = [3, 57, 1197, 25137]
    total_score = 0
    for line in inp:
        stack = []
        tmp_score = 0
        for c in line:
            if c in opening:
                stack.append(opening.find(c))
            elif c in closing:
                ind = closing.find(c)
                last = stack.pop()
                if ind != last:
                    total_score += scores[ind]
                    break
            total_score += tmp_score

    print(total_score)


def part_b():
    with open('input.txt', 'r') as f:
        inp = f.read().split('\n')
    opening = '([{<'
    closing = ')]}>'
    scores = [1, 2, 3, 4]
    total_score = []
    for line in inp:
        stack = []
        tmp_score = 0
        corrupted = False
        for c in line:
            if c in opening:
                stack.append(opening.find(c))
            elif c in closing:
                ind = closing.find(c)
                last = stack.pop()
                if ind != last:
                    corrupted = True
                    break
        if not corrupted:
            while len(stack) != 0:
                tmp_score *= 5
                tmp_score += scores[stack.pop()]
            total_score += [tmp_score]
    total_score.sort()
    print(total_score[len(total_score)//2])


if __name__ == '__main__':
    part_b()
