"use strict";
exports.__esModule = true;
var fs = require("fs");
var test_data = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8";
var input_data = fs.readFileSync('./day_4/input.txt', 'utf8');
// let big_list = test_data.split('\n');
var big_list = input_data.split('\r\n');
var counter_all = 0;
var counter_any = 0;
var _loop_1 = function () {
    var _a = big_list[_i].split(','), zone_1_short = _a[0], zone_2_short = _a[1];
    var _b = zone_1_short.split('-'), zone_1_start = _b[0], zone_1_end = _b[1];
    var _c = zone_2_short.split('-'), zone_2_start = _c[0], zone_2_end = _c[1];
    var zone_1 = [];
    var zone_2 = [];
    for (var _point = Number(zone_1_start); _point <= Number(zone_1_end); _point++) {
        zone_1.push(_point);
    }
    ;
    for (var _point = Number(zone_2_start); _point <= Number(zone_2_end); _point++) {
        zone_2.push(_point);
    }
    ;
    if (zone_1.every(function (ai) { return zone_2.includes(ai); }) || zone_2.every(function (ai) { return zone_1.includes(ai); })) {
        counter_all += 1;
    }
    else if (zone_1.some(function (ai) { return zone_2.includes(ai); }) || zone_2.some(function (ai) { return zone_1.includes(ai); })) {
        counter_any += 1;
    }
    ;
};
for (var _i in big_list) {
    _loop_1();
}
console.log('Part 1: ', counter_all);
console.log('Part 2: ', counter_all + counter_any);
