from copy import deepcopy


def add(x, y):
    return reduce([x, y])


def reduce(root):
    root = deepcopy(root)

    while action(root):
        pass

    return root

def action(root):
    pair_left, i_left = None, None
    pair_right, i_right = None, None
    pair_split, i_split = None, None

    stack = [(0, [root,  None], 0)]

    while stack:
        depth, pair, i = stack.pop()

        if isinstance(pair[i], int):
            # keep track of where to split if we don't end up exploding
            if not pair_split and pair[i] >= 10:
                pair_split, i_split = pair, i

            # keep track of most recent regular number (i.e. left of exploded number)
            pair_left, i_left = pair, i
        else:
            if depth >= 4:
                # keep iterating until the next regular number (i.e. right of exploded number)
                if stack:
                    _, pair_right, i_right = stack.pop()
                    while isinstance(pair_right[i_right], list):
                        pair_right, i_right = pair_right[i_right], 0

                # perform explode
                if pair_left:
                    pair_left[i_left] += pair[i][0]
                if pair_right:
                    pair_right[i_right] += pair[i][1]
                pair[i] = 0

                return True
            else:
                # push child numbers onto the stack
                stack.append((depth + 1, pair[i], 1))
                stack.append((depth + 1, pair[i], 0))

    # perform split
    if pair_split:
        pair_split[i_split] = [pair_split[i_split] // 2, (pair_split[i_split] + 1) // 2]
        return True

    return False


    
def magnitude(a):
    if isinstance(a,int):
        return(a)
    else:
        return 3 * magnitude(a[0]) + 2 * magnitude(a[1])


        
def main():
    with open("Day_18/input.txt") as f:
        numbers = [eval(line) for line in f.readlines()]

    # part 1
    x = numbers[0]
    for y in numbers[1:]:
        x = add(x, y)

    print(magnitude(x))

    # part 2
    max_magnitude = 0
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            if i == j:
                continue
            max_magnitude = max(max_magnitude, magnitude(add(a, b)))

    print(max_magnitude)





if __name__ == "__main__":
    main()