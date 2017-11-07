lines = [line.rstrip('\n') for line in open('ACESSOS/AcessoBinario.txt')]
bitTag = 5;
dado = 3;


linha00 = [None] * 9
linha01 = [None] * 9
linha10 = [None] * 9
linha11 = [None] * 9

tag = [None] * 4

result = ''
countMiss = 0
countHit = 0
menos = 0
for x in range(0, len(lines)):

    hexa = lines[x]
    tg = hexa[0:int(bitTag)]
    palavra = hexa[int(bitTag): int(dado) + int(bitTag)]
    print("tag", tg, "palavra", palavra)

    for i in range (0, len(tag)): #PROCURA NA MEMORIA ASSOCIATIVA
        if tag[i] == tg:
            print ("HIT")

        if tag[i] == None:
            tag[i] = tg
            menos = 0
            print ("MISS")

        else:
            tag[menos] = tg