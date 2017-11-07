lines = [line.rstrip('\n') for line in open('ACESSOS/AcessoBinario.txt')]
bitTag = input("BITS PARA TAG");
bitLinha = input("BITS PARA LINHA");
dado = input("BITS PARA PALAVRA");


linha00 = [None] * 9
linha01 = [None] * 9
linha10 = [None] * 9
linha11 = [None] * 9
result = ''
countMiss = 0
countHit = 0
for x in range(0, len(lines)):

    hexa = lines[x]
    tag = hexa[0:int(bitTag)]
    linha = hexa[int(bitTag):int(bitLinha) + int(bitTag)]
    palavra = hexa[int(bitLinha) + int(bitTag): int(dado) + int(bitLinha) + int(bitTag)]
    print("tag", tag, "linha", linha, "palavra", palavra)
    pal = tag + linha
    if linha == '00':

        if linha00[0]==tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
             linha00[0] = tag

             print(pal)
             linha00[1] = pal + "000"
             linha00[2] = pal + "001"
             linha00[3] = pal + "010"
             linha00[4] = pal + "011"
             linha00[5] = pal + "100"
             linha00[6] = pal + "101"
             linha00[7] = pal + "110"
             linha00[8] = pal + "111"
             print('MISS')
             result += " MISS"
             countMiss += 1



    if linha == '01':
        if linha01[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha01[0] = tag

            print(pal)
            linha01[1] = pal + "000"
            linha01[2] = pal + "001"
            linha01[3] = pal + "010"
            linha01[4] = pal + "011"
            linha01[5] = pal + "100"
            linha01[6] = pal + "101"
            linha01[7] = pal + "110"
            linha01[8] = pal + "111"
            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '10':
        if linha10[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1
        else:
            linha10[0] = tag

            print(pal)
            linha10[1] = pal + "000"
            linha10[2] = pal + "001"
            linha10[3] = pal + "010"
            linha10[4] = pal + "011"
            linha10[5] = pal + "100"
            linha10[6] = pal + "101"
            linha10[7] = pal + "110"
            linha10[8] = pal + "111"
            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '11':
        if linha11[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha11[0] = tag

            print(pal)
            linha11[1] = pal + "000"
            linha11[2] = pal + "001"
            linha11[3] = pal + "010"
            linha11[4] = pal + "011"
            linha11[5] = pal + "100"
            linha11[6] = pal + "101"
            linha11[7] = pal + "110"
            linha11[8] = pal + "111"
            print('MISS')
            result += " MISS"
            countMiss += 1

    print("LINHA ", 'TAG',"DADOS")
    print("00    ", linha00[0], linha00[1], linha00[2],linha00[3],linha00[4],linha00[5],linha00[6],linha00[7],linha00[8])
    print("01    ", linha01[0], linha01[1], linha01[2],linha01[3],linha01[4],linha01[5],linha01[6],linha01[7],linha01[8])
    print("10    ", linha10[0], linha10[1], linha10[2],linha10[3],linha10[4],linha10[5],linha10[6],linha10[7],linha10[8])
    print("11    ", linha11[0], linha11[1], linha11[2],linha11[3],linha11[4],linha11[5],linha11[6],linha11[7],linha11[8])
print(result)
print("TOTAL MISS",countMiss)
print("TOTAL HIT",countHit)


