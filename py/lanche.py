X, Y = map(int, input().split())

if X == 1:
    total = Y*4
elif X == 2:
    total = Y*4.50
elif X == 3:
    total = Y*5
elif X == 4:
    total = Y*2
elif X == 5:
    total = Y*1.50

print("Total: R$ %.2f" % total)
