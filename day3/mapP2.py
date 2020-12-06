#------Map part 2-----#
import map2

def treeCount(x , y):
    tree = 0
    for i in range(1, len(map2.map)):
        lineno = i * y
        if lineno > 322:
            break
        line = map2.map[i * y]
        charno = i * x % 31
        char = line[charno]
        if char == "#":
            tree = tree + 1
    return tree


tree1 = treeCount(1,1)
tree2 = treeCount(3,1)
tree3 = treeCount(5,1)
tree4 = treeCount(7,1)
tree5 = treeCount(1,2)
print(tree1, tree2, tree3, tree4, tree5)
print(tree1 * tree2 * tree3 * tree4 * tree5)
