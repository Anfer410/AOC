import time


test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def read_input():
    with open('input.txt') as f:
        file = f.read()
    
    return file


def main():
    # big_list = test_input.splitlines()

    big_list = read_input().splitlines()
    
    start_time = time.perf_counter()
    
    counter_all = 0
    counter_any = 0
    for zone in big_list:
        zone_1_short, zone_2_short = zone.split(',')
        zone_1_start, zone_1_end = zone_1_short.split('-')
        zone_2_start, zone_2_end = zone_2_short.split('-')

        zone_1 = [point for point in range(int(zone_1_start), int(zone_1_end) + 1)]
        zone_2 = [point for point in range(int(zone_2_start), int(zone_2_end) + 1)]        
        
        if all([item in zone_1 for item in zone_2]) or all([item in zone_2 for item in zone_1]):
            counter_all += 1
        elif any([item in zone_1 for item in zone_2]) or any([item in zone_2 for item in zone_1]):
            counter_any += 1

    
    end_time = time.perf_counter()
    
    print(f'Task execution time: {end_time - start_time} seconds')
    print(f'Part 1: {counter_all}')  
    print(f'Part 2: {counter_all + counter_any}')  


if __name__ == '__main__':
    main()