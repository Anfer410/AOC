def read_input(file):
    data = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        data.append(line.replace('\n',''))
    f.close()
    return data


def find_corrupted_chunks(data):
    valid_lines = []
    
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
        
        if status: print(line) 
    return illegal_chars
        

            
def test():
    
        
    counter_open = {
            "(": 0,
            "[": 0,
            "{": 0,
            "<": 0,
        }
    counter_close = {
            ")": 0,
            "]": 0,
            "}": 0,
            ">": 0
        }

    
def contest_points(illegal_character_list):
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    sum = 0
    for char in illegal_character_list:
        sum += points[char]
    
    print(sum)



def main():
    # input = read_input("Day_10/mock.txt")
    input = read_input("Day_10/input.txt")
    print(input)
    illegal_chars_list = find_corrupted_chunks(input)
    print(illegal_chars_list)
    contest_points(illegal_chars_list)


if __name__ == '__main__':
    main()