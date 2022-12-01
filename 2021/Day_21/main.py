def dice(d):
    if d != 3:
        return d + 1
    return 1



def dice_roll(ct,d):
    m = 0
    for _ in range(3):
            ct += 1
            d = dice(d)
            m +=d
            print("dice_roll: ", d)
    return ct,m,d

def move_pawn(p,m):
    p += m

    while p > 10:
        p = abs(p - 10)
    return p


def game(p1_pos,p2_pos):
    
    d = 0
    p1_c = 0
    p1_s = 0
    
    p2_c = 0
    p2_s = 0

    while True:
        #  p1 roll
        p1_m = 0
        p1_c,p1_m,d = dice_roll(p1_c,d)
        p1_pos = move_pawn(p1_pos,p1_m)
        p1_s += p1_pos
        
        print("p1_pos : ", p1_pos, "p1_score: ",p1_s)
        
        if p1_s >= 1000:
            print("Player 1 won with score: ",p1_s ,"in ", p1_c, "rolls")
            return p2_s * (p1_c + p2_c)
            break 

         #  p1 roll
        p2_m = 0
        p2_c,p2_m,d = dice_roll(p2_c,d)
        p2_pos = move_pawn(p2_pos,p2_m)
        p2_s += p2_pos
        
        print("p2_pos : ", p2_pos, "p2_score: ",p2_s)
        
        if p2_s >= 1000:
            print("Player 2 won with score: ",p2_s ,"in ", p2_c, "rolls")
            return p1_s * (p1_c + p2_c)
            break 


def main():
    print("Day 21")
    print(game(4,8))

        






if __name__ == "__main__":
    main()