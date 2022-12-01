input_file = 'input.txt'

test_case = '^v^v^v^v^v'
test_case_2 = '^^>>vv^^<<vv'

def read_instruction(file):
    with open(file) as f:
       text = f.read()
    return text

def deliver_present(pointer, direction, house_map):
    if direction == '^':
       pointer = (pointer[0], pointer[1] + 1)
    elif direction == 'v':
        pointer = (pointer[0], pointer[1] - 1)
    elif direction == '<':
        pointer = (pointer[0] - 1, pointer[1])
    elif direction == '>':
        pointer = (pointer[0] + 1, pointer[1])
    
    if pointer not in house_map:
        house_map.append(pointer)
    
    return pointer, house_map


def main():
    instruction = read_instruction(input_file)
    # instruction = test_case
    # instruction = test_case_2
    
    santa = True
    house_map_santa = [(0,0)]
    house_map_robo_santa = [(0,0)]
    
    house_map = [(0,0)]

    santa_xy = (0,0)
    robo_santa_xy = (0,0)

    for direction in instruction:
        if santa:
            santa_xy, house_map = deliver_present(santa_xy, direction, house_map)
        else:
            robo_santa_xy, house_map = deliver_present(robo_santa_xy, direction, house_map)
        
        santa = not santa
    
      
    
    # print(house_map)
    unique = len(house_map)
    print(unique)
    


if __name__ == '__main__':
    main()
