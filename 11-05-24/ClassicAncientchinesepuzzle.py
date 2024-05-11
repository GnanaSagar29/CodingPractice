n_heads = int(input())
n_legs = int(input())
for n_chickens in range(n_heads + 1):
    n_rabbits = n_heads - n_chickens
    if 2 * n_chickens + 4 * n_rabbits == n_legs:
        print(n_chickens, n_rabbits)
        break
else:
    print("No solution")
