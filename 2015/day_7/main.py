def read_input():
    with open('input.txt') as f:
        lines = f.readlines()
    
    cmd = []
    for line in lines:
        cmd.append(line.strip().split(" -> "))
    
    return cmd
    


OPERATORS = {
    None: lambda arg: arg(0),
    "NOT": lambda arg: ~arg(1),
    "AND": lambda arg: arg(0) & arg(2),
    "OR": lambda arg: arg(0) | arg(2),
    "LSHIFT": lambda arg: arg(0) << arg(2),
    "RSHIFT": lambda arg: arg(0) >> arg(2),
}


def get_def(key, instructions, known_def):
    for instruction in instructions:
        if instruction[1] == "a":
            known_def.append(instruction)


def main():
    instructions = read_input()
    # ['gj RSHIFT 5', 'gm']

    definitions = []
    
    get_def("lx", instructions, definitions)
    


    print(definitions)
    
    
    






    



if __name__ == '__main__':
    main()
