import * as fs from 'fs';

const game = {
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


const test_input : string = `A Y
B X
C Z`

let input_data = fs.readFileSync('./day_2/input.txt', 'utf8');

function part_1(rounds_list, game){
    let player_points : number = 0
    let player_game : string
    
    for(var round in rounds_list){
        var [opponent, player] = rounds_list[round].split(' ')
        
        if(game[opponent]['Name'] == game[player]['Name']){
            player_game = 'Draw'
        } else if( game[opponent]['Name'] == 'Scissors' && game[player]['Name'] == 'Rock'){
            player_game = 'Win'
        } else if(game[opponent]['Name'] == 'Rock' && game[player]['Name'] == 'Paper'){
            player_game = 'Win'
        } else if(game[opponent]['Name'] == 'Paper' && game[player]['Name'] == 'Scissors'){
            player_game = 'Win'
        } else {
            player_game = 'Loss'
        }
        
        player_points += game[player]['Points'] + game[player_game]['Points'];
    }

    return player_points
} 

function part_2(rounds_list, game){
    
    var player_points: number = 0
    var round_points: number = 0
    var player_action: string

    for(var round in rounds_list){
        var [opponent, action] = rounds_list[round].split(' ')
        player_action = game[action]['Action']
        
        if(player_action == 'Win'){
            round_points = game[game[opponent]['Losses']]['Points'] + game['Win']['Points']
        }
        else if(player_action == 'Draw'){
            round_points = game[opponent]['Points'] + game['Draw']['Points']
        }
        else if(game[action]['Action'] == 'Loss'){
            round_points = game[game[opponent]['Beats']]['Points'] + game['Loss']['Points']
        }
        
        player_points += round_points
    
    }
    return player_points
}


var rounds_list = input_data.split('\r\n')
// var rounds_list = test_input.split('\n')

console.log('Part 1: ', part_1(rounds_list, game))
console.log('Part 2: ', part_2(rounds_list, game))



