lines = [line.rstrip('\n') for line in open('ACESSOS/AcessoBinario.txt')]
bitTag = 5;
dado = 3;




tag = [None] * 5

result = ''
countMiss = 0
countHit = 0
count=1;
primeira = True
aux = False

for x in range(0, len(lines)):

    hexa = lines[x]
    tg = hexa[0:int(bitTag)]
    palavra = hexa[int(bitTag): int(dado) + int(bitTag)]
    print("tag", tg, "palavra", palavra)


    for i in range (0, len(tag)):
        if tag[i] == tg:
            print ("HIT")
            result += " HIT"
            aux = True
            break
        else:
            if tag[i] == None:
                tag[i] = tg
                print("MISS")
                result += " MISS"
                aux = True
                break


    if aux == False:
        tag[count] = tg
        print("MISS")
        result += " MISS"
        if count == 4:
            count = 0
        else:
            count += 1


    aux=False
print(tag[0],tag[1],tag[2],tag[3],tag[4])
print (result)


