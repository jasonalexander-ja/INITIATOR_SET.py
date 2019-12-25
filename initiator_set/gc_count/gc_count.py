def countG(mrna):
    return mrna.count(3)
def countC(mrna):
    return mrna.count(2)

def isg(ind):
    return ind == 3
def isc(ind):
    return ind == 2

def magiccalculator(curscore,distance,istarget):
    if istarget:
        return curscore + 5/distance
    else
        return curscore - 1/distance

def gscore(mrna,index):
    gscore = isg(mrna[index])*5
    for i in range(len(mrna)):
        if i-index != 0:
            gscore = magiccalculator(gscore,abs(i-index),isg(mrna[i]))
    return gscore

def cscore(mrna,index):
    cscore = isc(mrna[index])*5
    for i in range(len(mrna)):
        if i-index != 0:
            cscore = magiccalculator(cscore,abs(i-index),isc(mrna[i]))
    return cscore


def addresses(scores,treshold):
    points = []
    for i in range(len(scores)):
        if scores[i] >= treshold:
            points.append(i)
    return points

mrna = [] #temporary
gCount = countG(mrna)
cCount = countC(mrna)
gscores = []
cscores = []
for i in range(len(mrna)):
    gscores.append(gscore(mrna,i))
    cscores.append(cscore(mrna,i))
score_treshold = 0 #temporary
highest_g = addresses(gscores,score_treshold)
highest_c = addresses(cscores,score_treshold)