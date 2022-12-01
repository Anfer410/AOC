from rich import print

def read_input(file):
    with open(file) as f:
        mtrx = [[int(n) for n in line.strip()] for line in f if line.strip()]
    return mtrx

def neighbours(x, y, limit):
    return [
        (x1, y1)
        for (x1, y1) in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        if 0 <= x1 < limit and 0 <= y1 < limit
    ]


def find_path(data):
    costs = {(0, 0): 0}
    track = {}
    limit = len(data)
    # check
    assert limit == len(data[0])
    
    # start points
    points = [(0, 0)]
    
    for (x, y) in points:
        for (x1, y1) in neighbours(x, y, limit):
            if (x1, y1) in costs and costs[x1, y1] <= costs[x, y] + data[y1][x1]:
                continue
            costs[x1, y1] = costs[x, y] + data[y1][x1]
            points.append((x1, y1))
            track[x1, y1] = (x, y)

    path = {(0, 0)}
    x, y = limit - 1, limit - 1
    while (x, y) != (0, 0):
        path.add((x, y))
        x, y = track[x, y]
    
    # print(
    #     "\n".join(
    #         "".join(
    #             f"[green]{risk}[/green]"
    #             if (x, y) in path
    #             else f"[dim white]{risk}[/dim white]"
    #             for x, risk in enumerate(row)
    #         )
    #         for y, row in enumerate(data)
    #     )
    # )
    return costs[limit - 1, limit - 1]

def bump(row,n):
    return[((c + n - 1 ) % 9) + 1 for c in row]

def create_full_map(data):
    full_map = [
        bump(row, n)
        + bump(row, n + 1)
        + bump(row, n + 2)
        + bump(row, n + 3)
        + bump(row, n + 4)
        for n in range(5)
        for row in data
    ]
    return full_map


def main():
    cave_mtrx = read_input("Day_15/input.txt")
    # part 1
    print(find_path(cave_mtrx))
    
    # part 2
    print(find_path(create_full_map(cave_mtrx)))

    

if __name__ == "__main__":
    main()