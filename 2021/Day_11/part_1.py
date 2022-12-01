
def neighbours(cell):
    x = cell[0]
    y = cell[1]
    return [[x - 1, y - 1],[x, y - 1],[x + 1, y - 1],[x - 1, y],[x + 1, y],[x - 1, y + 1],[x, y + 1] ,[x + 1, y + 1]]


def find_neighbours(arr):
    neighbours_details = []

    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):
            value_pos = [i,j]
            new_neighbours_value = []
            new_neighbours_pos = []
            for neighbour in list(neighbours(value_pos)):
                x = neighbour[0]
                y = neighbour[1]
                
                if x >= 0 and x < len(arr) and y >= 0 and y < len(arr[i]):       
                    # new_neighbours_value.append(arr[neighbour[0]][neighbour[1]])
                    new_neighbours_pos.append(neighbour)
            
            neighbours_details.append({
                "value": value,
                "value_pos": value_pos,
                "neighbours_pos": new_neighbours_pos,
                })
    return neighbours_details


def read_input(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append([int(value) for value in line.replace('\n','')])
    return data

   

# step 1 update all octopus energy
def increase_octopus_energy(mtrx):
    for i in range(len(mtrx)):
        mtrx[i]["value"] += 1
            
            
# step 2 look for all octopus that has energy lvl above 9
def look_for_flash(mtrx,flash_counter):
    flash_list = []
    after_effect = True
    while after_effect:
        neighbours_increase = []
        after_effect = False
        for i in range(len(mtrx)):
            #  for values larger than 9 and if havent flash in this step ,
            if mtrx[i]["value"] > 9 \
            and mtrx[i]["value_pos"] not in [past_flash["value_pos"] for past_flash in flash_list]: 
                after_effect = True
                flash_counter +=1
                flash_list.append(mtrx[i])
                
                for neigbour in mtrx[i]["neighbors_pos"]:
                    neighbours_increase.append(neigbour)
        
        for i in range(len(mtrx)):
            if mtrx[i]["value_pos"] in neighbours_increase:
                mtrx[i]["value"] += 1
    
    for i in range(len(mtrx)):
        if mtrx[i]["value_pos"] in [past_flash["value_pos"] for past_flash in flash_list]:
            mtrx[i]["value"] = 0
        

    
    return flash_counter

def flash(mtrx,flash_counter):
    past_flash_points = []
    after_flashes = True
    
    affected_neigbours = []
    while after_flashes:
        print("while True")
        after_flashes = False
        
        for i in range(len(mtrx)):
            if mtrx[i]["value"] > 9 :
                if mtrx[i]["value_pos"] not in [ past_flash["value_pos"] for past_flash in past_flash_points]: 
                    after_flashes = True
                    # print("FLASH !")
                    past_flash_points.append(mtrx[i])
                    flash_counter += 1

                    for neigbour in mtrx[i]["neighbours_pos"]:
                        affected_neigbours.append(neigbour)
                # else:
                    # print(mtrx[i]["value_pos"], " already detected in this step")
            
            for i in range(len(mtrx)):
                if mtrx[i]["value_pos"] in affected_neigbours:
                    affected_neigbours.remove(mtrx[i]["value_pos"])
                    mtrx[i]["value"] += 1
            
    for i in range(len(mtrx)):
        if mtrx[i]["value"] > 9 :
           mtrx[i]["value"] = 0
           
           
                
    return flash_counter
            






    

def print_matrix(mtrx):
    y = 10
    x = 10
    index = 0
    for i in range(y):
        line = ''
        for j in range(x):
           line = line + str(mtrx[index]["value"]) + ','
           index +=1
        print(line)
    

def main():
    # input = read_input("Day_11/mock.txt")
    input = read_input("Day_11/input.txt")
    # print_matrix(input)
    
    print("Search for neigbors")
    octopus_mtrx = find_neighbours(input)
    # print_matrix(octopus_mtrx)
    flash_counter = 0
    i = 0 
    while i < 500:
        if all(octopus_mtrx[i]["value"] == 0 for i in range(len(octopus_mtrx))):
            break
        
        print("Step: ", i+1 )
        increase_octopus_energy(octopus_mtrx)
        # print_matrix(octopus_mtrx)
        # print("look for flashes")
        flash_counter = flash(octopus_mtrx,flash_counter)
        print_matrix(octopus_mtrx)
        i += 1
        
            
    
    print("First sync observed during step: ", i )
    print_matrix(octopus_mtrx)
    
    print("total_flashes:",flash_counter)
    


if __name__ == "__main__":
    main()