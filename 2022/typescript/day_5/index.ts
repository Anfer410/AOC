import { Deque } from '@blakeembrey/deque'
import * as fs from 'fs';

const test_data=`    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2`



function transform_stack(crates_stack){
    let index = crates_stack[crates_stack.length -1].split('  ');
    
    let stacks: Array<string> = [];
    for(var _i=0; _i < crates_stack.length - 1; _i++ ){
        stacks.push(crates_stack[_i]);};

    let vertical_stack: Array<any> = []
    let curr = 0
    for(var _x=0; _x<index.length; _x++){
        
        let stack = new Deque();
        
        for(var _l in stacks){
            let letter = stacks[_l].substring(curr+1,curr+2);
            if(letter != '' && letter != ' ' ){
                stack.pushLeft(letter)
             };
            
        }
        curr += 4
        vertical_stack.push(stack)        
    }

    return vertical_stack
}


function move_crates(crates, instructions, part){
    let crates_stack = crates.split('\n');
    let vertical_stacks = transform_stack(crates_stack);
    
    instructions = instructions.split('\n')

    for(var _instruction in instructions){
        let inst = instructions[_instruction].split(' ');
    
        let n_of_crates = Number(inst[1]);
        let original_stack = Number(inst[3]) - 1;
        let new_stack = Number(inst[5]) - 1;

        if(n_of_crates > 1 && part != 1){
            let temp_q = new Deque();
            for(var _i=0; _i < n_of_crates; _i++){
                if(vertical_stacks[original_stack]){
                    temp_q.push(vertical_stacks[original_stack].pop())}
            }
            
            for(var _i=0; _i < n_of_crates; _i++){
                if(temp_q){
                    vertical_stacks[new_stack].push(temp_q.pop())}
            }
        } else {
            for(var _i=0; _i < n_of_crates; _i++){
                if(vertical_stacks[original_stack].size > 0){
                    vertical_stacks[new_stack].push(vertical_stacks[original_stack].pop())}
            }
        }
    }
    
    let word = ''
    for(var _i=0; _i < vertical_stacks.length; _i++){
        if(vertical_stacks[_i]){
            word += vertical_stacks[_i].peek(-1)
        }
    }
    console.log('Part ', part, ' : ', word)
    
}
        

        
    
let input_data = fs.readFileSync('./day_5/input.txt', 'utf8');



let [crates, instructions] = input_data.split('\r\n\r\n')
// let [crates, instructions] = test_data.split('\n\n')


move_crates(crates, instructions, 1)
move_crates(crates, instructions, 2)



