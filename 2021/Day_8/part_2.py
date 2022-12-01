from itertools import permutations

with open("Day_8/mock.txt") as f:
    data = f.readlines()

display = {
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



part_1 = 0
part_2 = 0
for line in data:
    digits, result = line.split(" | ")
    digits = digits.split()
    result = result.split()
     
    part_1 += sum(len(code) in {2, 3, 4, 7} for code in result)
    for permutation in permutations("abcdefg"):
        to = str.maketrans("abcdefg", "".join(permutation))
        a_ = ["".join(sorted(code.translate(to))) for code in digits]
        b_ = ["".join(sorted(code.translate(to))) for code in result]
        
        print(a_)
        if all(code in display for code in a_):
            part_2 += int("".join(str(display[code]) for code in b_))
            break

print(part_1)
print(part_2)