n = int(input())
if n < 2:
    print("Not a Prime number")
elif n == 2:
    print("Prime number")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not a Prime number")
            break
    else:
        print("Prime number")
