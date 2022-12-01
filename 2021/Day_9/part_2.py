from os import read


def read_input(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append([int(value) for value in line.replace('\n','')])
    return data


def find_neighbours(arr):

    neighbors = []

    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):
            value_pos = [i,j]
            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                # corners
                new_neighbors = []
                new_neighbors_pos = []
                if i != 0:
                    new_neighbors.append(arr[i - 1][j])  # top neighbor
                    new_neighbors_pos.append([i-1,j])
                if j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i][j + 1])  # right neighbor
                    new_neighbors_pos.append([i,j +1])
                if i != len(arr) - 1:
                    new_neighbors.append(arr[i + 1][j])  # bottom neighbor
                    new_neighbors_pos.append([i + 1,j])
                if j != 0:
                    new_neighbors.append(arr[i][j - 1])  # left neighbor
                    new_neighbors_pos.append([i,j -1])

            else:
                # add neighbors
                new_neighbors = [
                    arr[i - 1][j],  # top neighbor
                    arr[i][j + 1],  # right neighbor
                    arr[i + 1][j],  # bottom neighbor
                    arr[i][j - 1]   # left neighbor
                ]
                new_neighbors_pos = [
                    [i-1,j],
                    [i,j + 1],
                    [i +1,j],
                    [i,j -1]
                ]

            neighbors.append({
                "value": value,
                "value_pos": value_pos,
                "neighbors": new_neighbors,
                "neighbors_pos": new_neighbors_pos,
                })

    return neighbors


def find_low_points(data):
    danger_zones = []
    for values in range(len(data)):
        # print(data[values]["neighbors"])
        if all(data[values]["value"] < neighbor for neighbor in data[values]["neighbors"]) :
            # print(data[values])    
            danger_zones.append(data[values])

    return danger_zones



def verify_neighbor_neighbor(point,parent_point, neighbors, verified_list):
    points_to_verify = []
    
    for neighbor in neighbors:
        # find neighbor neighbors
        if neighbor["value"] == point[0] and neighbor["value_pos"] == point[1]:
            for neighbor_neighbor in range(len(neighbor["neighbors"])):
                # print(neighbor["neighbors_pos"][neighbor_neighbor])
                # print([verified_list[i][1] for i in range(len(verified_list))])
                
                if neighbor["neighbors"][neighbor_neighbor] != 9 \
                and neighbor["neighbors"][neighbor_neighbor] != parent_point \
                and neighbor["neighbors_pos"][neighbor_neighbor] not in [verified_list[i][1] for i in range(len(verified_list))]:
                # and neighbor["neighbors_pos"][neighbor_neighbor] not in [ptv for ptv in points_to_verify]:
                    points_to_verify.append([neighbor["neighbors"][neighbor_neighbor],neighbor["neighbors_pos"][neighbor_neighbor]]) 
    # print(" I verified neigbors of: ", point[0], " and they are: ", points_to_verify)

    return points_to_verify




def find_basin(danger_points, neighbors):
    locations = []
    danger_point_0 = []
    danger_point_1 = []
    danger_point_2 = []
    danger_point_0.append({
        'value': 1, 
        'value_pos': [0, 1], 
        'neighbors': [9, 9, 2], 
        'neighbors_pos': [[0, 2], [1, 1], [0, 0]]
    })
    danger_point_1.append({
        'value': 0, 
        'value_pos': [0, 9], 
        'neighbors': [1, 1], 
        'neighbors_pos': [[1, 9], [0, 8]]
    })
    danger_point_2.append({
        'value': 5, 
        'value_pos': [2, 2], 
        'neighbors': [8, 6, 6, 8], 
        'neighbors_pos': [[1, 2], [2, 3], [3, 2], [2, 1]]
    })
    
    # print(danger_points)

    for point in danger_points:
        basin = []        
        parent_point = point["value"]
        points_to_verify = []
        verified_points = []
        
        verified_points.append([point["value"],point["value_pos"]])

        basin.append(parent_point)
        for neighbor in range(len(point["neighbors"])):
            if point["neighbors"][neighbor] != 9 and point["neighbors"][neighbor] != parent_point and point["neighbors_pos"][neighbor] not in verified_points:
                points_to_verify.append([point["neighbors"][neighbor],point["neighbors_pos"][neighbor]])       

        # print("Parent point: ",parent_point)
        # print("basin: ", basin," to check:", points_to_verify)

        while len(points_to_verify) > 0:
            for ptv in reversed(range(len(points_to_verify))):
                
                parent_neighbor = points_to_verify[ptv]
                
                # print("Parent neigbor: ",parent_neighbor)
                basin.append(parent_neighbor)

                new_ptv = verify_neighbor_neighbor(points_to_verify[ptv],parent_neighbor,neighbors, verified_points)
                
                verified_points.append(points_to_verify[ptv])
                    
                # print("new_ptv:", new_ptv)
                if new_ptv:
                    for new_point in new_ptv:
                        # print([ptv_list for ptv_list in points_to_verify])
                
                        if new_ptv not in points_to_verify:
                            # print("Point added to check :",new_point)
                            points_to_verify.append(new_point)
                
                points_to_verify.remove(points_to_verify[ptv])
                
                # print("basin: ", basin," to check:", points_to_verify)
                
            
        #  remove duplicate entries in basin
        basin_no_duplicates = []
        for bas in basin:
            if bas not in basin_no_duplicates:
                basin_no_duplicates.append(bas)
        locations.append(basin_no_duplicates)
    


    location_len = []
    for location in locations:
        location_len.append(len(location))
    
    location_len.sort(reverse=True)
    print(location_len)
    print(location_len[0]*location_len[1]*location_len[2])


        
def main():
    input = read_input("Day_9/input.txt")
    
    neighbors = find_neighbours(input)
    danger = find_low_points(neighbors)
    find_basin(danger,neighbors)
    



if __name__ == "__main__":
    main()