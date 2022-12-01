instruction_file = 'input.txt'


def read_instruction(file):
    with open(file) as f:
       text = f.read()
    return text

def floor_decryptor(instruction, part2 = False):
    #  part 1
    floor = 0
    basement_trigger = 0
    for index, character in enumerate(instruction):
        if character == '(':
            floor = floor + 1
        elif character == ')':
            floor = floor -1
        
        print(character, floor)
    if part2 == True:
        # Part 2
        if floor < 0 :
            basement_trigger = index + 1  # Add 1 because index starts from 0 and you need character number
            return floor, basement_trigger
    
    return floor, basement_trigger



def main():
    instruction = read_instruction(instruction_file)
    floor, basement_trigger = floor_decryptor(instruction)
    print(floor, basement_trigger)


if __name__ == '__main__':
    main()