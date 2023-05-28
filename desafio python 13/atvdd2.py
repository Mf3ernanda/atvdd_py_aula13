def calcula_fatorial(numero):
    if numero < 0:
        return None
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial
numero = int(input("Por favor, digite um número inteiro para calcular o fatorial: "))
resultado = calcula_fatorial(numero)

print("O fatorial de", numero, "é:", resultado)