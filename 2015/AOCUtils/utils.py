def read_input(day_num, read_type='f'):
    file = f'../day_{day_num}/input.txt'
    
    if read_type == 'f':
        with open(file) as f:
            content = f.read()
        
    elif read_type == 'l':
        with open(file) as f:
            lines = f.readlines()
            content = []
        for line in lines:
            content.append(line.strip())

    return content