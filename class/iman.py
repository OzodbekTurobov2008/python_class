class Telefon:
    def __init__(self,nomi, rangi, yili):
        self.nomi = nomi
        self.rangi = rangi
        self.yili = yili 

    def __str__(self):
        return f"Nomi: {self.nomi}, Rangi: {self.rangi}, Yili: {self.yili}"

tel1 = Telefon("Samsung", "qora", 2023)
tel2 = Telefon("Apple", "oq", 2023)
tel3 = Telefon("Huawe", "Crimson", 2023)
tel3 = Telefon("Honor", "kulrang", 2023)
tel5 = Telefon("Nokia", "jigari", 2024)



class Noutbook:
    def __init__(self,nomi, narxi, yili):
        self.nomi = nomi
        self.narxi = narxi
        self.yili = yili 

    def __str__(self):
        return f"Nomi: {self.nomi}, narxi: {self.rangi}, Yili: {self.yili}"

nout1 = Telefon("Acer", "qizil", 2022)
nout2 = Telefon("Apple", "qora", 2023)
nout3 = Telefon("Honor", "kulrang", 2023)


print(nout1)
print(nout2)
print(nout3)



class Airpods:
    def __init__(self,nomi, rangi, yili):
        self.nomi = nomi
        self.rangi = rangi
        self.yili = yili 

    def __str__(self):
        return f"Nomi: {self.nomi}, Blandligi: {self.rangi}, Yili: {self.yili}"

air1 = Airpods("Mir7", "bo`ladi", 2023)
air2 = Airpods("V68", "zo`r", 2022)
air3 = Airpods("MI", "jugda baland", 2022)

print(air1)
print(air2)
print(air3)


         
class Kitob:
    def __init__(self,nomi, yili, beti):
        self.nomi = nomi
        self.yili = yili
        self.beti = beti

    def __str__(self):
        return f"Nomi: {self.nomi}, Yili: {self.yili}, Beti: {self.beti}" 

ki1 = Kitob("PYTHON", '2022', 500)
ki2 = Kitob("HTML CSS", '2023', 600)
ki3 = Kitob("jACASCRIPT", '2022', 300)


print(ki1)
print(ki2)
print(ki3)

class Odam:
    def __init__(self,ism, fam, yosh):
        self.ism = ism
        self.fam=fam
        self.yosh=yosh 
    def __str__(self):
        return f"Ism: {self.ism}, Fam: {self.fam}, Yosh: {self.yosh}"

o1=Odam("Ozodbek", "Turobov", 15)
o2=Odam("Ubaydullo", "Jumayev", 20)
o3=Odam("Maruf", "Alimov", 15)

print(o1)
print(o2)
print(o3)



class Mashina:
    def __init__(self,nomi, rangi, yili):
        self.nomi = nomi
        self.rangi=rangi
        self.yili=yili
    def __str__(self):
        return f" Nomi: {self.nomi}, Rangi: {self.rangi}, Yili: {self.yili}"
    
o1=Mashina("Rols roys", "kulrang", 2024)
o2=Mashina("BMW", "oq", 2023 )
o3=Mashina("Apple", "Crimson", 2023)
o4=Mashina("Cobalt", "ko`k", 2023)
o5=Mashina("Gentra", "qora", 2024)

print(o1)
print(o2)
print(o3)
print(o4)
print(o5)


class Oshjihozlari:
    def __init__(self,rangi, yili, nomi, ishlashi, narxi):
        self.rangi=rangi
        self.yili=yili
        self.nomi=nomi
        self.ishlashi=ishlashi
        self.narxi=narxi
    def __str__(self):
        return f"Rangi: {self.rangi}, Yili: {self.yili}, Nomi: {self.nomi}, Ishlashi: {self.ishlashi}, Narxi: {self.narxi}"

osh1=Oshjihozlari("qara", 2022, "kapkur", "yaxshi", "50ming")
osh2=Oshjihozlari("qizil", 2020, "kohniya", "narmalni", "7million")
osh3=Oshjihozlari("ko`k", 2022, "multivarka", "daxshat", "900ming")
osh4=Oshjihozlari("sariq", 2021, "gazplita", "bo`ladi", "5million")
osh5=Oshjihozlari("oq", 2023, "muzlatgich", "zo`r", "9million")

print(osh1)
print(osh2)
print(osh3)
print(osh4)
print(osh5)

