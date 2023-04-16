n = int(input())

anos = n//365
n = n - anos * 365
meses = n//30
n = n - meses * 30
dias = n

print('%d ano(s)' % anos)
print('%d mes(es)' % meses)
print('%d dia(s)' % dias)
