n=[5,5,43,5,6,4,6,4,5,4]
m=[45,6,3,2,4,5,3]

for num in m:
    count=0
    for x in n:
        if x ==num:
            count+=1
            print(count)