n = float(input())

n100 = n // 100
n = n - n100*100

n50 = n // 50
n = n - n50*50

n20 = n // 20
n = n - n20*20

n10 = n // 10
n = n - n10*10

n5 = n // 5
n = n - n5*5

n2 = n // 2
n = n - n2*2

n1 = n // 1
n = n - n1*1

m50 = n // 0.5
n = n - m50*0.5

m25 = n // 0.25
n = n - m25*0.25

m10 = n // 0.10
n = n - m10*0.10

m5 = n // 0.05
n = n - m5*0.05

m1 = n * 100

print('NOTAS:')
print('%d nota(s) de R$ 100.00' % n100)
print('%d nota(s) de R$ 50.00' % n50)
print('%d nota(s) de R$ 20.00' % n20)
print('%d nota(s) de R$ 10.00' % n10)
print('%d nota(s) de R$ 5.00' % n5)
print('%d nota(s) de R$ 2.00' % n2)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' % n1)
print('%d moeda(s) de R$ 0.50' % m50)
print('%d moeda(s) de R$ 0.25' % m25)
print('%d moeda(s) de R$ 0.10' % m10)
print('%d moeda(s) de R$ 0.05' % m5)
print('%d moeda(s) de R$ 0.01' % m1)
