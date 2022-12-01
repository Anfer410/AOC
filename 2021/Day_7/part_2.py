def read_input(file):
    data = []
    f = open(file, 'r')
    line = f.readline()
    f.close()
    
    for number in line.split(","):
        data.append(int(number))

    return data

def fuel_consumption(n):
    s = 1
    for i in range(2, n+1):
        s += i
    return s


def calculate_fuel_consumption(list):
    fuel = []
    for number in range(len(list)):
        fuel_cons_list = []
        for element in range(len(list)):
            diff = abs(list[element] - number)
            consumption = fuel_consumption(diff)
            
            fuel_cons_list.append(consumption)
        fuel.append(fuel_consumption_total(fuel_cons_list))

    print(min(fuel))


def fuel_consumption_total(fuel_con_list):
    sum = 0
    for num in fuel_con_list:
        sum +=num
    
    return sum


def main():
    mock_input = [16,1,2,0,4,2,7,1,2,14]
    input = read_input('Day_7/input.txt')
    
    calculate_fuel_consumption(input)
    

if __name__ == "__main__":
    main()