num1, num2, num3 = list(map(int, input().split()))

numbers = [num1, num2, num3]

numbers.sort()

for i in range(len(numbers)):
    print(numbers[i])

print()
print(num1)
print(num2)
print(num3)
