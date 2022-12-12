test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

class Rope():
    def __init__(self):
        self.head = [0,0]
        self.tail = [0,0]
        self.head_positions = set()
        self.tail_positions = set()

    def move(self, direction, steps):

        for step in range(steps):
            y, x = self.head
            
            if direction == 'U':
                y -= 1
            if direction == 'D':
                y += 1
            if direction == 'R':
                x += 1
            if direction == 'L':
                x -= 1
            
            self.head = [y,x]
            self.head_positions.add(tuple(self.head))

            self.update_tail(direction)

    def update_tail(self, direction):
        hy, hx = self.head
        ty, tx = self.tail
        
        if direction == 'U' or direction == 'D':
            # head moves up
            if hy < ty - 1:
                if tx != hx:
                    tx = hx
                ty -= 1        
            # head moves down
            elif hy > ty + 1:
                if tx != hx:
                    tx = hx
                ty += 1
        if direction == 'R' or direction == 'L':
            # head moves right
            if hx > tx + 1:
                if ty != hy:
                    ty = hy
                tx += 1
            # head moves left
            elif hx < tx - 1:
                if ty != hy:
                    ty = hy
                tx -= 1
        
        self.tail = [ty, tx]
        self.tail_positions.add(tuple(self.tail))

    def draw_path_tail(self):
        for i in range(-6,6):
            line = []
            for j in range(-6,6):
                if (i,j) in self.tail_positions: 
                    line.append('T')
                else:
                    line.append('.')
            print(''.join(line))
    
    def draw_path_head(self):
        for i in range(-6,6):
            line = []
            for j in range(-6,6):
                if (i,j) in self.head_positions: 
                    line.append('H')
                else:
                    line.append('.')
            print(''.join(line))


def read_input():
    with open('input.txt') as f:
        file = f.read()
    return file


rope = Rope()
steps = read_input().splitlines()
# steps = test_input.splitlines()

for line in steps:
    direction, num_of_steps = line.split(' ')
    rope.move(direction, int(num_of_steps))

# rope.move('R', 4)
# rope.move('U', 4)
# rope.move('L', 4)
# rope.move('D', 4)

# print(sorted(rope.head_positions))
# print(len(rope.head_positions))
# print(sorted(rope.tail_positions))
print(len(rope.tail_positions))

# rope.draw_path_head()
# rope.draw_path_tail()