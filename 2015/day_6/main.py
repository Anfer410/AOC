import sys

sys.path.append('../AOCUtils')
import utils

# Variables
rows = 1000
cols = 1000


def init_grid(rows=rows, cols=cols):
   return [[0 for c in range(cols)] for r in range(rows)]

def read_command(text):
    return str(text).replace("turn ","").split()
    

def execute_command(command: str, grid, part=1):
    action = command[0]
    range_start = command[1].split(",")
    range_end = command[3].split(",")

    for row_i, row in enumerate(grid):
        if row_i >= int(range_start[0]) and row_i <= int(range_end[0]):
            for col_i, col in enumerate(grid[row_i]):            
                if col_i >= int(range_start[1]) and col_i <= int(range_end[1]):
                    if action == 'on':
                        if part == 1:
                            grid[row_i][col_i] = 1
                        else:
                            grid[row_i][col_i] += 1

                    if action == 'off':
                        if part == 1:
                            grid[row_i][col_i] = 0
                        else:
                            if grid[row_i][col_i] > 0:
                                grid[row_i][col_i] -= 1

                    if action == 'toggle':
                        if part == 1:
                            if grid[row_i][col_i] == 1:
                                grid[row_i][col_i] = 0
                            else: 
                                grid[row_i][col_i] = 1
                        else:
                            grid[row_i][col_i] += 2

    return grid


def count_ligths(grid, part=1):
    counter = 0
    for ix, i in enumerate(grid):
        for jx, j in enumerate(grid[ix]):
            counter += grid[ix][jx]
    print(f'Part {part} - Lit leds number: {counter}')


def main():
    instructions = utils.read_input(6, 'l')
    
    led_grid = init_grid()
    # grid_read(led_grid)

    for part in [1,2]:
        for ix, i in enumerate(instructions):
            command = read_command(i)
            led_grid = execute_command(command, led_grid, part)
            # grid_read(led_grid)
    
        count_ligths(led_grid, part)

    


if __name__ == '__main__':
    main()