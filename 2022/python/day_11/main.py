import operator as op
import math
from fractions import Fraction
import numpy as np

ops = {'+': op.add, '-': op.sub, '*': op.mul}

test_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

day_input = """Monkey 0:
  Starting items: 57, 58
  Operation: new = old * 19
  Test: divisible by 7
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 66, 52, 59, 79, 94, 73
  Operation: new = old + 1
  Test: divisible by 19
    If true: throw to monkey 4
    If false: throw to monkey 6

Monkey 2:
  Starting items: 80
  Operation: new = old + 6
  Test: divisible by 5
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 3:
  Starting items: 82, 81, 68, 66, 71, 83, 75, 97
  Operation: new = old + 5
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 2

Monkey 4:
  Starting items: 55, 52, 67, 70, 69, 94, 90
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 3

Monkey 5:
  Starting items: 69, 85, 89, 91
  Operation: new = old + 7
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 7

Monkey 6:
  Starting items: 75, 53, 73, 52, 75
  Operation: new = old * 7
  Test: divisible by 2
    If true: throw to monkey 0
    If false: throw to monkey 4

Monkey 7:
  Starting items: 94, 60, 79
  Operation: new = old + 2
  Test: divisible by 3
    If true: throw to monkey 1
    If false: throw to monkey 6
"""

data = test_input.split('\n\n')
# data = day_input.split('\n\n')

monkeys = {}

for details in data:
    
    monkey = details.split('\n')
    id = int(monkey[0].split()[1].replace(':',''))
    items = [int(i) for i in  monkey[1].split(':')[1].split(',')]    
    operation = monkey[2].split(':')[1].strip()
    test = int(monkey[3].split(':')[1].split()[2])
    true_result = int(monkey[4].split(':')[1].split()[3])
    false_result = int(monkey[5].split(':')[1].split()[3])
    
    monkeys.update({id:{
        'items': items,
        'operation': operation,
        'test': test,
        'true_result': true_result, 
        'false_result': false_result,
        'counter': 0
    }})

    
for round in range(20):
    for id in monkeys:
        print(f'Processing {id}, round {round}')
        # print(monkeys[id]['items'])
        for i in range(len(monkeys[id]['items'])):
            monkeys[id]['counter'] += 1
            
            worry_level = monkeys[id]['items'].pop()
            
            operation = monkeys[id]['operation'].split()
            if operation[4] == 'old':
                x = worry_level
            else:
                x = int(operation[4])

            new_worry_level = ops[operation[3]](worry_level, x)
            not_damaged = np.fix(np.floor_divide(new_worry_level, 3))

            if (not_damaged % monkeys[id]['test']) == 0 :
                monkeys[monkeys[id]['true_result']]['items'].append(not_damaged)
            else:
                monkeys[monkeys[id]['false_result']]['items'].append(not_damaged)




print(sorted([monkeys[monkey]['counter'] for monkey in monkeys], reverse=True))
x,y = sorted([monkeys[monkey]['counter'] for monkey in monkeys], reverse=True)[:2]

print(f'Part 1: {x*y}')
    