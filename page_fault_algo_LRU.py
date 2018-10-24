p = "7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1".split()
f = 4
ar = []
hit = 0
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
            q = []
            j = i - 1
            while len(q) != f:
                if p[j] not in q:
                    q.append(p[j])
                j -= 1
            l = len(q)
            x = q[l-1]
            ind = ar.index(x)
            ar[ind] = p[i]
            print(ar)

print("no of hit : {} and no. of page fault : {}".format(hit,len(p)-hit))
print("final array is {}".format(ar))




