n = int(input())
total = 1
counter = 2
while not counter>n:
    total+=(1/counter)
    counter+=1
print(total)