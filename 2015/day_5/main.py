import sys
import re

sys.path.append('../AOCUtils')
import utils

day = 5

def good_or_naughty(string, part):
    if part == 1:
        if len(re.findall('[aeiou]', string)) > 2:
            if re.search(r'(\w)(\1)', string):
                if not re.search(r'ab|cd|pq|xy', string):
                    return True                   
    
    if part == 2:
        if re.search(r'(\w)(\w).*(\1)(\2)', string):
            if re.search(r'(\w)(\w)(\1)', string):
                return True
        
    return False


def tests(part=1):
    if part == 1:
        test_1 = 'ugknbfddgicrmopn'  # Nice
        test_2 = 'jchzalrnumimnmhp'  # Naughty
        test_3 = 'haegwjzuvuyypxyu'  # Naughty
        test_4 = 'dvszwmarrgswjxmb'  # Naughty
        test = [test_1, test_2, test_3, test_4]
    if part == 2:
        test_1 = 'qjhvhtzxzqqjkmpb'  # Nice
        test_2 = 'xxxyxxx'           # Nice
        test_3 = 'uurcxstgmygtbstg'  # Naughty
        test_4 = 'ieodomkazucvgmuy'  # Naughty
        # test = [test_1, test_2, test_3, test_4]
        test = [test_1]

    return test


def main(part=1, test=False):
    print(f'Part: {part}')
    
    if test: 
        strings = tests(part)
    else:
        strings = utils.read_input(5, 'l')
    
    nice_counter = 0
    
    for string in strings:
        is_nice = good_or_naughty(string, part)
        if is_nice:
            nice_counter += 1

    print(f'Nice strings: {nice_counter}')
    


    
if __name__ == '__main__':
    main(part=1)
    main(part=2)