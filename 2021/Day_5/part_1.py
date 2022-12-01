def read_input(file):
    data = []
    f = open(file, 'r')
    lines = f.readlines()
    f.close()

    for line in lines: 
        line = line.replace('\n','').replace(' -> ',',')
        print(line.split(','))
        data.append(line.split(','))
        
    return data


def find_numbers_in_between(n1,n2):
    list = []
    low = 0
    high = 0

    if n1 > n2: 
        low = n2
        high = n1
    
    if n1 < n2: 
        low = n1
        high = n2

    for number in range(low, high +1):
        list.append(number)
    return list

def find_vents(data, mtrx):
   
    for line in data:
        x_fields = []
        y_fields = []
        x1 = int(line[0])
        y1 = int(line[1])
        x2 = int(line[2])
        y2 = int(line[3])

        # Look for x lines
        if x1 == x2:
            y_fields = find_numbers_in_between(y1,y2)
            for y_field in y_fields:
                mtrx[y_field][x1] += 1
        
        # Look for y lines
        if y1 == y2:
            x_fields = find_numbers_in_between(x1,x2)
            for x_field in x_fields:
                mtrx[y1][x_field] += 1
            
            

def find_number_of_dangerous_points(mtrx):
    counter = 0
    mtrxrows = len(mtrx)
    mtrxcols = len(mtrx[0])
    # Check rows
    for m in range(mtrxcols):
        for n in range(mtrxrows):
            if mtrx[n][m] > 1:
                counter += 1
    return counter
                            


def initiate_map(rows,cols):
    mtrx = [ [ 0 for i in range(rows) ] for j in range(cols) ]
    return mtrx
            


def main():
    debug = False
    
    if debug == True: 
        input_data = 'Day_5/mock.txt'
        mtrx =initiate_map(10,10)
        
    else:
        input_data = 'Day_5/input.txt'
        mtrx =initiate_map(1000,1000)

    
    input = read_input(input_data)

    find_vents(input, mtrx)

    print(find_number_of_dangerous_points(mtrx))


    if debug == True:  
        print(mtrx)         

    


if __name__ == "__main__":
    main()