


test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def read_input():
    with open('input.txt') as f:
        file = f.read()
    
    return file


'''PART 01'''
def part_1(fs):
    total=0
    grandtotal=0
    for a,b in fs:
        if a[-1:]=='/': # directory
            for c,d in fs:
                if c.find(a) != -1 : # this file lives inside the directory
                    total+=d
            if total<=100000:
                grandtotal+=total
            total=0
    print('part 01: ',grandtotal)


def main():
    # data = test_input.splitlines()
    data = open("input.txt", "r", encoding="utf-8").read().splitlines()
    
    fs = [] #['/a/b/c/file|dir, size'],[...],[...]
    filepath = []
    
    for d in data:
        a = d.strip().split()
        if a[0] == '$':
            if a[1] =='cd':
                if a[2] == '..':
                    filepath.pop()
                else:
                    if a[2] == '/': a[2]=''
                    filepath.append(a[2] + '/')
        elif a[0] == 'dir':
            fs.append( [ ''.join(map(str,filepath)) + a[1] + '/' , 0] )
        else:
            fs.append( [ ''.join(map(str,filepath)) + a[1], int(a[0]) ] )
    
    fs.sort()
    for f in fs:
        print(*f)
 
    part_1(fs)


if __name__ == '__main__':
    main()