from statistics import multimode

def read_input():
    data = []
    f = open('Day_3/input.txt', 'r')
    # f = open('Day_3/mock.txt', 'r')
    lines = f.readlines()
    f.close()
    
    for line in lines: 
        data.append(line.replace('\n',''))

    return data
    

def create_list_of_elements(calculate_data, position):
    list = []
    for bits in range(len(calculate_data)):
        list.append(calculate_data[bits][position])
    return list


def create_list_common_element(list, common_element, position):
    for bits in reversed(range(len(list))):
        if list[bits][position] != common_element:
            del list[bits]
    return list


#  Returns most common element, if there is no uniqe value, it returns default
def find_most_common(l):
    result = multimode(l)

    if len(result) > 1: 
        out = '1'
    else :
        out = str(result[0])
    return  out

#  Returns least common element, if there is no uniqe value, it returns default
def find_least_common(l):
    common = find_most_common(l)
    if common == '1':
        number = '0'
    elif common == '0':
        number = '1'
    return number



def decode_oxygen(calculate_data, elements):
    
    for i in range(0,elements):
        list = create_list_of_elements(calculate_data,i)
        
        common = find_most_common(list)
        calculate_data = create_list_common_element(calculate_data,common,i)
        if len(list) > 1:
            calculate_data = create_list_common_element(calculate_data,common,i)
        else: 
            break

    
    decoded = int(''.join(calculate_data),2)
    return decoded



def decode_co2(calculate_data, elements):

    for i in range(0, elements):
        list = create_list_of_elements(calculate_data,i)
        common = find_least_common(list)
        # print("Data elements: ",len(calculate_data), " Common number: ", common)
        
        if len(list) > 1 : 
            calculate_data = create_list_common_element(calculate_data,common,i)
        else:
            break
        
    # print(calculate_data)
    decoded = int(''.join(calculate_data),2)
    return decoded


def main():
    elements = 12
    # elements = 5
    data = read_input()
    oxygen = decode_oxygen(data, elements)
    print(data)
    data = read_input()
    co2 = decode_co2(data,elements)
    
    print('Oxygen: {}, CO2: {}, Life support: {}'.format(oxygen, co2, oxygen * co2))
    
    


if __name__ == "__main__":
    main()
