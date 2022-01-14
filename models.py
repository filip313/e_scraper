class Cena():

    def __init__(self, id_prod, id, cena, datum):
        self.id_prod = id_prod
        self.id = id
        self.cena = cena
        self.datum = datum


class Linkovi():

    def __init__(self, id_prod, link):
        self.id_prod = id_prod
        self.link = link


class Proizvod():
    
    def __init__(self, ime:str, id:int, cene, linkovi):
        self.ime = ime
        self.id = id
        self.cene = cene
        self.linkovi = linkovi 


class Prodavnica():

    def __init__(self, ime='', id=''):
        self.ime = ime
        self.id = id

