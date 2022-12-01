from itertools import permutations, product

def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    content = []
    scanner_data = []
    scanner_id = ''
    for line in lines:
        if '---' in line:
            scanner_new_id = line
            if scanner_data:
                if scanner_id == '':
                    scanner_id = '--- scanner 0 ---\n'
                content.append([scanner_id.replace('\n',''),scanner_data])
                scanner_id = scanner_new_id
                scanner_data = []
        else:
            if line != '\n':
                scanner_data.append(tuple(int(e) for e in line.replace('\n','').strip().split(',')))
    return content


def rotations(items):
    l = []
    for signed in product(*[[-a,a] for a in items]):
        for p in permutations(signed):
            l.append(p)
    return l
# To Do:
# Create list of all posible rotations
# Compare list with other beacons 
# find 12 overlapping beacons 

    
    


def main():
    content = read_input("Day_19/input.txt")
    
    # reading = content[0][1][0]
    # print(reading)
    #  Demo
    
    # if reading in angles:
    #     print("Found:",reading)

    for i in range(len(content)-1):
        for j in range(len(content[i][1])):
            if content[i][1][j] in rotations(content[i+1][1]):
                print("found matching ", content[i][0], " in ", content[i+1][0] )




if __name__ == "__main__":
    main()