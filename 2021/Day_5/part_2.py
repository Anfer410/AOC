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
    high = 0
    low = 0

    if n1 < n2:
        for number in range(n1, n2+1):
            list.append(number)
        return list
    if n1 > n2:
        for number in reversed(range(n2, n1+1)):
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


        if x1 != x2 and y1 != y2:
            # Find points
            y_fields = find_numbers_in_between(y1,y2)            
            x_fields = find_numbers_in_between(x1,x2)

            print(y_fields)
            print(x_fields)

            #  validate if 45 deg
            valid = False
            
            for i in range(len(y_fields) - 1):

            
                if int(x_fields[i]) - int(x_fields[i+1]) == 1 or int(x_fields[i]) - int(x_fields[i+1]) == -1 :
                    valid = True
                    print(x_fields[i]," - ",x_fields[i+1]," = ", x_fields[i] - x_fields[i+1] )
            
                if int(y_fields[i]) - int(y_fields[i+1]) == 1 or int(y_fields[i]) - int(y_fields[i+1]) == -1 :
                    valid = True
                    print(y_fields[i]," - ",y_fields[i+1]," = ", y_fields[i] - y_fields[i+1] )
            
            print(valid)
            
            
            if valid == True:
                for i in range(len(y_fields)):
                    mtrx[y_fields[i]][x_fields[i]] += 1
                    # print("Mark: ", x_fields[i],y_fields[i])

                    
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
                            
def print_map(mtrx):
    mtrxrows = len(mtrx)
    # Check rows
    for m in range(mtrxrows):
        print(mtrx[m])
        
def initiate_map(rows,cols):
    mtrx = [ [ 0 for i in range(rows) ] for j in range(cols) ]
    return mtrx
            


def main():
    mock_data = 'Day_5/mock.txt'
    input_data = 'Day_5/input.txt'
    
    # input = read_input(mock_data)
    # mtrx =initiate_map(10,10)

    input = read_input(input_data)
    mtrx =initiate_map(1000,1000)
    
    
    

    find_vents(input, mtrx)

    print("Found dangerous points: ",find_number_of_dangerous_points(mtrx))
    print(' ')
    # print("Map with dangerous points:")
    # print_map(mtrx)

    

    


if __name__ == "__main__":
    main()