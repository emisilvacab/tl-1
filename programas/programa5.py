# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    sal = re.sub(r'\s*<\w*>\s*(\d*\.\d*|\d*)\s*</\w*>', "", texto)
    sal = re.sub(r'\n\s*<\w*>\s*</\w*>', "\n", sal)
    sal = re.sub(r'\n\s*\n(\s*\n)*<\?xml', "<?xml", sal)
    sal = re.sub(r'</Image>\n\s*(\n\s*)*', "</Image>", sal)
    sal = re.sub(r'\n\s*\n(\s*\n)*', "\n", sal)
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
