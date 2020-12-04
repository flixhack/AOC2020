#-----Password Part Two-----#
import lists

pas = 0
let = 0
min = 0
max = 0
app = 0
for i in lists.passList:
    pasE = lists.passList[pas]
    letE = lists.letList[let]
    minE = lists.minList[min]
    maxE = lists.maxList[max]
    if pasE[minE-1] == letE and not pasE[maxE-1] == letE or pasE[maxE-1] == letE and not pasE[minE-1] == letE:
        app = app + 1
        print(app)
    pas = pas + 1
    let = let + 1
    min = min + 1
    max = max + 1
