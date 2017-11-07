lines = [line.rstrip('\n') for line in open('ACESSOS/AcessoBinario.txt')]
bitTag = 3;
bitLinha = 4;
dado = 1;


linha0000 = [None] * 4
linha0001 = [None] * 4
linha0010 = [None] * 4
linha0011 = [None] * 4
linha0100 = [None] * 4
linha0101 = [None] * 4
linha0110 = [None] * 4
linha0111 = [None] * 4

linha1000 = [None] * 4
linha1001 = [None] * 4
linha1010 = [None] * 4
linha1011 = [None] * 4
linha1100 = [None] * 4
linha1101 = [None] * 4
linha1110 = [None] * 4
linha1111 = [None] * 4



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


    if linha == '0000':

        if linha0000[0]==tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
             linha0000[0] = tag

             print(pal)
             linha0000[1] = pal + "0"
             linha0000[2] = pal + "1"
             print('MISS')
             result += " MISS"
             countMiss += 1



    if linha == '0001':
        if linha0001[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha0001[0] = tag

            print(pal)
            linha0001[1] = pal + "0"
            linha0001[2] = pal + "1"

            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '0010':
        if linha0010[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1
        else:
            linha0010[0] = tag

            print(pal)
            linha0010[1] = pal + "0"
            linha0010[2] = pal + "1"

            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '0011':
        if linha0011[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha0011[0] = tag

            print(pal)
            linha0011[1] = pal + "0"
            linha0011[2] = pal + "1"


            print('MISS')
            result += " MISS"
            countMiss += 1
#######################################################################################
    if linha == '0100':
        if linha0100[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha0100[0] = tag

            print(pal)
            linha0100[1] = pal + "0"
            linha0100[2] = pal + "1"


            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '0101':
        if linha0101[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha0101[0] = tag

            print(pal)
            linha0101[1] = pal + "0"
            linha0101[2] = pal + "1"


            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '0110':
        if linha0110[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha0110[0] = tag

            print(pal)
            linha0110[1] = pal + "0"
            linha0110[2] = pal + "1"


            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '0111':
        if linha0111[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha0111[0] = tag

            print(pal)
            linha0111[1] = pal + "0"
            linha0111[2] = pal + "1"


            print('MISS')
            result += " MISS"
            countMiss += 1

###########################################################################################

    if linha == '1000':

        if linha1000[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha1000[0] = tag

            print(pal)
            linha1000[1] = pal + "0"
            linha1000[2] = pal + "1"
            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '1001':
        if linha1001[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha1001[0] = tag

            print(pal)
            linha1001[1] = pal + "0"
            linha1001[2] = pal + "1"

            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '1010':
        if linha1010[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1
        else:
            linha1010[0] = tag

            print(pal)
            linha1010[1] = pal + "0"
            linha1010[2] = pal + "1"

            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '1011':
        if linha1011[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha1011[0] = tag

            print(pal)
            linha1011[1] = pal + "0"
            linha1011[2] = pal + "1"

            print('MISS')
            result += " MISS"
            countMiss += 1
            #######################################################################################
    if linha == '1100':
        if linha1100[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha1100[0] = tag

            print(pal)
            linha1100[1] = pal + "0"
            linha1100[2] = pal + "1"

            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '1101':
        if linha1101[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha1101[0] = tag

            print(pal)
            linha1101[1] = pal + "0"
            linha1101[2] = pal + "1"

            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '1110':
        if linha1110[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha1110[0] = tag

            print(pal)
            linha1110[1] = pal + "0"
            linha1110[2] = pal + "1"

            print('MISS')
            result += " MISS"
            countMiss += 1

    if linha == '1111':
        if linha1111[0] == tag:
            print('HIT')
            result += " HIT"
            countHit += 1

        else:
            linha1111[0] = tag

            print(pal)
            linha1111[1] = pal + "0"
            linha1111[2] = pal + "1"

            print('MISS')
            result += " MISS"
            countMiss += 1










    print("LINHA ", 'TAG',"DADOS")
    print("0000    ", linha0000[0], linha0000[1], linha0000[2])
    print("0001    ", linha0001[0], linha0001[1], linha0001[2])
    print("0010    ", linha0010[0], linha0010[1], linha0010[2])
    print("0011    ", linha0011[0], linha0011[1], linha0011[2])
    print("0100    ", linha0100[0], linha0100[1], linha0100[2])
    print("0101    ", linha0101[0], linha0101[1], linha0101[2])
    print("0110    ", linha0110[0], linha0110[1], linha0110[2])
    print("0111    ", linha0111[0], linha0111[1], linha0111[2])

    print("1000    ", linha1000[0], linha1000[1], linha1000[2])
    print("1001    ", linha1001[0], linha1001[1], linha1001[2])
    print("1010    ", linha1010[0], linha1010[1], linha1010[2])
    print("1011    ", linha1011[0], linha1011[1], linha1011[2])
    print("1100    ", linha1100[0], linha1100[1], linha1100[2])
    print("1101    ", linha1101[0], linha1101[1], linha1101[2])
    print("1110    ", linha1110[0], linha1110[1], linha1110[2])
    print("1111    ", linha1111[0], linha1111[1], linha1111[2])
print(result)
print("TOTAL MISS", countMiss)
print("TOTAL HIT", countHit)


