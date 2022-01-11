n = int(input())
l = [0, 1]
for i in range(n):
    l.append(int(l[-2])+int(l[-1]))
print(l[-2])