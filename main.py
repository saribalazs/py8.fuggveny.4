'''
4. Feladat
Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is! 
Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét (0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!
'''


def negyzet_kerulet(a, b):
    elemzes = 0
    if b != '':
        for i in b:
            elemzes +=1
    elif b == '':
        a = 4*a
        return f"A négyzet kerülete: {a} cm"

def teglalap_kerulet(a, b):
    elemzes = 0
    if elemzes == 1:
        ertek = 0
        ossz = 0
        for i in b:
            ertek = i
        ossz = a + ertek
        ossz = ossz * 2
        return f"A téglalap kerülete: {ossz} cm"

def haromszog_kerulet(*args):
    elemzes = 0
    if elemzes == 2:
        ossz = 0
        args.append(args)
        for i in args:
            ossz += i
        return f"A hármszög kerülete: {ossz} cm"

def sokszog_kerulet(*args):
    elemzes = 0
    if elemzes > 2:
        ossz = 0
        args.append(args)
        for i in args:
            ossz += i
        return f"A sokszög kerülete: {ossz} cm"


while True:
    sikidom = input("Kérem adja meg miyen síkidomot szeretne megvizsgálni!")
    if sikidom == "négyzet":
        oldal = int(input("Kérem adja meg megkora a négyzet oldala"))
        negyzet_kerulet(oldal, )
        break
    
    elif sikidom == "téglalap":
        oldal1 = int(input("Kérem adja meg a téglalap másik oldalát!"))
        oldal2 = int(input("Kérem adja meg a téglalap másik oldalát!"))
        teglalap_kerulet(oldal1, oldal2)
        break
    
    elif sikidom == "háromszög":
        oldal1 = int(input("Kérem adja meg a háromszőg egyik oldalát!"))
        oldal2 = int(input("Kérem adja meg a háromszőg egyik oldalát!"))
        oldal3 = int(input("Kérem adja meg a háromszőg egyik oldalát!"))
        haromszog_kerulet(oldal1, oldal2, oldal3)

    elif sikidom == "sokszög":
        while True:
            oldal = int(input("Kérem adja meg a sokszög egyik oldalát!"))
            if oldal < 0:
                sokszog_kerulet(oldal)
        break
    
