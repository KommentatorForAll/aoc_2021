import math


class Pkg:

    def __init__(self, bits):
        self.version = int(bits[:3], 2)
        self.type_id = int(bits[3:6], 2)
        self.remaining = ''
        self.val = None
        self.sub_pkgs = []
        self._parse(bits)

    def _parse(self, bits):
        if self.type_id == 4:
            i = 6
            val = ''
            while bits[i] == '1':
                val += bits[i+1:i+5]
                i += 5
            self.val = int(val + bits[i+1:i+5], 2)
            self.remaining = bits[i+5:]
        else:
            self.length_type_id = int(bits[6], 2)
            if self.length_type_id == 0:
                sub_pkg_len = int(bits[7:22], 2)
                self.sub_pkgs = [Pkg(bits[22:22+sub_pkg_len])]

                while len(self.sub_pkgs[-1].remaining) != 0:
                    self.sub_pkgs.append(Pkg(self.sub_pkgs[-1].remaining))
                self.remaining = bits[22+sub_pkg_len:]
            elif self.length_type_id == 1:
                sub_pkg_cnt = int(bits[7:18], 2)
                remaining = bits[18:]
                for i in range(sub_pkg_cnt):
                    self.sub_pkgs.append(Pkg(remaining))
                    remaining = self.sub_pkgs[-1].remaining
                self.remaining = remaining

            sub_vals = [pkg.val for pkg in self.sub_pkgs]
            if self.type_id == 0:
                self.val = sum(sub_vals)
            elif self.type_id == 1:
                self.val = math.prod(sub_vals)
            elif self.type_id == 2:
                self.val = min(sub_vals)
            elif self.type_id == 3:
                self.val = max(sub_vals)
            elif self.type_id == 5:
                self.val = self.sub_pkgs[0].val > self.sub_pkgs[1].val
            elif self.type_id == 6:
                self.val = self.sub_pkgs[0].val < self.sub_pkgs[1].val
            elif self.type_id == 7:
                self.val = self.sub_pkgs[0].val == self.sub_pkgs[1].val


def main():
    with open('input.txt', 'r') as f:
        inp = f.read()
    inp = str(bin(int(inp, 16)))[2:].zfill(len(inp)*4)
    a = Pkg(inp)

    def sum_up(pkg: Pkg):
        if len(pkg.sub_pkgs) > 0:
            return pkg.version + sum([sum_up(p) for p in pkg.sub_pkgs])
        return pkg.version

    print(f'part a: {sum_up(a)}')
    print(f'part b: {a.val}')


if __name__ == '__main__':
    main()
