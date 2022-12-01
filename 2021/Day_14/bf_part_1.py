from collections import Counter, defaultdict

with open('Day_14/input.txt', 'r') as f:
    polymer, insertion_rules = f.read().split('\n\n')
    pair_info = {}
    for char1, char2, *_, element in insertion_rules.split('\n'):
        pair_info[char1 + char2] = (element, char1 + element, element + char2)

def count_pairs(polymer):
    return Counter(''.join(pair) for pair in zip(polymer, polymer[1:]))

def count_elements(polymer):
    return Counter(polymer)

def create_new_polymer(pair_counts, element_counts):
    new_polymer = defaultdict(int)
    for pair, total in pair_counts.items():
        element, pair1, pair2 = pair_info[pair]
        element_counts[element] += total
        new_polymer[pair1] += total
        new_polymer[pair2] += total
    return new_polymer

def AOC_day14_pt_and_pt2(iterations):
    pair_counts = count_pairs(polymer)
    element_counts = count_elements(polymer)
    for _ in range(iterations):
        pair_counts = create_new_polymer(pair_counts, element_counts)
    totals = sorted(element_counts.values())
    return totals[-1] - totals[0]

print(AOC_day14_pt_and_pt2(iterations=10))
print(AOC_day14_pt_and_pt2(iterations=40))