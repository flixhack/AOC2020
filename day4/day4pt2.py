batchfile = open("C:/Users/felix/Documents/Adventofcode/AOC2020/day4/passbatch.txt")

def passSplit():
    batch = batchfile.read()
    contentSplit = batch.split("\n\n")
    return contentSplit


def checkTrue():
    controlList = []
    ap = 0
    for i in range(len(passlist)):
        checking = passlist[i]
        tf = "ecl" in checking and "pid" in checking and "eyr" in checking and  "hcl" in checking and "byr" in checking and "iyr" in checking and "hgt" in checking
        if tf == True:
            ap = ap +1
            # print(checking + " = true\n")
            controlList.append(checking)
        else:
            pass# print(checking + " = false\n")
    return controlList
    # return ap


def check2():
    pass



passlist = passSplit()
controlList = checkTrue()
hl = controlList
print(len(controlList[0]))
hl = [i.split(" ")[0] for i in controlList]
hl = [i.split("\n")[0] for i in controlList]
# a = split2()
print(hl)
