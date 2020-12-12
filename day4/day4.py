batchfile = open("C:/Users/felix/Documents/Adventofcode/AOC2020/day4/passbatch.txt")

def passSplit():
    batch = batchfile.read()
    contentSplit = batch.split("\n\n")
    return contentSplit

passlist = passSplit()

def checkTrue():
    ap = 0
    for i in range(len(passlist)):
        checking = passlist[i]
        tf = "ecl" in checking and "pid" in checking and "eyr" in checking and  "hcl" in checking and "byr" in checking and "iyr" in checking and "hgt" in checking
        if tf == True:
            ap = ap +1
            print(checking + " = true\n")
        else:
            print(checking + " = false\n")
    return ap

a = checkTrue()
print(a)
