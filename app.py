from urllib import request

def ucitaj_linkove(putanja):
    file = open(putanja, "rt")
    linkovi = list()
    for line in file:
        linkovi.append(line.strip())

    return linkovi


putanja_do_linkova = "./linkovi.txt"

linkovi = ucitaj_linkove(putanja_do_linkova)