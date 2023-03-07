def calcula_sequencia_fibonacci(numero_declarado):
    sequencia_fibonacci = [1,1]
    numero_fibonacci = 0
    i = 2

    while(numero_fibonacci < numero_declarado):
        numero_fibonacci = sequencia_fibonacci[i-2] + sequencia_fibonacci[i-1]
        sequencia_fibonacci.append(numero_fibonacci)
        i += 1

    for numero in sequencia_fibonacci:
        if(numero == numero_declarado):
            print(f'O numero {numero_declarado} pertence à sequência de Fibonacci')
        elif(numero > numero_declarado):
            print(f'O numero {numero_declarado} não pertence à sequência de Fibonacci')
        else: pass


print("")
numero_declarado = int(input('Qual o número deseja saber se faz parte da sequência de Fibonacci: '))
calcula_sequencia_fibonacci(numero_declarado)
print("")