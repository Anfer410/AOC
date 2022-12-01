from statistics import multimode

def read_input(file):
    data = []
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    for line in lines: 
        data.append(line.replace('\n',''))

    return data
    

def create_list_of_elements(data, position):
    list = []
    for bits in range(len(data)):
        list.append(data[bits][position])
    return list


def create_list_common_element(data, common_element, position):
    for bits in reversed(range(len(data))):
        if data[bits][position] != common_element:
            del data[bits]
    return data


#  Returns most common element, if there is no uniqe value, it returns default
def find_most_common(l):
    common = multimode(l)

    if len(common) > 1: 
        return '1'
    else :
        return str(common[0])
    

#  Returns least common element, if there is no uniqe value, it returns default
def find_least_common(l):
    common = find_most_common(l)
    if common == '1':
        return '0'
    elif common == '0':
        return '1'
    



def decode_oxygen(data, elements):
    
    for position in range(0,elements):
        
        list = create_list_of_elements(data,position)
        common = find_most_common(list)
        data = create_list_common_element(data,common, position)
        if len(list) > 1:
            data = create_list_common_element(data,common,position)
        else: 
            break
    
    decoded = int(''.join(data),2)
    return decoded



def decode_co2(calculate_data, elements):

    for position in range(0, elements):
        list = create_list_of_elements(calculate_data,position)
        common = find_least_common(list)
        # print("Data elements: ",len(calculate_data), " Common number: ", common)
        
        if len(list) > 1 : 
            calculate_data = create_list_common_element(calculate_data,common,position)
        else:
            break
        
    # print(calculate_data)
    decoded = int(''.join(calculate_data),2)
    return decoded


def main():
    file = "Day_3/input.txt"
    elements = 12

    oxygen = decode_oxygen(read_input(file), elements)  
    co2 = decode_co2(read_input(file),elements)
    
    print('Oxygen: {}, CO2: {}, Life support: {}'.format(oxygen, co2, oxygen * co2))
    


if __name__ == "__main__":
    main()
