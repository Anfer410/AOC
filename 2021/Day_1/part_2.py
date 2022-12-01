def read_input():
    data = []
    f = open('Day_1/input.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines: 
        data.append(int(line.replace('\n','')))

    return data

def compare_measurements(input):
    previous_measurement = None
    counter = 0
    dcounter = 0


    for measurement in input:
        # print("current: " + measurement)
        
        if previous_measurement:
            # print("previous: :" + previous_measurement)
            
            if measurement > previous_measurement:
                counter += 1
                status = "increased"
            else: 
                dcounter += 1
                status = "decreased"
        else:
            status = "N/A - no previous measurement"
        previous_measurement = measurement


    print("increased :", counter)
    print("decreased :",  dcounter)


# produce new list of sums of 3
def generate_sums(input):
    sums = []
    for i in range(len(input) - 2):        
        sums.append(input[i] + input[i+1] + input[i+2])
        print("item: ", i, " value: ", input[i], " sum: ", input[i] + input[i+1] + input[i+2] )
    return sums

def main():
    data = read_input()
    
    compare_measurements(generate_sums(data))


if __name__ == "__main__":
    main()