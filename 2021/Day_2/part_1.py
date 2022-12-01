def read_input():
    data = []
    f = open('Day_2/input.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines: 
        data.append(line.replace('\n','').split(maxsplit=1))

    return data
    

def calculate_course(input):
    forward = 0
    depth = 0

    for move in range(len(input)):
        print("direction: ", input[move][0])
        if input[move][0] == "up":
            depth -= int(input[move][1])
        if input[move][0] == "down":
            depth += int(input[move][1])
        if input[move][0] == "forward":
            forward += int(input[move][1])
        
    print("forward: ", forward)
    print("depth: ", depth)
    print("total: ", forward * depth)



def main():
    data = read_input()
    calculate_course(data)



if __name__ == "__main__":
    main()