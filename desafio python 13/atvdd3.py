def converte_tempo(tempo_segundos):
    horas = tempo_segundos // 3600
    minutos = (tempo_segundos % 3600) // 60
    segundos = tempo_segundos % 60

    return "{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos)
tempo_segundos = int(input("Digite um valor inteiro representando um tempo em segundos: "))
tempo_formatado = converte_tempo(tempo_segundos)
print("O tempo convertido é: " + tempo_formatado)