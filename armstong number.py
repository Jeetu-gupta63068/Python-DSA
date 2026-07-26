n=153
num=n
total=0
node=len(str(n))
while num>0:
    ld=num%10
    total=total+(ld**node)
    num=num//10
    print(total)