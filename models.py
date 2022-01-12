from json.encoder import JSONEncoder
import json

class Cena():

    def __init__(self, id_prod, id, cena, datum):
        self.id_prod = id_prod
        self.id = id
        self.cena = cena
        self.datum = datum

    def __iter__(self):
        yield from {
            "id" : self.id,
            "id_prod" : self.id,
            "cena" : self.cena,
            "datum" : self.datum
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


class Linkovi():

    def __init__(self, id_prod, link):
        self.id_prod = id_prod
        self.link = link

    def __iter__(self):
        yield from {
            "id_prod" : self.id_prod,
            "link" : self.link
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

class Proizvod():
    
    def __init__(self, ime:str, id:int, cene, linkovi):
        self.ime = ime
        self.id = id
        self.cene = cene
        self.linkovi = linkovi 

    def __iter__(self):
        yield from {
            "ime" : self.ime,
            "id" : self.id,
            "cene" : self.cene,
            "self.linkovi" : self.linkovi
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def print(self):
        print(f"{self.id} -> {self.ime}")
        for i in self.cene.keys():
            print(f"\t{self.cene[i].id} -> {self.cene[i].cena}\twww.eponuda.com"+
            f"{self.linkovi[self.cene[i].id_prod].link}")


class Prodavnica():

    def __init__(self, ime='', id=''):
        self.ime = ime
        self.id = id

    def __iter__(self):
        yield from {
            "ime" : self.ime,
            "id" : self.id
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


class MyEncoder(JSONEncoder):

    def default(self, obj):
        return obj.__dict__