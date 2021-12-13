import numpy as np


def main(part_a=True):
    x = []
    y = []
    folds = []
    is_coord = True
    with open('input.txt', 'r') as f:
        for line in f.read().split('\n'):
            if line == '':
                is_coord = False
                continue
            if is_coord:
                c = line.split(',')
                y.append(int(c[0]))
                x.append(int(c[1]))
            else:
                folds.append(line.split('='))

    paper = np.ma.make_mask(np.zeros((max(x)+1, 1311)), shrink=False)
    for pos_x, pos_y in zip(x, y):
        paper[pos_x, pos_y] = True
    # print(np.array([['+' if x else '.' for x in row] for row in paper]))
    for fold in folds:
        i = int(fold[1])
        print(paper.shape)
        # print(i)
        if fold[0] == 'fold along y':
            # print(paper[i, :].any())
            # for j in range(len(paper)):
            #     print(['-' if j == i else ('#' if x else '.') for x in paper[j]])
            paper = np.ma.mask_or(paper[:i, :], paper[:i:-1, :])
        elif fold[0] == 'fold along x':
            # print(paper[:, i].any())
            # print(paper[:, :i].shape)
            # print(paper[:, :i:-1].shape)
            paper = np.ma.mask_or(paper[:, :i], paper[:, :i:-1])
        if part_a:
            break
    print(np.array([['+' if x else '.' for x in row] for row in paper]))
    for j in range(len(paper)):
        print(''.join(['#' if x else '.' for x in paper[j]]))
    print(paper.sum())


if __name__ == '__main__':
    main(False)
