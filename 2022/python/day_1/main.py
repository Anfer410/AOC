test_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def read_input():
    with open('input.txt') as f:
        data = f.read()
    return data


def solve(item_list):
    elf_list = []
    item_cal_sum = 0
    
    for item in item_list:
        if item != '':
            item_cal_sum += int(item)
        else:
            elf_list.append(item_cal_sum)
            item_cal_sum = 0

    return elf_list


def main():    
    items_list = read_input().splitlines()
    elf_items = solve(items_list)
   
    # Part 1
    print(f'Part 1: {max(elf_items)}')

    # Part 2
    print(f'Part 2: {sum(sorted(elf_items, reverse=True)[:3])}')
    

if __name__ == '__main__':
    main()