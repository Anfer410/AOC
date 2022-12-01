def read_input(file):
    with open(file) as f:
        contents =f.read().strip().split('\n\n')
        return list(map(str , contents))

def fold_it(dots, axis, fold):
    return {(2*fold-x, y) if axis == 'x' and x > fold else
            (x, 2*fold-y) if axis == 'y' and y > fold else
            (x, y)
            for x, y in dots}


def grid2list(grid):
    max_x, max_y = map(max, zip(*grid))
    lines = [[' ' for ele in range(max_x+1)] for ele in range(max_y+1)]
    for x, y in grid:
        lines[y][x] = '#'
    return lines

def generate_code(dots,folds):
    for axis, fold in folds:
        dots = fold_it(dots,axis,fold)
    
    for line in grid2list(dots):
        print(''.join(line))


def main():
    dots, folds = map(str.splitlines, read_input("Day_13/input.txt"))    
    dots = [tuple(map(int,dot.split(",")) ) for dot in dots]
    
    
    folds  = [(line[11], int(line[13:])) for line in folds]
    
    print("Part 1: ",len(fold_it(dots,*folds[0])))

    print("Part 2:")
    generate_code(dots,folds)
    
    
    
if __name__ == "__main__":
    main()