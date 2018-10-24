p = "a b c d c a d b e b a b c d".split()
f = 4
ar = []
hit = 0
ins = 0
print("array steps :")
for i in range(len(p)):
    if i < f:
        ar.append(p[i])
        print(ar)
    else:
        if p[i] in ar:
            hit += 1
            print(ar)
        else:
            if ins < f:
                ar[ins] = p[i]
                ins += 1
                print(ar)
            else:
                ins = 0
                ar[ins] = p[i]
                print(ar)
print("no of hit : {} and no. of page fault : {}".format(hit,len(p)-hit))
print("final array is {}".format(ar))




