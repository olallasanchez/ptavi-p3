#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.L_Primera = ['width', 'height', 'background-color']
        self.L_Segunda = ['id', 'top', 'bottom', 'left', 'right']
        self.L_Tercera = ['src', 'region', 'begin', 'dur']
        self.L_Cuarta = ['src', 'begin', 'dur']
        self.L_Quinta = ['src', 'region']
        self.Lista = []

    def startElement(self, name, attrs):

        if name == 'root-layout':
            dic = {"name": "Root-Layout"}
            for atributo in self.L_Primera:
                dic[atributo] = attrs.get(atributo, "")
            self.Lista.append(dic)

        elif name == 'region':
            dic = {"name": "Region"}
            for atributo in self.L_Segunda:
                dic[atributo] = attrs.get(atributo, "")
            self.Lista.append(dic)

        elif name == 'img':
            dic = {"name": "Img"}
            for atributo in self.L_Tercera:
                dic[atributo] = attrs.get(atributo, "")
            self.Lista.append(dic)

        elif name == 'audio':
            dic = {"name": "Audio"}
            for atributo in self.L_Cuarta:
                dic[atributo] = attrs.get(atributo, "")
            self.Lista.append(dic)

        elif name == 'textstream':
            dic = {"name": "Textstream"}
            for atributo in self.L_Quinta:
                dic[atributo] = attrs.get(atributo, "")
            self.Lista.append(dic)

    def get_tags(self):
        return self.Lista


if __name__ == "__main__":
    fichero = sys.argv
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(fichero[1]))
    print cHandler.get_tags()
