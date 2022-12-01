instruction_file = 'input.txt'

def read_instructions(file):
    with open(file) as f:
        lines = f.readlines()
    text = []
    for line in lines:
        text.append(line.strip())
    return text

# l w h
# 2*l*w + 2*w*h + 2*h*l
def main():
    instructions = read_instructions(instruction_file)
    # instructions = ['2x3x4']

    total = 0
    total_bow = 0
    for line in instructions:
        l = int(line[:line.find("x")])
        w = int(line[line.find("x")+1:line.rfind("x")])
        h = int(line[line.rfind("x")+1:])

        side_1 = l*w
        side_2 = w*h
        side_3 = h*l

        extra = min(side_1, side_2, side_3)

        total += 2*side_1 + 2*side_2 + 2*side_3 + extra

        # Part 2 - ribbon
        rib_a = sorted([l,w,h])[0]
        rib_b = sorted([l,w,h])[1]
        total_bow += rib_a + rib_a + rib_b + rib_b + l*w*h




        

    print(f"paper: {total}")
    print(f"ribbon: {total_bow}")
        


if __name__ == '__main__':
    main()