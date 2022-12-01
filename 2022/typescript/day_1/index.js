"use strict";
exports.__esModule = true;
var fs = require("fs");
var test_data = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000";
var input_data = fs.readFileSync('./day_1/input.txt', 'utf8');
// console.log(input_data)
var elfList = [];
var itemCalSum = 0;
// let item_list = test_data.split('\n');
var item_list = input_data.split('\r\n');
console.log(item_list);
for (var item in item_list) {
    if (item_list[item] != '') {
        itemCalSum = itemCalSum + Number(item_list[item]);
    }
    else {
        elfList.push(itemCalSum);
        itemCalSum = 0;
    }
}
var sorted_list = elfList.sort(function (x, y) { return x - y; }).reverse();
// Part 1
console.log(sorted_list[0]);
// Part 2
var top_three = sorted_list[0] + sorted_list[1] + sorted_list[2];
console.log(top_three);