class Jihozlar:
    def __init__(self,nomi, rangi, yili, narxi, chidam):
        self.nomi=nomi
        self.rangi=rangi
        self.yili=yili
        self.narxi=narxi
        self.chidam=chidam
    def __str__(self):
        return f"Nomi: {self.nomi}, Rangi: {self.rangi}, Yili{self.yili}, Narxi: {self.narxi}, Chidam: {self.chidam}"

ji1=Jihozlar("Ketmon", "sabzirang", 2018, "70ming", "yaxshi")
ji2=Jihozlar("Tesha", "qora", 2020, "70ming", "zo`r")
ji3=Jihozlar("Randa", "oq", 2023, "70ming", "bo`ladi")
ji4=Jihozlar("Lapatka", "qizil", 2022, "70ming", "yaxshi")
ji5=Jihozlar("O`roq", "sariq", 2015, "70ming", "narmalni")


print(ji1)
print(ji2)
print(ji3)
print(ji4)
print(ji5)


class Ferma:
    def __init__(self,nomi, rangi, nimaish, yili, qandayligi):
        self.nomi = nomi
        self.rangi = rangi
        self.yili = yili
        self.nimaish = nimaish
        self.qandayligi = qandayligi
    def __str__(self):
        return f"Nomi: {self.nomi}, Rangi: {self.rangi}, Nimaish: {self.nimaish}, Yili: {self.yili}, Qandayligi: {self.qandayligi}"

f1=Ferma("Honor", "oq", "Nout-tel", 2023, "yaxshi")
f2=Ferma("Apple", "qora", "Nout-tel", 2023, "yaxshi")
f3=Ferma("Audi", "kulrang", "Nout-tel", 2022, "narmalni")
f4=Ferma("Acer", "qizil", "Nout-tel", 2024, "boladi")
f5=Ferma("Victus", "oq", "Nout-tel", 2026, "zor")

print(f1)
print(f2)
print(f3)
print(f4)
print(f5)

class Gul:
    def __init__(self,ismi, rangi, hidi, yili, qandayligi):
        self.ismi=ismi
        self.rangi=rangi
        self.hidi=hidi
        self.yili=yili
        self.qandayligi=qandayligi

    def __str__(self):
        return f" Ismi: {self.ismi}, Ismi: {self.ismi}, Rangi: {self.hidi}, Yili: {self.yili}, Qandayligi: {self.qandayligi}"

g1=Gul("Lola", "qizil", "hushbuy", 2023, "narmalni")
g2=Gul("Atirgul", "sabzirang", "hushbuy", 2023, "narmalni")
g3=Gul("Lola", "sariq", "bo`ladi", 2023, "narmalni")
g4=Gul("Lola", "Oq", "unchamas", 2023, "bo`ladi")
g5=Gul("Binafsha", "binafsha", "yaxshi", 2023, "narmalni")


print(g1)
print(g2)
print(g3)
print(g4)
print(g5)


class Daftar:
    def __init__(self,nomi, varagi, rangi, yili):
        self.nomi = nomi
        self.varagi = varagi
        self.rangi = rangi
        self.yili = yili

    def __str__(self):
        return f"Nomi: {self.nomi}, Varagi: {self.varagi}, Rangi: {self.rangi}, Yili: {self.yili}"

d1=Daftar("obshe", 96, "qizil", 2023)
d2=Daftar("blaknot", 20, "qora", 2023)
d3=Daftar("Banner", 100, "oq", 2023)
d4=Daftar("obshe", 36, "yashil", 2023)
d5=Daftar("obshe", 48, "ko`k", 2023)

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)

class Meva:
    def __init__(self,nomi, rangi, qayerdan, qanaqaligi, tami):
        self.nomi=nomi
        self.rangi=rangi
        self.qayerdan=qayerdan
        self.qanaqaligi=qanaqaligi
        self.tami=tami

    def __str__(self):
        return f"Nomi: {self.nomi}, rangi: {self.rangi}, qayerdan: {self.qayerdan}, Qanaqaligi: {self.qanaqaligi}"

m1=Daftar("olma", "sariq", "O`zbak", "yaxshi", "shirin")
m2=Daftar("Anor", "qizil", "O`zbek", "yaxshi", "nordon")
m3=Daftar("Banan", "sabzirang", "Hind", "yaxshi", "narmalni")
m4=Daftar("Xurmo", "qoraroq", "", "")
m5=Daftar("", "", "", "")

print(m1)
print(m2)
print(m3)
print(m4)
print(m5)