x = int(input())
ch = 2
zn = 3
step = 1
minus = True
total = 0
while not step>10:
    pre = (ch/zn)*(x**step)
    if minus:
        total-=pre
        minus = False
    else:
        total+=pre
        minus = True
    step+=1
    ch+=1
    zn+=1
print(total)