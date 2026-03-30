# 1
class Bank:
    def __init__(self, balans):
        self.__balans = balans

b = Bank(100000)
print(b.__balans)


# 2
class A:
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val



# 3
class Sanoq:
    umumiy = 0

    def __init__(self, ism):
        self.ism = ism
        Sanoq.umumiy += 1

a = Sanoq('Ali')
b = Sanoq('Vali')
c = Sanoq('Gali')
print(Sanoq.umumiy)



# 4
class Mehmon:
    pass

m = Mehmon()
m.ism = 'Zulfiya'
m.yosh = 25
print(hasattr(m, 'ism'))
print(hasattr(m, 'manzil'))



# 5
class Til:
    versiya = 3.11

t1 = Til()
t2 = Til()
Til.versiya = 3.12
print(t1.versiya)
print(t2.versiya)


# 6
class Hayvon:
    def nafas_ol(self):
        return 'Nafas olmoqda'

class It(Hayvon):
    def vov(self):
        return 'Vov-vov!'

i = It()
print(i.nafas_ol())
print(i.vov())

# 7
class Kalit:
    pass

k = Kalit()
k.rang = 'sariq'
print(k.rang)



# 8
class Ota:
    def kim(self):
        return 'Ota'

class Farzand(Ota):
    pass

f = Farzand()
print(f.kim())


# 9
class Salom:
    def ayt(self):
        return 'Assalomu alaykum!'

s = Salom()
print(s.ayt())

# 10
class Hisoblagich:
    soni = 0

    def oshir(self):
        self.soni += 1

h = Hisoblagich()
h.oshir()
h.oshir()
h.oshir()
print(h.soni)
