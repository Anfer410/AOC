
def read_input(file):
    data = []
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    
    for line in lines:
        input_output_list = []
        
        for elements in line.replace("\n","").split("|"):
            input_output_list.append(elements.split())
        data.append(input_output_list)
        
    return data


def main():
    # input = read_input("Day_8/input.txt")
    input = read_input("Day_8/mock.txt")
    counter = 0
    for inputs in range(len(input)):
        for digit in input[inputs][1]:
            # print(len(digit), " of ", digit)
            if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
                counter += 1 

    print(counter)






if __name__ == "__main__":
    main()