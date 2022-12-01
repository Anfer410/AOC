from collections import defaultdict

def mapl(f, iterable):
    return list(map(f, iterable))

def read_input(filename, datatype=str, sep='\n'):
    with open(filename) as f:
        contents = f.read().strip().split(sep)
        return mapl(datatype, contents)


def traverse(can_twice, a='start', seen={'start'}):
    if a == 'end': yield 1
    else:
        for b in connections[a]:
            if b.islower():
                if b not in seen:
                    yield from traverse(can_twice, b, seen | {b})
                elif can_twice and b not in {'start', 'end'}:
                    yield from traverse(False, b, seen)
            else:
                yield from traverse(can_twice, b, seen)


connections = defaultdict(list)
for line in read_input("Day_12/input.txt"):
    a, b = line.split('-')
    connections[a].append(b)
    connections[b].append(a)

print(sum(traverse(can_twice=False)))
print(sum(traverse(can_twice=True)))