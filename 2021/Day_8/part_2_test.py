def read_input(file):
    data = []
    f = open(file,'r')
    lines = f.readlines()
    for line in lines:
        input_output_list = []
        
        for elements in line.replace("\n","").split("|"):
            input_output_list.append(elements.split())
        data.append(input_output_list)
        
    return data


def find_uniqe_patterns(encoded_input,decoded_patterns):
    
    if len(encoded_input) == 2 :
        for char in encoded_input:
            decoded_patterns[1].append(char) 
    
    if len(encoded_input) == 4 :
        for char in encoded_input:
            decoded_patterns[4].append(char) 
    
    if len(encoded_input) == 3 :
        for char in encoded_input:
            decoded_patterns[7].append(char) 
    
    if len(encoded_input) == 7 :
        for char in encoded_input:
            decoded_patterns[8].append(char) 
    
    return decoded_patterns


def find_missing_patterns(decoded_patterns, encoded_digits):
    #  you have 1 4 7 8

    #  top line = 7 - 1 
    top_line = []
    for char in decoded_patterns[7]:
        if char not in decoded_patterns[1]:
            top_line.append(char)
    

    #  left bottom corner = 8 - (4 + top)
    bottom_left_corner_helper = []
    for char in top_line:
        if char not in bottom_left_corner_helper:
            bottom_left_corner_helper.append(char)
    
    for char in decoded_patterns[4]:
        if char not in top_line:
            bottom_left_corner_helper.append(char)
    bottom_left_corner = []
    for char in decoded_patterns[8]:
        if char not in bottom_left_corner_helper:
            bottom_left_corner.append(char)
        
    # left mid corner = 8 - ( 7 + bottom left corner)
    mid_left_corner_helper = []
    for char in decoded_patterns[7]:
        if char not in mid_left_corner_helper:
            mid_left_corner_helper.append(char)
    for char in bottom_left_corner:
        if char not in mid_left_corner_helper:
            mid_left_corner_helper.append(char)

    mid_left_corner = []
    for char in decoded_patterns[8]:
        if char not in mid_left_corner_helper:
            mid_left_corner.append(char) 

def decode_missing_numbers(pattern_map,encoded_digits):
    if len(encoded_digits) == 6 :
        #  number can be 0 6 9 
        print("Deciding between 0 6 9 ")
    
    if len(encoded_digits) == 5 :
        print("Deciding between 2 3 5")


def print_resolved_patterns(pattern_map,decoded_patterns):
    for i in range(len(decoded_patterns)):
        if decoded_patterns[i] : 
            print("found pattern for number ", i , ' : ', decoded_patterns[i])




        
def sum(list):
    sum = ''
    for num in list:
        sum += str(num)
    return int(sum)

def main():
    # input = read_input("Day_8/input.txt")
    input = read_input("Day_8/mock.txt")
    number = 0

    for encoded_inputs in range(len(input)):
        pattern_map = [[],[],[],[],[],[],[],[],[],[]]
        
        for encoded_digits in input[encoded_inputs][0]:
            pattern_map = find_uniqe_patterns(encoded_digits, pattern_map)
        print(pattern_map)
        
        find_missing_patterns(pattern_map, encoded_digits)
        
        for encoded_digits in input[encoded_inputs][0]:
                decode_missing_numbers(pattern_map,encoded_digits)
        print(pattern_map)
        
        
        print_resolved_patterns(pattern_map)



if __name__ == "__main__":
    main()