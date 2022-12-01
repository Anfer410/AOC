from collections import Counter
import sys
def read_input(file):
    with open(file) as f:
        contents =f.read().strip().split('\n\n')
        return list(map(str , contents))


def polimeryze(template,rules,steps):
    pair_frequencies = Counter()
    
    for pos in range(1, len(template)):
        pair = template[pos-1:pos+1]
        pair_frequencies[pair] += 1

    for _step in range(steps):
        pair_frequencies_step = Counter()
        for pair, frequency in pair_frequencies.items():
            if pair in rules:
                pair_frequencies_step[pair[0] + rules[pair]] += frequency
                pair_frequencies_step[rules[pair] + pair[1]] += frequency
        pair_frequencies = pair_frequencies_step
    
        char_frequencies = Counter()
        for pair, frequency in pair_frequencies.items():
            char_frequencies[pair[0]] += frequency
            char_frequencies[pair[1]] += frequency
        
        # include begining chars
        for char in char_frequencies:
            char_frequencies[char] //= 2
        char_frequencies[template[0]] += 1
        char_frequencies[template[-1]] += 1
    
    return max(char_frequencies.values()) - min(char_frequencies.values())


def main():
    template, rules = map(str.splitlines, read_input("Day_14/input.txt"))    
    template = template[0]
    rules = {left: right for left, right in (line.split(' -> ') for line in rules)}

    print(template)
    print("Part 1:", polimeryze(template,rules,10))
    print("Part 2:", polimeryze(template,rules,40))
    


if __name__ == "__main__":
    main()