import time

game = {
   'A': {
        'Points': 1,
        'Name': 'Rock',
        'Beats': 'C',
        'Losses': 'B'},
    'B': {
        'Points': 2,
        'Name': 'Paper',
        'Beats': 'A',
        'Losses': 'C'},
    'C': {
        'Points': 3,
        'Name': 'Scissors',
        'Beats': 'B',
        'Losses': 'A'},
    'X': {
        'Points': 1,
        'Name': 'Rock',
        'Action': 'Loss'},
    'Y': {
        'Points': 2,
        'Name': 'Paper',
        'Action': 'Draw'},
    'Z': {
        'Points': 3,
        'Name': 'Scissors',
        'Action': 'Win'},
    'Draw': {
        'Points': 3
    },
    'Win': {
        'Points': 6
    },
    'Loss':{
        'Points': 0
    }
}


test_input = """A Y
B X
C Z"""


def read_input():
    with open('input.txt') as f:
        guide = f.read()
    return guide


def part_1(rounds_list):
    start_time = time.perf_counter()
    player_points = 0
    for round in rounds_list:
        opponent, player = round.split()        
        # Draw
        if game[opponent]['Name'] == game[player]['Name']:
            player_game = 'Draw'
        # Player win
        elif game[opponent]['Name'] == 'Scissors' and game[player]['Name'] == 'Rock':
            player_game = 'Win'
        elif game[opponent]['Name'] == 'Rock' and game[player]['Name'] == 'Paper':
            player_game = 'Win'
        elif game[opponent]['Name'] == 'Paper' and game[player]['Name'] == 'Scissors':
            player_game = 'Win'
        else:
            player_game = 'Loss'

        player_points += game[player]['Points'] + game[player_game]['Points']
    end_time = time.perf_counter()
    print(f'Part 1 execution time: {end_time - start_time} seconds')
    
    return player_points

    
def part_2(rounds_list):
    start_time = time.perf_counter()
    player_points = 0

    for round in rounds_list:
        opponent, action = round.split()
        player_action = game[action]['Action']

        if player_action == 'Win':
            round_points = game[game[opponent]['Losses']]['Points'] + game['Win']['Points']
        
        elif player_action == 'Draw':
            round_points = game[opponent]['Points'] + game['Draw']['Points']

        elif game[action]['Action'] == 'Loss':
            round_points = game[game[opponent]['Beats']]['Points'] + game['Loss']['Points']
        
        player_points += round_points
        
    end_time = time.perf_counter()
    print(f'Part 1 execution time: {end_time - start_time} seconds')
    
    return player_points


def main():
    rounds_list = read_input().splitlines() 
    
    print(f'Part_1: {part_1(rounds_list)}')
    print(f'Part_2: {part_2(rounds_list)}')


if __name__ == '__main__':
    main()