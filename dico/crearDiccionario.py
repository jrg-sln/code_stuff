# -*- coding: utf-8 -*-


def crearCombinaciones(abecedario):
    for d1 in abecedario:
        for d2 in abecedario:
            for d3 in abecedario:
                for d4 in abecedario:
                    for d5 in abecedario:
                        for d6 in abecedario:
                            for d7 in abecedario:
                                for d8 in abecedario:
                                    #print(d1+''+d2+''+d3+''+d4+''+d5+''+d6+''+d7+''+d8)
                                    f.write(d1+''+d2+''+d3+''+d4+''+d5+''+d6+''+d7+''+d8)
                                    f.write('\n')


abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

f = open("dico.txt", "w")
crearCombinaciones(abecedario)
f.close()
