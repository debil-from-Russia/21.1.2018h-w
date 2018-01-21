minus = False
zn = 1
total = 1
n = int(input())
while not zn>n:
    pre = 1/zn
    if minus:
        total-=pre
        minus = False
    else:
        total+=pre
        minus = True
    zn+=1
print(total)