def part_a():
    with open('input.txt', 'r') as f:
        inp = [x.split('|') for x in f.read().split('\n')]

    cnt = 0
    for line in inp:
        nums = line[1]
        print(nums)
        for num in nums.split(' '):
            if len(num) in [2, 3, 4, 7]:
                cnt += 1
    print(cnt)


def part_b():
    with open('input.txt', 'r') as f:
        inp = [x.split('|') for x in f.read().split('\n')]

    s = 0
    for line in inp:
        tmp_res = ''
        test_nums = line[0].split(' ')
        test_nums.sort(key=len)
        test_nums = [set(list(x)) for x in test_nums[1:]]
        for num in line[1].split(' '):
            if len(num) == 2:
                tmp_res += '1'
            elif len(num) == 3:
                tmp_res += '7'
            elif len(num) == 4:
                tmp_res += '4'
            elif len(num) == 7:
                tmp_res += '8'
            elif len(num) == 5:
                if test_nums[0] in set(list(num)):
                    tmp_res += '3'
                elif (test_nums[2] - test_nums[0]) in set(list(num)):
                    tmp_res += '5'
                else:
                    tmp_res += '2'
            elif len(num) == 0:
                continue
            else:
                if len(num) != 6:
                    print(len(num))
                    raise ValueError('unexpected number')
                if test_nums[2] in set(list(num)):
                    tmp_res += '9'
                elif test_nums[0] in set(list(num)):
                    tmp_res += '0'
                else:
                    tmp_res += '6'
        s += int(tmp_res)
    print(s)


if __name__ == '__main__':
    part_b()
