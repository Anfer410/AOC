"use strict";
exports.__esModule = true;
var deque_1 = require("@blakeembrey/deque");
var fs = require("fs");
var test_data = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2";
function transform_stack(crates_stack) {
    var index = crates_stack[crates_stack.length - 1].split('  ');
    var stacks = [];
    for (var _i = 0; _i < crates_stack.length - 1; _i++) {
        stacks.push(crates_stack[_i]);
    }
    ;
    var vertical_stack = [];
    var curr = 0;
    for (var _x = 0; _x < index.length; _x++) {
        var stack = new deque_1.Deque();
        for (var _l in stacks) {
            var letter = stacks[_l].substring(curr + 1, curr + 2);
            if (letter != '' && letter != ' ') {
                stack.pushLeft(letter);
            }
            ;
        }
        curr += 4;
        vertical_stack.push(stack);
    }
    return vertical_stack;
}
function move_crates(crates, instructions, part) {
    var crates_stack = crates.split('\n');
    var vertical_stacks = transform_stack(crates_stack);
    instructions = instructions.split('\n');
    for (var _instruction in instructions) {
        var inst = instructions[_instruction].split(' ');
        var n_of_crates = Number(inst[1]);
        var original_stack = Number(inst[3]) - 1;
        var new_stack = Number(inst[5]) - 1;
        if (n_of_crates > 1 && part != 1) {
            var temp_q = new deque_1.Deque();
            for (var _i = 0; _i < n_of_crates; _i++) {
                if (vertical_stacks[original_stack]) {
                    temp_q.push(vertical_stacks[original_stack].pop());
                }
            }
            for (var _i = 0; _i < n_of_crates; _i++) {
                if (temp_q) {
                    vertical_stacks[new_stack].push(temp_q.pop());
                }
            }
        }
        else {
            for (var _i = 0; _i < n_of_crates; _i++) {
                if (vertical_stacks[original_stack].size > 0) {
                    vertical_stacks[new_stack].push(vertical_stacks[original_stack].pop());
                }
            }
        }
    }
    var word = '';
    for (var _i = 0; _i < vertical_stacks.length; _i++) {
        if (vertical_stacks[_i]) {
            word += vertical_stacks[_i].peek(-1);
        }
    }
    console.log('Part ', part, ' : ', word);
}
var input_data = fs.readFileSync('./day_5/input.txt', 'utf8');
var _a = input_data.split('\r\n\r\n'), crates = _a[0], instructions = _a[1];
// let [crates, instructions] = test_data.split('\n\n')
move_crates(crates, instructions, 1);
move_crates(crates, instructions, 2);
