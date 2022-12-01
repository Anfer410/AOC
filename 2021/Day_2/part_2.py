def read_input():
    data = []
    f = open('Day_2/input.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines: 
        data.append(line.replace('\n','').split(maxsplit=1))

    return data
    
def calculate_course(input):
    horizontal = 0
    depth = 0
    aim = 0

    for move in range(len(input)):
        print("command ",input[move][0], " ", int(input[move][1]))
        if input[move][0] == "down": 
            aim += int(input[move][1])
            print("aim increased, ", aim)
        
        if input[move][0] == "up": 
            aim -= int(input[move][1])
            print("aim decreased, ", aim)
       
        if input[move][0] == "forward": 
            horizontal += int(input[move][1])
            print("moving forward: ", horizontal)
            print("adjust depth: ", depth, " + ", aim, " * ", int(input[move][1]))
            depth = depth + (aim * int(input[move][1]))
            print(depth)

    print("forward: ", horizontal)
    print("depth: ", depth)
    print("total: ", horizontal * depth)


def main():
    data = read_input()
    calculate_course(data)



if __name__ == "__main__":
    main()