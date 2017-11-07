lines = [line.rstrip('\n') for line in open('ACESSOS/AcessoBinario.txt')]
bitTag = 3;
bitLinha = 3;
dado = 2;


linha000 = [None] * 5
linha001 = [None] * 5
linha010 = [None] * 5
linha011 = [None] * 5
linha100 = [None] * 5
linha101 = [None] * 5
linha110 = [None] * 5
linha111 = [None] * 5



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


    if linha == '000':

        if linha000[0]==tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
             linha000[0] = tag

             print(pal)
             linha000[1] = pal + "00"
             linha000[2] = pal + "01"
             linha000[3] = pal + "10"
             linha000[4] = pal + "11"
             print('MISS')
             result += " MISS"
             countMiss += 1



    if linha == '001':
        if linha001[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha001[0] = tag

            print(pal)
            linha001[1] = pal + "00"
            linha001[2] = pal + "01"
            linha001[3] = pal + "10"
            linha001[4] = pal + "11"

            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '010':
        if linha010[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1
        else:
            linha010[0] = tag

            print(pal)
            linha010[1] = pal + "00"
            linha010[2] = pal + "01"
            linha010[3] = pal + "10"
            linha010[4] = pal + "11"

            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '011':
        if linha011[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha011[0] = tag

            print(pal)
            linha011[1] = pal + "00"
            linha011[2] = pal + "01"
            linha011[3] = pal + "10"
            linha011[4] = pal + "11"

            print('MISS')
            result += " MISS"
            countMiss += 1
#######################################################################################
    if linha == '100':
        if linha100[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha100[0] = tag

            print(pal)
            linha100[1] = pal + "00"
            linha100[2] = pal + "01"
            linha100[3] = pal + "10"
            linha100[4] = pal + "11"

            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '101':
        if linha101[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha101[0] = tag

            print(pal)
            linha101[1] = pal + "00"
            linha101[2] = pal + "01"
            linha101[3] = pal + "10"
            linha101[4] = pal + "11"

            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '110':
        if linha110[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha110[0] = tag

            print(pal)
            linha110[1] = pal + "00"
            linha110[2] = pal + "01"
            linha110[3] = pal + "10"
            linha110[4] = pal + "11"

            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '111':
        if linha111[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha111[0] = tag

            print(pal)
            linha111[1] = pal + "00"
            linha111[2] = pal + "01"
            linha111[3] = pal + "10"
            linha111[4] = pal + "11"

            print('MISS')
            result += " MISS"
            countMiss += 1


    print("LINHA ", 'TAG',"DADOS")
    print("000    ", linha000[0], linha000[1], linha000[2],linha000[3],linha000[4])
    print("001    ", linha001[0], linha001[1], linha001[2],linha001[3],linha001[4])
    print("010    ", linha010[0], linha010[1], linha010[2],linha010[3],linha010[4])
    print("011    ", linha011[0], linha011[1], linha011[2],linha011[3],linha011[4])
    print("100    ", linha100[0], linha100[1], linha100[2], linha100[3], linha100[4])
    print("101    ", linha101[0], linha101[1], linha101[2], linha101[3], linha101[4])
    print("110    ", linha110[0], linha110[1], linha110[2], linha110[3], linha110[4])
    print("111    ", linha111[0], linha111[1], linha111[2], linha111[3], linha111[4])
print(result)
print("TOTAL MISS",countMiss)
print("TOTAL HIT",countHit)


