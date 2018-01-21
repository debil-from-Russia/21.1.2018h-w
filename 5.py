step = 1
x = int(input())
total=0
while not step>11:
    total+=((x**step)/step)
    step+=2
print(total)
    