import string
import time


test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def part_1(ruckstack, letters_priorities):
    start_time = time.perf_counter()
    ruckstack_sum = 0
    
    for items in ruckstack:
        common = ''
        items_part_1 = items[:int(len(items)/2)]
        items_part_2 = items[int(len(items)/2):]

        if len(items_part_1) != len(items_part_2):
            raise ValueError

        for item in [*items_part_1]:
            if item in items_part_2:
                common = item

        ruckstack_sum += letters_priorities[common]['prio']
    
    end_time = time.perf_counter()
    print(f'Part 1 execution time: {end_time - start_time} seconds')

    return ruckstack_sum


def part_2(rucksack_list, letters_priorities):
    start_time = time.perf_counter()
    priorities_sum = 0

    for i in range(0, len(rucksack_list)-2, 3):
        found = []
        elf_1_rucksack = rucksack_list[i]
        elf_2_rucksack = rucksack_list[i+1]
        elf_3_rucksack = rucksack_list[i+2]

        for badge in [*elf_1_rucksack]:
            if badge in elf_2_rucksack and badge in elf_3_rucksack and badge not in found:
                found.append(badge)

                priorities_sum += letters_priorities[badge]['prio']
    
    end_time = time.perf_counter()
    print(f'Part 2 execution time: {end_time - start_time} seconds')

    return priorities_sum


def letters_prio():
    letters_priorities = {}
    letters_list = [i for i in string.ascii_letters]
    for ix, letter in enumerate(letters_list):
        letters_priorities.update({letter:{'prio':ix+1}})
    
    return letters_priorities

    
def read_input():
    with open('input.txt') as f:
        file = f.read()
    return file


def main():
    # rucksack_list = test_input.splitlines()
    rucksack_list = read_input().splitlines()
    
    letters_priorities = letters_prio()
    print(f'Part 1: {part_1(rucksack_list, letters_priorities)}')
    print(f'Part 2: {part_2(rucksack_list, letters_priorities)}')


if __name__ == '__main__':
    main()
