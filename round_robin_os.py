p = ['a','b','c']
bt = [7,6,4]
q = 4
wt = [0,0,0]
et = [0,0,0]
s = [0,0,0]
rt = bt
i = 0
print("process : ",end=' ')
while rt != s:
    if rt[i] >= q:
        rt[i] = rt[i] - q
        print(p[i],end=' ')
        if i == 2:
            i = -1
        if rt[i+1] != 0:
            wt[i+1] = wt[i+1] + q
        if i == 1:
            i = -2
        if rt[i+2] != 0:
            wt[i+2] = wt[i+2] + q
        print(wt[i],rt[i])
    elif rt[i] < q and rt[i] != 0:
        if i == 2:
            i = -1
        if rt[i+1] != 0:
            wt[i+1] = wt[i+1] + rt[i]
        if i == 1:
            i = -2
        if rt[i+2] != 0:
            wt[i+2] = wt[i+2] + rt[i]
        print(p[i],end=' ')
        rt[i] = 0
        print(wt[i],rt[i])
    else:
        continue
    i += 1
print("\nremaining time is :{}".format(rt))
print("waiting time is : {}".format(wt))