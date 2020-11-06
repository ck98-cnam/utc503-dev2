from fractions import Fraction
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    numerateur   = 1
    denominateur = 1
    def __init__(self, num, den):
        self.numerateur   = num
        self.denominateur = den
    def __str__(self):
        return str(self.numerateur) + "/" + str(self.denominateur)
    def __add__(self, Fra2):
        newnum = self.numerateur * Fra2.denominateur + self.denominateur * Fra2.numerateur
        newden = self.denominateur * Fra2.denominateur
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
    def __mul__(self, Fra2):
        newnum = self.numerateur * Fra2.numerateur
        newden=self.denominateur * Fra2.denominateur
        common=gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def simplifie(a,b):
        num = a
        den = b
        common = gcd(a, b)
        return Fraction(num // common, den // common)

fra1 = Fraction.simplifie(200, 40)
print(fra1)
fra1 = Fraction(50, 8)
fra2 = Fraction(22, 4)
fra3 = fra1 + fra2
print(fra3)
fra1 = Fraction(50, 8)
fra2 = Fraction(22, 4)
fra3 = fra1 * fra2
print(fra3)