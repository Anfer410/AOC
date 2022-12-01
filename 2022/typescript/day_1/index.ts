import * as fs from 'fs'

const test_data : string =`1000
2000
3000

4000

5000
6000

7000
8000
9000

10000`;

let input_data = fs.readFileSync('./day_1/input.txt', 'utf8');

let elfList: number[] = [];
let itemCalSum: number = 0

// let item_list = test_data.split('\n');
let item_list = input_data.split('\r\n')

for(var item in item_list) {
    if (item_list[item] != '' ){
        itemCalSum = itemCalSum + Number(item_list[item]);
    } else {
        elfList.push(itemCalSum);
        itemCalSum = 0;
    }
}

var sorted_list = elfList.sort(function(x,y){return x-y}).reverse()

// Part 1
console.log(sorted_list[0])

// Part 2
var top_three: number = sorted_list[0] + sorted_list[1] + sorted_list[2]
console.log(top_three)