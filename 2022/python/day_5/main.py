from collections import deque
import time

test_input ="""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def transform_stack(crates_stacks):
    index = crates_stacks[len(crates_stacks)-1].split()
    crates_stacks = [crates_stacks[i] for i in range(len(crates_stacks)-1)]  # remove index 

    stacks = []
    curr = 0
    
    for i in range(len(index)):
        stack = deque()
        for l in crates_stacks:
            letter = l[curr + 1:curr + 2]
            if letter != ' ':
                stack.appendleft(letter)
        curr += 4
        stacks.append(stack)
    
    return stacks 
    

def move_crates(crates, instructions, part=1):
    start_time = time.perf_counter()
    crates_stack = crates.splitlines()
    vertical_stacks = transform_stack(crates_stack)   
    
    for instruction in instructions.splitlines():
        inst = instruction.split(' ')
        
        n_of_crates = int(inst[1])
        original_stack = int(inst[3]) - 1
        new_stack = int(inst[5]) - 1

        if n_of_crates > 1 and part != 1:
            temp_queue = deque()
            for i in range(n_of_crates):
                if vertical_stacks[original_stack]:
                    temp_queue.append(vertical_stacks[original_stack].pop())
            
            for i in range(n_of_crates):
                if temp_queue:
                    vertical_stacks[new_stack].append(temp_queue.pop())
        else:
            for i in range(n_of_crates):
                if vertical_stacks[original_stack]:
                    vertical_stacks[new_stack].append(vertical_stacks[original_stack].pop())

    word = ''.join([vertical_stacks[i][-1] for i in range(len(vertical_stacks))])
    end_time = time.perf_counter()
    print(f'Part {part}: {end_time - start_time} seconds')
    return word


def read_input():
    with open('input.txt') as f:
        file = f.read()
    
    return file


def main():
    crates, instructions = \
        test_input.split('\n\n')

    crates, instructions = read_input().split('\n\n')

    print(f'Part 1: {move_crates(crates, instructions, 1)}')
    print(f'Part 2: {move_crates(crates, instructions, 2)}')
  

if __name__ == '__main__':
    main()