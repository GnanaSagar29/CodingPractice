num1=int(input())
num2=int(input())
if num2>99:
    num2 = 99
d = 0
for i in range (num1,num2+1):
    if i%15==0 and len(str(i))==2:
        c =i
        d=1
if d==0:
    print(-1)
else:
    print(c)
