from itertools import permutations

def read_file(file):
    f = open("Day_8/mock.txt")
    data = f.readlines()
    f.close
    
    return data


def perm(data, display):
    counter = 0

    for line in data:
        digits, result = line.split(" | ")
        digits = digits.split()
        result = result.split()
    
        for permutation in permutations("abcdefg"):
            to = str.maketrans("abcdefg", "".join(permutation))

            a_ = ["".join(sorted(code.translate(to))) for code in digits]
            b_ = ["".join(sorted(code.translate(to))) for code in result]

            if all(code in display for code in a_):
                counter += int("".join(str(display[code]) for code in b_))
                break
    
    return counter


def main():
    
    data = read_file("Day_8/mock.txt")
    
    display_config = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }

    result = perm(data,display_config)
    print(result)
    

if __name__ == "__main__":
    main()