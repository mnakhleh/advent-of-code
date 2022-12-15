from data.day15 import SAMPLE_TXT, INPUT_TXT
from dataclasses import dataclass
from typing import Iterable
from itertools import combinations, chain
import re


SCANNED = '#'


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def part1(raw: str, check_row: int) -> int:
    sensor_beacon_pairs = [parse_line(line) for line in raw.splitlines()]

    scanned = dict()
    for sensor, beacon in sensor_beacon_pairs:
        # Feels like this should fail as update() can overwrite a Beacon / Sensor into a Scanned... but it doesn't!
        # Also, passing along the previously scanned dict takes like 50% longer to solve!!
        scanned.update(get_scanned_area(sensor, beacon, check_row=check_row))

    return sum([1 for point in scanned if point.y == check_row and scanned[point] == SCANNED])


def part2(raw: str, max_row: int) -> int:
    # Inspired by a comment about the answer being just outside of at least 2 scans to reduce the inspection space
    sensor_beacon_pairs = [parse_line(line) for line in raw.splitlines()]
    bounding_boxes = [get_bounding_box(sensor, beacon) for sensor, beacon in sensor_beacon_pairs]
    for intersection in get_intersections(bounding_boxes):
        if is_outside_scans(intersection, sensor_beacon_pairs, max_row):
            return intersection.x * 4000000 + intersection.y


def parse_line(line: str) -> tuple[Point, Point]:
    vals = re.split(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
    return Point(int(vals[1]), int(vals[2])), Point(int(vals[3]), int(vals[4]))


def get_scanned_area(sensor: Point, beacon: Point, check_row: int) -> dict[Point, str]:
    scanned = dict()
    distance = get_distance(sensor, beacon)
    for x in range(sensor.x - distance, sensor.x + distance + 1):
        if check_row not in range(sensor.y - distance, sensor.y + distance + 1):
            continue
        if get_distance(Point(x, check_row), sensor) <= distance:
            scanned[Point(x, check_row)] = SCANNED

    scanned.update({sensor: 'S', beacon: 'B'})
    return scanned


def get_distance(point1: Point, point2: Point) -> int:
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)


def get_bounding_box(sensor: Point, beacon: Point) -> list[Point]:
    distance = get_distance(sensor, beacon) + 1
    all_points = [[Point(sensor.x + x_delta, sensor.y + (distance - x_delta)),
                   Point(sensor.x + x_delta, sensor.y - (distance - x_delta)),
                   Point(sensor.x - x_delta, sensor.y + (distance - x_delta)),
                   Point(sensor.x - x_delta, sensor.y - (distance - x_delta))] for x_delta in range(distance)]
    return list(chain.from_iterable(all_points))


def get_intersections(bounding_boxes: list[list[Point]]) -> Iterable[Point]:
    for box1, box2 in combinations(bounding_boxes, 2):
        for intersection in set(box1) & set(box2):
            yield intersection


def is_outside_scans(point: Point, sensor_beacon_pairs: list[tuple[Point, Point]], max_row: int) -> bool:
    if not (0 <= point.x <= max_row and 0 <= point.y <= max_row):
        return False
    for beacon, sensor in sensor_beacon_pairs:
        beacon_sensor_distance = get_distance(beacon, sensor)
        if get_distance(point, beacon) <= beacon_sensor_distance:
            return False
    return True


##########################
if __name__ == '__main__':
    assert part1(SAMPLE_TXT, 10) == 26
    print(part1(INPUT_TXT, 2000000))
    assert part2(SAMPLE_TXT, 20) == 56000011
    print(part2(INPUT_TXT, 4000000))
