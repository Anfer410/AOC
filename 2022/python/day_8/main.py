from os import read

test_input = """30373
25512
65332
33549
35390"""


def read_input():
    with open('input.txt') as f:
        lines = f.read()
    return lines    


def look_at_trees(forest):

    visible = set()
    # from left to right
    for i in range(1, len(forest)-1):
        hihest_tree = forest[i][0]
        for j in range(1,len(forest)-1):            
            if forest[i][j] > hihest_tree:
                hihest_tree = forest[i][j]
                if (i,j) not in visible:
                    visible.add((i,j))

    # from right to left
    for i in range(1, len(forest)-1):
        hihest_tree = forest[i][len(forest)-1]
        for j in reversed(range(1,len(forest)-1)):
            
            if forest[i][j] > hihest_tree:
                hihest_tree = forest[i][j]
                if (i,j) not in visible:
                    visible.add((i,j))
    
    # from top to bottom
    for j in range(1, len(forest)-1):
        hihest_tree = forest[0][j]
        for i in range(1,len(forest)-1):
            if forest[i][j] > hihest_tree:
                hihest_tree = forest[i][j]
                if (i,j) not in visible:
                    visible.add((i,j))
    
    #  from bottom to top
    for j in range(1, len(forest)-1):
        hihest_tree = forest[len(forest)-1][j]
        for i in reversed(range(1,len(forest)-1)):
            if forest[i][j] > hihest_tree:
                hihest_tree = forest[i][j]
                if (i,j) not in visible:
                    visible.add((i,j))

    return visible


def main():
    input = read_input().splitlines()
    # input = test_input.splitlines()
    
    forest = []
    
    for line in input:
        forest.append([int(value) for value in line.replace('\n','')])
    
    neighbours = look_at_trees(forest)
    
    for i in range(len(forest)):
        char = ''
        for j in range(len(forest)):
            if (i,j) in neighbours or i == 0 or j==0 or i == len(forest)-1 or j==len(forest[i])-1:
                char += str(forest[i][j])
            else:
                char += '#'
        print(char)
    
    size = len(forest[0])*2 + len(forest) *2 - 4
    print(f'Part 1: {size + len(neighbours)}')


if __name__ == "__main__":
    main()