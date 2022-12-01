def read_input():
    data = []
    # f = open('Day_3/input.txt', 'r')
    f = open('Day_3/mock.txt', 'r')
    lines = f.readlines()
    f.close()

    for line in lines: 
        data.append(line.replace('\n',''))

    return data
    

def create_list_of_elements(data, position):
    list = []
    for bits in range(len(data)):
        # print(data[bits])
        # print("First bit is : ", data[bits][1])
        list.append(data[bits][position])
    return list


def find_most_common_element(iterable_list): 
    most_common_element = max(set(iterable_list), key = iterable_list.count) # Returns the most common element
    return most_common_element # Return most common element

def find_least_common_element(iterable_list): 
    most_common_element = min(set(iterable_list), key = iterable_list.count) # Returns the most common element
    return most_common_element # Return most common element
            

def decode_gamma(data, elements):
    gamma = []
    for i in range(0,elements):
        gamma.append(find_most_common_element(create_list_of_elements(data,i)))
        
        decoded = int(''.join(gamma),2)
    return decoded

def decode_epsilon(data, elements):
    epsilion = []
    for i in range(0,elements):
        epsilion.append(find_least_common_element(create_list_of_elements(data,i)))

        decoded = int(''.join(epsilion),2)
    return decoded

def main():
    elements = 12
    data = read_input()
    gamma = decode_gamma(data, elements)
    epsilion = decode_epsilon(data, elements)

    # print("Gamma: ", gamma, " Epsilion: ", epsilion, "Fuel consumption: ", gamma * epsilion)
    print('Gamma: {}, Epsilion: {}, Fuel consumption: {}'.format(gamma, epsilion, gamma * epsilion))
    
    


if __name__ == "__main__":
    main()
