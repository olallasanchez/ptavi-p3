#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import os
import sys
import smallsmilhandler


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.Lista = cHandler.get_tags()

    def __str__(self):
        total = ""
        for Diccionario in self.Lista:
            for Clave_Dic in Diccionario.keys():
                if Clave_Dic != 'name' and Diccionario[Clave_Dic] != '':
                    total = total + Clave_Dic + "="
                    total += Diccionario[Clave_Dic] + '\t'
        return Diccionario['name'] + "\t" + total

    def do_local(self):
        for Diccionario in self.Lista:
            total = ""
            for Clave_Dic in Diccionario.keys():
                if Clave_Dic == 'src':
                    Recurso = Diccionario[Clave_Dic]
                    os.system("wget -q " + Recurso)
                    Lista = Diccionario[Clave_Dic].split('/')
                    Recurso = Lista[-1]
                    Diccionario[Clave_Dic] = Recurso
                if Clave_Dic != 'name' and Diccionario[Clave_Dic] != '':
                    total = total + Clave_Dic + "="
                    total += Diccionario[Clave_Dic] + '\t'


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("")

    karaoke = KaraokeLocal(sys.argv[1])
    print karaoke
    karaoke.do_local()
    print karaoke
