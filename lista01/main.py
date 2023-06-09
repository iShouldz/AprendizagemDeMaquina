teste = open('car.txt', 'r')
print(teste.readline())
print(teste.readline().split(',')[6])

for i in teste:
    #print(i.split(',')[6])
    if str(i.split(',')[6]) != 'unacc':
        print('yes')
