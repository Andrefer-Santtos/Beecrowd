horaInicial, minutoInicial, horaFinal, minutoFinal = list(map(int, input().split()))

tempo = ((horaFinal*60)+minutoFinal)-((horaInicial*60)+minutoInicial)
if (tempo <= 0):
    tempo += 24*60

horas = tempo//60
minutos = tempo % 60

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (horas, minutos))
