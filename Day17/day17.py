def simulate(init_vel, x_range, y_range):
    # print()
    vel = init_vel
    pos = (0, 0)
    hit = False
    through_shot = False
    highest = 0
    overshot = False

    while True:
        pos = pos[0] + vel[0], pos[1] + vel[1]
        vel = vel[0] - (1 if vel[0] > 0 else (-1 if vel[0] < 0 else 0)), vel[1] - 1
        if vel[1] == 0:
            # print(f'highest point: {pos[1]}')
            highest = pos[1]

        if pos[0] in x_range and pos[1] in y_range:
            hit = True
            break
        if pos[0] < x_range.start and vel[0] <= 0:
            overshot = False
            break
        if pos[0] > x_range.stop and vel[0] >= 0:
            overshot = True
            break
        if pos[1] < y_range.start:
            through_shot = True
            break
    return hit, through_shot, overshot, highest


def part_a():
    with open('input.txt', 'r') as f:
        x_range, y_range = f.read().split(' ')[2:]
    print(x_range, y_range)
    x_range = x_range.split('=')[1].split('..')
    x_range = range(int(x_range[0]), int(x_range[1][:-1]))
    y_range = y_range.split('=')[1].split('..')
    y_range = range(int(y_range[0]), int(y_range[1]))

    finished = False
    vel = (5, 0)
    init_vel = vel
    through_shots = 0
    last_hit = False
    while not finished:
        hit, through_shot, overshot, highest = simulate(vel, x_range, y_range)
        if hit:
            last_hit = init_vel
            init_vel = init_vel[0], init_vel[1]+1
            print(f'hit on: {last_hit}')
            overall_highest = highest
            through_shots = 0
        elif through_shot:
            print(f'through shot on: {init_vel}')
            init_vel = init_vel[0], init_vel[1]+1
            through_shots += 1
        elif overshot:
            print(f'overshot: {init_vel}')
            init_vel = init_vel[0] - 1, init_vel[1]
            through_shots = 0
        else:
            print(f'undershot: {init_vel}')
            init_vel = init_vel[0] + 1, init_vel[1]
            through_shots = 0

        if through_shots > 1000 and last_hit:
            finished = True

    print(last_hit, overall_highest)


def part_b():
    with open('input.txt', 'r') as f:
        x_range, y_range = f.read().split(' ')[2:]
    print(x_range, y_range)
    x_range = x_range.split('=')[1].split('..')
    x_range = range(int(x_range[0]), int(x_range[1][:-1])+1)
    y_range = y_range.split('=')[1].split('..')
    y_range = range(int(y_range[0]), int(y_range[1])+1)
    counts = 0
    for x in range(x_range.stop+1, 0, -1):
        for y in range(y_range.start-1, 1000):
            hit, through, over, highest = simulate((x, y), x_range, y_range)
            if hit:
                counts += 1
    print(counts)


if __name__ == '__main__':
    part_b()
