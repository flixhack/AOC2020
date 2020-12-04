#-------Password-----#
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
    if pasE.count(letE) >= minE and pasE.count(letE) <= maxE:
        app = app + 1
        print(app)
    pas = pas + 1
    let = let + 1
    min = min + 1
    max = max + 1
