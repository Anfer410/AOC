import * as fs from 'fs';

const test_data = `vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw`


function part_1(rucsack, letters_priorities){
    var rucksack_sum: number = 0

    for(var items in rucsack){
        
        var common = ''
        var items_len = rucksack[items].length / 2
        var item_1 = rucksack[items].substring(0,items_len)
        var item_2 = rucksack[items].substring(items_len)

        for(var item in item_1){
            if(item_2.includes(item_1[item])){
                common = item_1[item]
            }
        }
        console.log(common)
        rucksack_sum += letters_priorities.indexOf(common) + 1
    }
        
    console.log(rucksack_sum)
}


function part_2(rucksack, letters_priorities){
    var rucksack_sum: number = 0

    for(var _i=0; _i < rucksack.length -2; _i=_i + 3){
        var found: Array<string>  = []
        var elf_rucksack_1: string = rucksack[_i]
        var elf_rucksack_2: string = rucksack[_i + 1]
        var elf_rucksack_3: string = rucksack[_i + 2]

        for(var _j=0;  _j < elf_rucksack_1.length; _j++){
            if(elf_rucksack_2.includes(elf_rucksack_1[_j]) && elf_rucksack_3.includes(elf_rucksack_1[_j]) && !found.includes(elf_rucksack_1[_j])){
                found.push(elf_rucksack_1[_j])   
                rucksack_sum += letters_priorities.indexOf(elf_rucksack_1[_j]) + 1
            }   
        }
    }
        
    console.log(rucksack_sum)
}

let input_data = fs.readFileSync('./day_3/input.txt', 'utf8');

let alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
// let rucksack = test_data.split('\n')
let rucksack = input_data.split('\r\n')

part_1(rucksack, alph)
part_2(rucksack, alph)

