import sys
from itertools import permutations

sys.path.append('../AOCUtils')
import utils

test_places_list = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

def calculate_distances(places_list):
    places = set()
    distances = dict()
    for line in places_list.splitlines():
        (source, _, dest, _, distance) = line.split()
        places.add(source)
        places.add(dest)
        distances.setdefault(source, dict())[dest] = int(distance)
        distances.setdefault(dest, dict())[source] = int(distance)
        print(distances)

    shortest = sys.maxsize
    longest = 0
    for items in permutations(places):
        dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
        shortest = min(shortest, dist)
        longest = max(longest, dist)

    print("shortest: %d" % (shortest))
    print("longest: %d" % (longest))


def main():
    test = False
    if test:
        calculate_distances(test_places_list)
    else:
        calculate_distances(utils.read_input(9))

         
if __name__ == "__main__":
    main()