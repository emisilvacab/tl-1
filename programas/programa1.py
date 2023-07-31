# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    fech = re.search(r'<FileModifyDate>\s*(.*)T', texto, flags=0)
    hor = re.search(r'T((\d)*:(\d)*).*</FileModifyDate>', texto, flags=0)
    return hor.group(1) + ' del ' + fech.group(1)

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
