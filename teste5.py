palavra = input('Insira a palavra a ser invertida: ')
tamanho_palavra = len(palavra)

palavra_invertida = ['']*tamanho_palavra

for i in range(tamanho_palavra):
    palavra_invertida[tamanho_palavra-1-i] = palavra[i]

palavra_invertida = "".join(palavra_invertida)
print("")
print(palavra_invertida)
print("")