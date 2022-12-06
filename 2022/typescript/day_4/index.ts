import * as fs from 'fs';


const test_data = `2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8`;

let input_data = fs.readFileSync('./day_4/input.txt', 'utf8');

// let big_list = test_data.split('\n');
let big_list = input_data.split('\r\n');

let counter_all: number = 0
let counter_any: number = 0

for(var _i in big_list){
    let [zone_1_short, zone_2_short] = big_list[_i].split(',');
    let [zone_1_start, zone_1_end] = zone_1_short.split('-');
    let [zone_2_start, zone_2_end] = zone_2_short.split('-');

    let zone_1 : Array<number> = [];
    let zone_2 : Array<number> = [];

    for(var _point=Number(zone_1_start); _point<= Number(zone_1_end); _point++ ){
        zone_1.push(_point);
    };
    for(var _point=Number(zone_2_start); _point<= Number(zone_2_end); _point++ ){
        zone_2.push(_point);
    };

    if (zone_1.every(ai => zone_2.includes(ai)) || zone_2.every(ai => zone_1.includes(ai))){
        counter_all += 1;
    }
    else if(zone_1.some( ai => zone_2.includes(ai)) || zone_2.some(ai => zone_1.includes(ai))){
        counter_any += 1;
    };

}

console.log('Part 1: ', counter_all)
console.log('Part 2: ', counter_all + counter_any)