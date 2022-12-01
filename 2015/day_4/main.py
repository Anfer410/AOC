import sys
import hashlib

sys.path.append('../AOCUtils')
import utils

day = 4


def gen_secretkey(message):
    result = hashlib.md5(message.encode())
    return result.hexdigest()

def find_lowest_secret(message, part=1):
    if part == 1:
        leeding_zeeros = '00000'
    if part == 2:
        leeding_zeeros = '000000'
    number = 0
    i = 0
    hex_digest = '1111000000000'
    while hex_digest[:len(leeding_zeeros)] != leeding_zeeros:
        number = number + 1
        i += 1
        hex_digest = gen_secretkey(message+str(number))
        if i%100000 == 0:
            print(f'op: {i}, Hex: {hex_digest}')
        

    return hex_digest, number

def main():    
    task_input = utils.read_input(4)
    # task_input = 'pqrstuv'
    
    hex, num = find_lowest_secret(task_input)
    print(f'Hex: {hex}, Num: {num}, Message: {task_input+str(num)}')
    
    hex, num = find_lowest_secret(task_input, part=2)
    print(f'Hex: {hex}, Num: {num}, Message: {task_input+str(num)}')
    
    
    

    


if __name__ == '__main__':
    main()