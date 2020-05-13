from collections import Counter
autok = []
igenyek = []
def readfiles(name,listname):
    f1 = open(name,'r',encoding='ISO-8859-1')
    for eachline in f1:
        listname.append(eachline.strip('\n').split(';'))
    f1.close
readfiles('autok.csv',autok)

#Feladat_2
print('2. feladat\n  ', len(autok)-1,'autos hirdet fuvart')

#Feladat_3
Osszes = 0
for each_adat in autok:
    if each_adat[0] == 'Budapest' and each_adat[1] == 'Miskolc':
        Osszes += 1
print('3. feladat\n', '  Osszesen',Osszes,'ferohelyet hirdettek')

#Feladat_4
lehetosegek = []
for chance in autok:
    lehetosegek.append((chance[0],chance[1]))
Most_count = Counter(lehetosegek)
Most = Most_count.most_common(1)
print('4. feladat')
print('  A legtobb herohelyet  (' + str(Most[0][1]) + '-at) a ' + Most[0][0][0] + '-' + Most[0][0][1] + ' kozott ajanlottak fel a hirdetok')

#Feladat_5
readfiles('igenyek.csv',igenyek)
autok.remove(autok[0])
igenyek.remove(igenyek[0])
print('5. feladat')
for i in igenyek:
    for each in autok:
        if i[1]+i[2] == each[0]+each[1] and int(i[3]) <= int(each[4]):
            print('   '+i[0]+' => '+each[2])
            break
        
#Feladat_6
print('6. feladat')
f2 = open('utasuzenetek.txt','w')
for i in igenyek:
    for each in autok:
        if i[1]+i[2] == each[0]+each[1] and int(i[3]) <= int(each[4]):
            f2.write(i[0]+': Rendszam:'+each[2]+', Telefonszam:'+each[3]+'\n')
            break
    f2.write(i[0]+': Sajnos nem sikerult autot talalni\n')
f2.close
