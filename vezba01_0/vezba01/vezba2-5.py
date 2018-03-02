import sys
dict={'kljucna_rec' : 'amet'}
fin = open('dict_test.txt', 'r')
x=0
for line in fin:
    if dict['kljucna_rec'] in line.split():
        x+=1
print("broj ponavljanja je",x)
fin.close()