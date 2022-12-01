def init_matrix(data):
    #         0 1 2 3 4 5 6 7 8
    fishes = [0,0,0,0,0,0,0,0,0,0]

    for fish_number in range(len(data)):
        fishes[data[fish_number]] += 1
    
    return fishes


def solve(fishes, days):
    i=1
    while i < days +1:
        # print("Day: ",i)
        # Get number of fishes at 0
        total_at_zero = fishes[0]

        #  Move all numbers of fhishes to the left
        for j in range(1,len(fishes)-1):
            fishes[j-1] = fishes[j]
        
        fishes[6] += total_at_zero
        fishes[8] = total_at_zero
        i+=1
        
    # print(fishes)
    return(fishes)

def count_fishes_total(fishes):
    sum = 0
    for num in fishes:
        sum +=num
    
    return sum


def main():
    days_80 = 80
    days_256 = 256

    fishes = [1,1,3,5,1,3,2,1,5,3,1,4,4,4,1,1,1,3,1,4,3,1,2,2,2,4,1,1,5,5,4,3,1,1,1,1,1,1,3,4,1,2,2,5,1,3,5,1,3,2,5,2,2,4,1,1,1,4,3,3,3,1,1,1,1,3,1,3,3,4,4,1,1,5,4,2,2,5,4,5,2,5,1,4,2,1,5,5,5,4,3,1,1,4,1,1,3,1,3,4,1,1,2,4,2,1,1,2,3,1,1,1,4,1,3,5,5,5,5,1,2,2,1,3,1,2,5,1,4,4,5,5,4,1,1,3,3,1,5,1,1,4,1,3,3,2,4,2,4,1,5,5,1,2,5,1,5,4,3,1,1,1,5,4,1,1,4,1,2,3,1,3,5,1,1,1,2,4,5,5,5,4,1,4,1,4,1,1,1,1,1,5,2,1,1,1,1,2,3,1,4,5,5,2,4,1,5,1,3,1,4,1,1,1,4,2,3,2,3,1,5,2,1,1,4,2,1,1,5,1,4,1,1,5,5,4,3,5,1,4,3,4,4,5,1,1,1,2,1,1,2,1,1,3,2,4,5,3,5,1,2,2,2,5,1,2,5,3,5,1,1,4,5,2,1,4,1,5,2,1,1,2,5,4,1,3,5,3,1,1,3,1,4,4,2,2,4,3,1,1]
    
    fishes_matrix = init_matrix(fishes)
    sum_80 = count_fishes_total(solve(fishes_matrix,days_80))
    
    fishes_matrix = init_matrix(fishes)
    sum_256 = count_fishes_total(solve(fishes_matrix,days_256))

    print("At 80 Days, fish count is: ", sum_80)
    print("At 256 Days, fish count is: ", sum_256)

    
if __name__ == "__main__":
    main()
    

    # Old idea, missing RAM to solve
    # while days > 0:
    #     for fish in range(len(fishes)):
    #         if fishes[fish] > 0:
    #             fishes[fish] -= 1
    #             # print(fishes[fish])
    #         elif fishes[fish] == 0:
    #             fishes[fish] = 6
    #             fishes.append(8)
    #             # print("new Fish spawned")
        
    #     print ("Days left:", days)
    #     days -= 1
    #     # print(fishes)
    # print(len(fishes))