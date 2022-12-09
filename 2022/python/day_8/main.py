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


def find_neighbours(arr, trees):

    potentials = {}
    for tree_pos in trees:
        potentials.update({tree_pos:{}})
        
        # look up 
        view = []
        tall_tree = arr[tree_pos[0]][tree_pos[1]]
        
        for i in reversed(range(0, tree_pos[0])):
            if arr[i][tree_pos[1]] < tall_tree or arr[i][tree_pos[1]] > tall_tree:
                view.append(arr[i][tree_pos[1]])
                if arr[i][tree_pos[1]] >= tall_tree:
                    tall_tree = arr[i][tree_pos[1]]
            elif arr[i][tree_pos[1]] == tall_tree:
                view.append(arr[i][tree_pos[1]])
                break
        
        potentials[(tree_pos)].update({'up':view})
        
        # look down
        view = []
        tall_tree = arr[tree_pos[0]][tree_pos[1]]
        for i in range(tree_pos[0]+1, len(arr)):
            if arr[i][tree_pos[1]] < tall_tree or arr[i][tree_pos[1]] > tall_tree:
                view.append(arr[i][tree_pos[1]])
                if arr[i][tree_pos[1]] >= tall_tree:
                    tall_tree = arr[i][tree_pos[1]]
            elif arr[i][tree_pos[1]] == tall_tree:
                view.append(arr[i][tree_pos[1]])
                break
        potentials[tree_pos].update({'down':view})

        # look right
        view = []
        tall_tree = arr[tree_pos[0]][tree_pos[1]]
        for i in range(tree_pos[1]+1,len(arr[tree_pos[0]])):
            
            if arr[tree_pos[0]][i] < tall_tree or arr[tree_pos[0]][i] > tall_tree:
                view.append(arr[tree_pos[0]][i])
                if arr[tree_pos[0]][i] >= tall_tree:
                    tall_tree = arr[tree_pos[0]][i]
            elif arr[tree_pos[0]][i] == tall_tree:
                view.append(arr[tree_pos[0]][i])
                break
        
        potentials[tree_pos].update({'right':view})

        # look left
        view = []
        tall_tree = arr[tree_pos[0]][tree_pos[1]]
        for i in reversed(range(0, tree_pos[1])):
            if arr[tree_pos[0]][i] < tall_tree or arr[tree_pos[0]][i] > tall_tree:
                view.append(arr[tree_pos[0]][i])
                if arr[tree_pos[0]][i] >= tall_tree:
                    tall_tree = arr[tree_pos[0]][i]
            elif arr[tree_pos[0]][i] == tall_tree:
                view.append(arr[tree_pos[0]][i])
                break
        
        potentials[tree_pos].update({'left':view})
            
    return potentials


def main():
    # input = test_input.splitlines()
    input = read_input().splitlines()
    
    forest = []
    
    for line in input:
        forest.append([int(value) for value in line.replace('\n','')])
    
    visible_trees = look_at_trees(forest)
    
    # for i in range(len(forest)):
    #     char = ''
    #     for j in range(len(forest)):
    #         if (i,j) in visible_trees or i == 0 or j==0 or i == len(forest)-1 or j==len(forest[i])-1:
    #             char += str(forest[i][j])
    #         else:
    #             char += '#'
    #     print(char)
    
    size = len(forest[0])*2 + len(forest) *2 - 4
    print(f'Part 1: {size + len(visible_trees)}')

    pot_spots = find_neighbours(forest, visible_trees)
    
    weight = []

    for spot in pot_spots:
        weight.append(len(pot_spots[spot]['left']) * len(pot_spots[spot]['up']) * len(pot_spots[spot]['down']) * len(pot_spots[spot]['right']))
        
    # print(weight)
    print(f'Part 2: {sorted(weight, reverse=True)[0]}')

if __name__ == "__main__":
    main()