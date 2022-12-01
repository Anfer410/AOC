def read_input(file):
    data = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        data.append(line.replace('\n',''))
    f.close()
    return data


def find_corrupted_chunks(data):
    open_brackets = []
    
    dict = {
        40:41,
        91:93,
        123:125,
        60:62,
        41:40,
        93:91,
        125:123,
        62:60,
    }

    illegal_chars = []
    for line in data:
        brackets = []
        
        status = False 
        print("verifying line: ", line)
        for char in line:

            if char in ["(","[","{","<"]:
                brackets.append(char)
            
            if char in [")","]","}",">"]:
                if char.translate(dict) == brackets[len(brackets)-1]:
                    del brackets[len(brackets)-1]
                else:
                    print("line_corrupted")
                    print("illegal character: ",char)
                    illegal_chars.append(char)
                    status = True
                    break
            
        if status: 
            print(line) 
        else: 
            open_brackets.append(brackets)


    points = []
    for line in open_brackets:
        auto_complete = []
        for bracket in reversed(line):
            auto_complete.append(bracket.translate(dict))
        
        point = autocomplete_contest_points(auto_complete)
        points.append(point)
        print(auto_complete, " : ", point)

    
    middleIndex = (len(points) - 1)/2
    points.sort()
    print("Solve: ", points[int(middleIndex)])
    
            
    return illegal_chars, open_brackets
        

def autocomplete_contest_points(missing_brackets_list):
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    sum = 0
    for char in missing_brackets_list:
        sum = (sum * 5) +  points[char]
    
    return sum

 

def main():
    input = read_input("Day_10/input.txt")
    # input = read_input("Day_10/input.txt")
    print(input)
    open_brackets,illegal_chars_list = find_corrupted_chunks(input)
    





if __name__ == '__main__':
    main()