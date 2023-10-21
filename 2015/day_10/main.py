from itertools import groupby

play = "1113222113"
test_input = "211"
 
def look_and_say(input_string):
    input_string = ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])
    
    return input_string

def main():
    game_input = play
    for i in range(50):
        print("Game id:", i)
        if i == 40:
            game_40 = game_input
        new_number = look_and_say(game_input)
        game_input = new_number
        
    
    print("Game_40: ",len(game_40))
    print("Game_50: ",len(game_input))

if __name__ == "__main__":
    main()
# end main