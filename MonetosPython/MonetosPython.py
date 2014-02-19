import time
class Moneta:
    verte = 0
    svoris = 0
    def __init__(self, v, s):
        self.verte = v
        self.svoris = s

def sprendimas(svoris, monetos, comparator):
    vertes = [-1] * (svoris + 1)
    for moneta in monetos:
        if(comparator(vertes[moneta.svoris], moneta.verte) or vertes[moneta.svoris] == -1):
            vertes[moneta.svoris] = moneta.verte
    
    for i in range(1, svoris + 1):
        for moneta in monetos:
            if(i - moneta.svoris > 0):
                if(vertes[i] == -1 or comparator(vertes[i - moneta.svoris] + moneta.verte, vertes[i])):
                    if(vertes[i - moneta.svoris] != -1):
                        vertes[i] = vertes[i - moneta.svoris] + moneta.verte
    return vertes[svoris]

def skaitymas(filename):
    file = open(filename)
    s = int(file.readline())
    m = int(file.readline())
    ret = []
    for line in file:
        verte, svoris = [int(x) for x in line.split()]
        ret.append(Moneta(verte, svoris))
    return s, ret

def daugiau(left, right):
    return left > right

def maziau(left, right):
    return left < right

def main():
    svoris, monetos = skaitymas('duomenai.txt')
    start = time.clock()
    daugiausiai = sprendimas(svoris, monetos, daugiau)
    maziausiai = sprendimas(svoris, monetos, maziau)
    end = time.clock()
    print('Didziausia imanoma verte %d' % daugiausiai)
    print('Maziausia imanoma verte %d' % maziausiai)
    print('Praejes laikas %fus' % float((end - start) * 1000000.0))

main()