from collections import Counter

TEST = """3,4,3,1,2"""
INPUT = """1,3,4,1,1,1,1,1,1,1,1,2,2,1,4,2,4,1,1,1,1,1,5,4,1,1,2,1,1,1,1,4,1,1,1,4,4,1,1,1,1,1,1,1,2,4,1,3,1,1,2,1,2,1,1,4,1,1,1,4,3,1,3,1,5,1,1,3,4,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,5,2,5,5,3,2,1,5,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,1,1,1,1,5,1,1,1,1,1,4,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,3,1,2,4,1,5,5,1,1,5,3,4,4,4,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,5,3,1,4,1,1,2,2,1,2,2,5,1,1,1,2,1,1,1,1,3,4,5,1,2,1,1,1,1,1,5,2,1,1,1,1,1,1,5,1,1,1,1,1,1,1,5,1,4,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,4,5,1,1,1,1,1,1,1,5,1,1,3,1,1,1,3,1,4,2,1,5,1,3,5,5,2,1,3,1,1,1,1,1,3,1,3,1,1,2,4,3,1,4,2,2,1,1,1,1,1,1,1,5,2,1,1,1,2"""


"""Solutions from snakerjake:
for f in fish:
  fishstate[f] += 1

for _ in range(days):
    fishstate = fishstate[1:] + fishstate[:1]
    fishstate[7] += fishstate[0]
    
Solutions from joshbduncan:
tracker = [data.count(i) for i in range(9)]
    for day in range(days):
        tracker[(day + 7) % 9] += tracker[day % 9]
    return sum(tracker)
"""


def num_fish(pop_raw, days):
    count = Counter([int(age) for age in pop_raw.split(',')])
    fishes = [count.get(i, 0) for i in range(9)]

    for _ in range(days):
        mature_fish = fishes[0]
        fishes = fishes[1:] + fishes[:1]
        fishes[6] += mature_fish
    return sum(fishes)


"""Cohort-based also way too slow

class Cohort:
    def __init__(self, nb, age: int):
        self.nb = nb
        self.age = age

    def __str__(self):
        return f"Cohort of {self.nb} fish age {self.age}"

    def advance(self):
        self.age -= 1
        if self.age == -1:
            self.age = 6
            return Cohort(int(self.nb), 8)
        return None


class School:
    def __init__(self, cohorts: List[Cohort]):
        self.cohorts = list(cohorts)

    def advance(self):
        cur_cohorts = list(self.cohorts)
        for cohort in cur_cohorts:
            new_coh = cohort.advance()
            if new_coh:
                self.cohorts.append(new_coh)

    def __len__(self):
        return sum(coh.nb for coh in self.cohorts)

    def __str__(self):
        return '\n'.join(str(coh) for coh in self.cohorts)


def num_fish(pop_raw, days):
    t0 = time.perf_counter()

    all_cohorts = []
    age_counter = Counter(int(age) for age in pop_raw.split(','))
    for i in range(9):
        cohort = Cohort(age_counter.get(i, 0), i)
        all_cohorts.append(cohort)
    school = School(all_cohorts)
    for day in range(days):
        school.advance()

    print(time.perf_counter() - t0)
    return len(school)

Naive attempt below

class School:
    def __init__(self, fish_ages_raw):
        self.gang = []
        for age in fish_ages_raw.split(','):
            self.gang.append(Fish(int(age)))

    def age_all(self):
        for fish in self.gang:
            fish.age -= 1
        fish_maturing = [fish for fish in self.gang if fish.age == -1]
        self.gang.extend(Fish() for _ in range(len(fish_maturing)))
        for fish in fish_maturing:
            fish.age = 6

    def age_all_old(self):
        gang = list(self.gang)  # Done to not have list size change when spawning
        for fish in gang:
            fish.age -= 1
            if fish.age == -1:
                fish.age = 6
                self.gang.append(Fish())

    def __len__(self):
        return len(self.gang)

    def __str__(self):
        return ','.join(str(fish.age) for fish in self.gang)


class Fish:
    def __init__(self, start_age: int = 8):
        self.age = start_age


def num_fish(pop_raw, days):
    t0 = time.perf_counter()
    school = School(pop_raw)
    for day in range(days):
        school.age_all()
    print(time.perf_counter() - t0)
    return len(school)"""


##########################
if __name__ == '__main__':
    assert num_fish(TEST, 18) == 26
    assert num_fish(TEST, 80) == 5934
    assert num_fish(INPUT, 80) == 390011
    assert num_fish(TEST, 256) == 26984457539
    assert num_fish(INPUT, 256) == 1746710169834
