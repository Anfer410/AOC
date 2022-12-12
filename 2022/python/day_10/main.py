from queue import Queue

test_input= """noop
addx 3
addx -5"""

with open('input.txt') as f:
    file = f.read()

x = 1
cycle_counter = 1
sprite_counter = 0
command_i = 0

command_q = Queue()
commands = file.splitlines()
signal_strenght = []
next_cycle_readout = 60

line_1 = ['.' for i in range(40)]
line_2 = ['.' for i in range(40)]
line_3 = ['.' for i in range(40)]
line_4 = ['.' for i in range(40)]
line_5 = ['.' for i in range(40)]
line_6 = ['.' for i in range(40)]


while len(commands)-1 != command_i:
    # set current sprite position
    sprite = [x - 1, x, x + 1]
    
    # Line 1 cycle 1 to cycle 40
    if cycle_counter >= 0 and cycle_counter <= 40:
        if sprite_counter in sprite:
            line_1[sprite_counter] ='#'
    
    # Line 2 cycle 41 to cycle 80
    if cycle_counter >= 41 and cycle_counter <= 80:
        if sprite_counter in sprite:
            line_2[sprite_counter] ='#'
    
    # Line 3 cycle 81 to cycle 120
    if cycle_counter >= 81 and cycle_counter <= 120:
       if sprite_counter in sprite:
            line_3[sprite_counter] ='#'
    
    # Line 4 cycle 121 to cycle 160
    if cycle_counter >= 121 and cycle_counter <= 160:
        if sprite_counter in sprite:
            line_4[sprite_counter] ='#'
        
    # Line 5 cycle 161 to cycle 200
    if cycle_counter >= 161 and cycle_counter <= 200:
      if sprite_counter in sprite:
            line_5[sprite_counter] ='#'
        
    # Line 6 cycle 201 to cycle 240
    if cycle_counter >= 201 and cycle_counter <= 240:
        if sprite_counter in sprite:
            line_6[sprite_counter] ='#'

    # Calculate signal strength
    if cycle_counter == 20:
        signal_strenght.append(cycle_counter * x)
        
    if cycle_counter == next_cycle_readout:
        signal_strenght.append(cycle_counter * x)
        next_cycle_readout += 40
    
    # Check for next command in queue
    if not command_q.empty():
        # use cycle to execute command
        item = command_q.get()
        x += item

    # if no items in queue check commands
    elif 'addx' in commands[command_i]:
        # read command
        c, i = commands[command_i].split()
        command_q.put(int(i))
        command_i += 1
    else:
        # use cycle
        command_i += 1
    
    # update counters
    if sprite_counter == 39:
        sprite_counter = 0
    else:
        sprite_counter += 1
    
    cycle_counter += 1
    


print(f'Part 1: {sum(signal_strenght)}')

print('Part 2:')
print(''.join(line_1))
print(''.join(line_2))
print(''.join(line_3))
print(''.join(line_4))
print(''.join(line_5))
print(''.join(line_6))


