class monaie:
    valeur = 0
    devise = ""
    def __init__(this, val, dev):
        this.valeur = val
        this.devise = dev
    def ajouter(self, mon2):
        if self.devise != mon2.devise:
            err ="Les deux monaies doivent avoir la meme devise!"
            raise TypeError(err)
        self.valeur += mon2.valeur
        return self.valeur
    def retrancher(self, mon2):
        if self.devise != mon2.devise:
            err ="Les deux monaies doivent avoir la meme devise!"
            raise TypeError(err)
        self.valeur -= mon2.valeur
        return self.valeur

### premier test m1 + m2 = 12 euros
m1 = monaie(5, "euro")
m2 = monaie(7, "euro")
m1.ajouter(m2)
### deuxieme test m1 - m2 = -2 euros
m1 = monaie(5, "euro")
m2 = monaie(7, "euro")
m1.retrancher(m2)
### troisieme test m1 et m2 differents devise
m1 = monaie(5, "euro")
m2 = monaie(7, "dollar")
m1.ajouter(m2)
m1.retrancher(m2)