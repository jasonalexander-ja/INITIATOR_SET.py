#counts Gs and Cs in sequence
def countG(mrna):
    return mrna.count(3)
def countC(mrna):
    return mrna.count(2)

#returns if a specific index is a G or C
def isg(ind):
    return ind == 3
def isc(ind):
    return ind == 2

#something for score calculation
def magiccalculator(distance,istarget):
    if istarget:
        return 5/distance
    else:
        return -1/distance

#gets concentration scores for G and C
def gscore(mrna,index):
    gscore = isg(mrna[index])*5
    for i in range(len(mrna)):
        if i-index != 0:
            gscore += magiccalculator(abs(i-index),isg(mrna[i]))
    return gscore
def cscore(mrna,index):
    cscore = isc(mrna[index])*5
    for i in range(len(mrna)):
        if i-index != 0:
            cscore += magiccalculator(abs(i-index),isc(mrna[i]))
    return cscore

#gets the points at which the concentrations are above a specific threshold
def addresses(scores,threshold):
    points = []
    for i in range(len(scores)):
        if scores[i] >= threshold:
            points.append(i)
    return points


#main function
mrna = [] #temporary
score_threshold = 0 #temporary
gCount = countG(mrna)
cCount = countC(mrna)
gscores = []
cscores = []
for i in range(len(mrna)):
    gscores.append(gscore(mrna,i))
    cscores.append(cscore(mrna,i))
highest_g = addresses(gscores,score_threshold)
highest_c = addresses(cscores,score_threshold)
