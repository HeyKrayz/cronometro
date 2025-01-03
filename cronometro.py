from time import sleep

segundos = 0
minutos = 0
horas = 0

while True:
    sleep(1)
    segundos += 1
    if segundos == 60:
        minutos = 1
        segundos = 0
    if minutos == 60:
        horas = 1
        minutos = 0
    print (f'horas: {horas} minutos: {minutos} segundos: {segundos}')