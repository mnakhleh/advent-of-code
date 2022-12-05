import re
import itertools
TEST = """target area: x=20..30, y=-10..-5"""
INPUT = """target area: x=150..193, y=-136..-86"""


class Probe:
    def __init__(self, x_vel, y_vel):
        self.x_cur, self.y_cur = 0, 0
        self.x_vel, self.y_vel = x_vel, y_vel
        self.cache_pos = []

    def step(self):
        self.x_cur += self.x_vel
        self.y_cur += self.y_vel
        self.x_vel = self.x_vel - 1 if self.x_vel > 0 else 0
        self.y_vel -= 1
        self.cache_pos.append((self.x_cur, self.y_cur))

    def check_hit(self, x_min, x_max, y_min, y_max):
        if x_min <= self.x_cur <= x_max and y_min <= self.y_cur <= y_max:
            # print(self.cache_pos)
            max_height = max(y for x,y in self.cache_pos)
            return "HIT", max_height
        elif self.x_cur > x_max or self.y_cur < y_min:
            return "MISSED", None
        return "-", None


def main(text):
    matches = re.match(r'target area: x=(\d+)\.\.(\d+), y=(-?\d+)\.\.(-?\d+)', text)
    xmin, xmax, ymin, ymax = [int(v) for v in matches.groups()]

    values_to_try = [p for p in itertools.product(range(-300, 300), repeat=2)]
    probes = [Probe(x, y) for x, y in values_to_try]
    all_heights = [max_height(probe, (xmin, xmax, ymin, ymax)) for probe in probes]
    real_heights = [hgt for hgt in all_heights if hgt != -1000]
    overall_max_height = max(real_heights)
    return len(real_heights), overall_max_height


def max_height(probe, solution_box):
    xmin, xmax, ymin, ymax = solution_box

    while 1:
        probe.step()
        probe_status, height = probe.check_hit(xmin, xmax, ymin, ymax)
        if probe_status == 'HIT':
            return height
        elif probe_status == 'MISSED':
            return -1000


##########################
if __name__ == '__main__':
    print(main(TEST))
    print(main(INPUT))
