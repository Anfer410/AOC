def read_input(filename):
    content = []
    with open(filename) as f:
        lines = f.readlines()
    f.close()
    
    for line in lines:
        line = line.replace("\n", "")
        command = line.split()[0]
        pos = line.split()[1].split(",")
        
        content.append({
            "switch": command,
            "pos": [pos[c][2:] for c in range(len(pos))]
        })
        
    return content
 

def main():
    data = read_input('Day_22/input.txt')
    cubes = []
    x_str,y_str,z_str = data[0]["pos"]
    
    x_range = x_str.split("..")
    x_range = [ x for x in range(int(x_range[0]),int(x_range[1])+1)]
    
    y_range = y_str.split("..")
    y_range = [ y for y in range(int(y_range[0]),int(y_range[1])+1)]
    
    z_range = z_str.split("..")
    z_range = [ z for z in range(int(z_range[0]),int(z_range[1])+1)]
    
    for x in x_range:
        for y in y_range:
            for z in z_range:
                cubes.append(zip(x,y,z))

    print(cubes)




if __name__ == "__main__":
    main()
