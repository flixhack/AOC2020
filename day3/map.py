#------Map-----#
import map2

tree = 0
x = 3
for i in range(len(map2.map)):
    line = map2.map[i]
    char = line[i * x % 31]
    if char == "#":
        tree = tree + 1
    print(tree)
    
