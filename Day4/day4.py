import numpy as np


def check_if_won(mask):
    for m in [mask, mask.T]:
        try:
            for row in m:
                if row.all():
                    return True
        except TypeError:
            pass
    return False


def calc_num(board, mask, num):
    m = mask == False
    x = 0
    for row, mrow in zip(board, m):
        for j in range(len(row)):
            x += row[j] * mrow[j]
    return x * num


def part_a():
    with open('input.txt', 'r') as f:
        input_data = f.read().split('\n\n')
    numbers, boards = input_data[0], input_data[1:]
    numbers = [int(i) for i in numbers.split(',')]
    boards = [np.array([[int(x) for x in r.split(' ') if x != ''] for r in board.split('\n')]) for board in boards]
    masks = [np.ma.make_mask(np.array([[False for k in range(5)] for j in range(5)])) for i in range(len(boards))]

    for number in numbers:
        for i, board in enumerate(boards):
            mask = np.ma.make_mask(board == number)
            masks[i] = np.ma.mask_or(masks[i], mask, copy=True)
            if check_if_won(masks[i]):
                return calc_num(board, masks[i], number)


def part_b():
    with open('input.txt', 'r') as f:
        input_data = f.read().split('\n\n')
    numbers, boards = input_data[0], input_data[1:]
    numbers = [int(i) for i in numbers.split(',')]
    boards = [np.array([[int(x) for x in r.split(' ') if x != ''] for r in board.split('\n')]) for board in boards]
    masks = [np.ma.make_mask(np.array([[False for k in range(5)] for j in range(5)])) for i in range(len(boards))]
    won_mask = np.array([False for i in range(len(boards))])
    enable_end = False

    for number in numbers:
        for i, board in enumerate(boards):
            if won_mask[i]:
                continue
            mask = np.ma.make_mask(board == number)
            masks[i] = np.ma.mask_or(masks[i], mask, copy=True)
            if check_if_won(masks[i]):
                won_mask[i] = True
                if enable_end:
                    return calc_num(boards[i], masks[i], number)

        print(f'number: {number}, wonmask: {won_mask}')
        if won_mask.sum() == len(won_mask)-1:
            enable_end = True


if __name__ == '__main__':
    print(part_b())
