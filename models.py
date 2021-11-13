from json.encoder import JSONEncoder


class Cena(JSONEncoder):

    def __init__(self, id_prod = -1, id = -1, cena = -1 , datum = -1):
        self.id_prod = id_prod
        self.id = id
        self.cena = cena
        self.datum = datum


class Linkovi(JSONEncoder):

    def __init__(self, id_prod = -1, link = ''):
        self.id_prod = id_prod
        self.link = link


class Proizvod(JSONEncoder):
    
    def __init__(self, ime:str, id:int, cene = dict(), linkovi = dict()):
        self.ime = ime
        self.id = id
        self.cene = cene
        self.linkovi = linkovi 

    def print(self):
        print(f"{self.id} -> {self.ime}")
        for i in self.cene.keys():
            print(f"\t{self.cene[i].id} -> {self.cene[i].cena}\twww.eponuda.com"+
            f"{self.linkovi[self.cene[i].id_prod].link}")


class Prodavnica(JSONEncoder):

    def __init__(self, ime='', id=''):
        self.ime = ime
        self.id = id

