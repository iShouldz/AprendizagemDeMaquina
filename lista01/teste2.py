unacc = acc = good = vgood = 0
totalrealunacc = totalrealacc = totalrealgood = totalrealvgood = 0
carros = open('car.txt', 'r')
print(carros.readline())
for x in carros:
    if((x.split(',')[0] == 'vhigh' and x.split(',')[1] == 'vhigh') or
            (x.split(',')[0] == 'high' and x.split(',')[1] == 'high') and x.split(',')[6] == 'unacc'):
        unacc += 1
    elif ((x.split(',')[0] == 'med' and x.split(',')[1] == 'med') or
        (x.split(',')[0] == 'med' and x.split(',')[1] == 'high') and x.split(',')[6] == 'acc'):
        acc += 1
    elif ((x.split(',')[0] == 'low' and x.split(',')[1] == 'low') or
          (x.split(',')[0] == 'low' and x.split(',')[1] == 'med') and x.split(',')[6] == 'good'):
       good += 1
    elif(x.split(',')[4] == 'big' and x.split(',')[5] == 'high' and x.split(',')[6] == 'vgood'):
        vgood += 1


for k in carros:
    print(k.split(',')[6])
    if(k.split(',')[6] == 'unacc'):
        totalrealunacc += 1
    elif(k.split(',')[6] == 'acc'):
        totalrealacc += 1
    elif(k.split(',')[6] == 'good'):
        totalrealgood +=1
    else:
        totalrealvgood += 1


print("Acertos de unacc: " + str(unacc) + "/1209")
print("Acertos de acc: " + str(acc) + "/384")
print("Acertos de good: " + str(good) + "/69")
print("Acertos de vgood: " + str(vgood) + "/65")