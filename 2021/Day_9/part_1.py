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

            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                # corners
                new_neighbors = []
                if i != 0:
                    new_neighbors.append(arr[i - 1][j])  # top neighbor
                if j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i][j + 1])  # right neighbor
                if i != len(arr) - 1:
                    new_neighbors.append(arr[i + 1][j])  # bottom neighbor
                if j != 0:
                    new_neighbors.append(arr[i][j - 1])  # left neighbor

            else:
                # add neighbors
                new_neighbors = [
                    arr[i - 1][j],  # top neighbor
                    arr[i][j + 1],  # right neighbor
                    arr[i + 1][j],  # bottom neighbor
                    arr[i][j - 1]   # left neighbor
                ]

            neighbors.append({
                "value": value,
                "neighbors": new_neighbors})

    return neighbors



def find_low_points(data):
    danger_zones = []
    for values in range(len(data)):
        if all(data[values]["value"] < neighbor for neighbor in data[values]["neighbors"]) :
            danger_zones.append(data[values]["value"])
    
    return danger_zones

def solve(data):
    total = 0
    for point in data:
        total += point + 1
    return total




def main():
    input = read_input("Day_9/input.txt")
    
    # find_min(input)
    neighbours = find_neighbours(input)
    danger = find_low_points(neighbours)
    print(danger)
    print(solve(danger))



if __name__ == "__main__":
    main()