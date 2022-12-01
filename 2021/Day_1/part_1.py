def read_input():
    data = []
    f = open('Day_1/input.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines: 
        data.append(int(line.replace('\n','')))

    return data

def calculate_course(input):
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


def main():
    data = read_input()
    calculate_course(data)


if __name__ == "__main__":
    main()