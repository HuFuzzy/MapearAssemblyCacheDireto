
lines = [line.rstrip('\n') for line in open('ACESSOS/AcessoBinario.txt')]
bitTag = input("BITS PARA TAG");
bitLinha = input("BITS PARA LINHA");
dado = input("BITS PARA PALAVRA");

for x in range(0, len(lines)):

    hexa = lines[x]
    tag = hexa[0:int(bitTag)]
    linha = hexa[int(bitTag):int(bitLinha) + int(bitTag)]
    palavra = hexa[int(bitLinha) + int(bitTag): int(dado) + int(bitLinha) + int(bitTag)]
    print("tag",tag,"linha", linha,"palavra", palavra)
