arq = open('num.txt', 'r')
numeros = arq.read()
arq.close()



valores = numeros.split(',')

for x in range(0, valores.__sizeof__()):
    hexa = valores[x]
    base = 16
    num_of_bits = 8
    binario = bin(int(hexa, base))[2:].zfill(num_of_bits)
    print(binario)
