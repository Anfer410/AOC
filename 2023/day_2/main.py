test_data="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def read_input(file="input.txt"):
    with open(file) as f:
        lines = f.readlines()
        content = []
    for line in lines:
        content.append(line.strip())
    
    return(content)

def part_1():
    red = 12
    green = 13
    blue = 14

    possible_game = []
    test_game_data = test_data.splitlines()
    game_data = read_input()

    for games in game_data:
        game_num,game=games.split(":")
        
        possible = True
        for r in game.split(";"):
            if "," in r:
                for balls in r.split(","):
                    count, color = balls.split()
                    if (int(count) > red and color == "red"):
                         print(f"{game_num}, red:{count}/{red}")
                         possible = False
                    if (int(count) > green and color == "green"):
                         possible = False
                         print(f"{game_num}, green:{count}/{green}")
                    if (int(count) > blue and color == "blue"):
                         possible = False
                         print(f"{game_num}, blue:{count}/{blue}")
            else:
                count, color = r.split()
                if (int(count) > red and color == "red"):
                     print(f"{game_num}, red:{count}/{red}")
                     possible = False
                if (int(count) > green and color == "green"):
                     possible = False
                     print(f"{game_num}, green:{count}/{green}")
                if (int(count) > blue and color == "blue"):
                     possible = False
                     print(f"{game_num}, blue:{count}/{blue}")
                       
                        
        if possible:
            possible_game.append(int(game_num.split()[1]))


    print(possible_game)
    print(sum(possible_game))


def part_2():
    possible_game = []
    test_game_data = test_data.splitlines()
    game_data = read_input()

    power = []
    for games in game_data:
        game_num,game=games.split(":")
        min_red = 0
        min_green = 0 
        min_blue = 0

        for r in game.split(";"):
            if "," in r:
                for balls in r.split(","):
                    count, color = balls.split()
                    if min_red < int(count) and color == "red":
                        min_red = int(count)
                    if min_green < int(count) and color == "green":
                        min_green = int(count)
                    if min_blue < int(count) and color == "blue":
                        min_blue = int(count)
            else:
                count, color = r.split()
                if min_red < int(count) and color == "red":
                    min_red = int(count)
                if min_green < int(count) and color == "green":
                    min_green = int(count)
                if min_blue < int(count) and color == "blue":
                    min_blue = int(count)
            
        power.append(min_blue * min_green * min_red)

    print(sum(power))



def main():
    part_2()


if __name__ == "__main__":
    main()
# end main