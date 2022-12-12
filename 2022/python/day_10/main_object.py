class Processor():
    def __init__(self):
        self.cycle = 1
        self.x = 1
        self.memory = []
        self.signal_strenght = []
        
        # display init
        self.spirte_cycle = 0
        self.display = [['.' for i in range(40)] for y in range(6)]

    def calculate_signal_strenght(self):
        self.signal_strenght.append(self.cycle * self.x)
        return self.cycle + 40
    
    def update_display_line(self):
        # Select line
        if self.cycle >= 0 and self.cycle <= 40:
            self.display_line = 0
        if self.cycle >= 41 and self.cycle <= 80:
            self.display_line = 1
        if self.cycle >= 81 and self.cycle <= 120:
            self.display_line = 2
        if self.cycle >= 121 and self.cycle <= 160:
            self.display_line = 3
        if self.cycle >= 161 and self.cycle <= 200:
            self.display_line = 4
        if self.cycle >= 201 and self.cycle <= 240:
            self.display_line = 5
        
    def update_sprite_pos(self):
        self.sprite_pos = [self.x - 1, self.x, self.x + 1]
            
    def update_pixel(self):
        if self.spirte_cycle in self.sprite_pos:
            self.display[self.display_line][self.spirte_cycle] ='#'
    
    def update_display(self):
        self.update_sprite_pos()
        self.update_display_line()
        self.update_pixel()
        
        if self.spirte_cycle == 39:
            self.spirte_cycle = 0
        else:
            self.spirte_cycle += 1
    
    def run(self, commands):
        command_i = 0
        next_cycle_readout = 20
        while len(commands)-1 != command_i:
            self.update_display()

            # Calculate signal strength
            if self.cycle == next_cycle_readout:
                next_cycle_readout = self.calculate_signal_strenght()

            # Check for next command in queue
            if len(self.memory) != 0:
                # use cycle to execute command
                item = self.memory.pop()
                self.x += item

            # if no items in queue check commands
            elif 'addx' in commands[command_i]:
                # read command
                i = commands[command_i].split()[1]
                self.memory.append(int(i))
                command_i += 1
            else:
                # use cycle
                command_i += 1
            
            self.cycle += 1


test_input= """noop
addx 3
addx -5"""


def read_input():
    with open('input.txt') as f:
        file = f.read()
    
    return file


def main():
    processor = Processor()
    processor.run(read_input().splitlines())

    print(f'Part 1: {sum(processor.signal_strenght)}')
    print('Part 2:')
    for line in processor.display:
        print(''.join(line))


if __name__ == '__main__':
    main()