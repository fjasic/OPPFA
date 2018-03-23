import sys
lista=[]
torka1=tuple(int(x) for x in input('unesi 4 integera: ').split(' '))
torka2=tuple(float(x) for x in input('unesi 4 floata: ').split(' '))
torka3=tuple(x for x in input('unesi 4 stringa: ').split(' '))
print('integeri su: ',torka1)
print('floatovi su: ',torka2)
print('stringovi su: ',torka3)
lista.append(torka1)
lista.append(torka2)
lista.append(torka3)
print('lista je : ',lista)

