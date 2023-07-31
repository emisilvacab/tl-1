# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    sal = len(re.findall(r'<(.*)(D|d)ate(.*)>(.*)<(.*)(D|d)ate(.*)>', texto, flags=0))
    sal = str(sal)
    return sal

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
