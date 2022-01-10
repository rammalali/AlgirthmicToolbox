#import time
#start = time.time()


def MaxPairwise():
    index1 = 0
    res = l[0]*l[0]
    for i in range(0, len(l)):
        for j in range(0, len(l)):
                res = max(res, l[i]*l[j])
    return res
def fastMaxPairwise():
    index1 = 0
    index2 = 0
    for i in range(len(l)):
        if l[i]>l[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for j in range(len(l)):
        if l[j]>l[index2] and j != index1:
            index2 = j
    return int(l[index1]) * int(l[index2])
nb = input()
input1 = input()
l = []
for x in input1.split():
    l.append(int(x))
#print(l)
res = fastMaxPairwise()
print(res)

#end = time.time()
#print(end-start)