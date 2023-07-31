# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    copia = texto
    res = re.sub(r'<[^>]*>.*?\.uy[^<]*<[^>]*>', "", copia)
    lista = re.findall(r'<[^>]*>.*?http[^\s]*', res)
    if len(lista) > 0:
        resu = re.sub(r'>.*?\shttp', ' -- http', re.sub(r'<', '', lista[0]))
        for i in range(1, len(lista)):
            resu = resu + "\n" + re.sub(r'>.*?\shttp', ' -- http', re.sub(r'<', '', lista[i]))
        return resu
    else:
        return ""

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = open(archivo_entrada, 'r')
    datos = f.read()
    f.close()
    salida = programa(datos)
    f = open(archivo_salida, 'w')
    f.write(salida)
    f.close()
