# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    resx = re.search(r'<Resolution>[^X]*X>\s*(\d*)\s*</X>', texto)
    reseny = re.search(r'<Resolution>[^Y]*Y>\s*(\d*)\s*</Y>', texto)
    return 'Resolucion X: ' + resx.group(1) + '\n' + 'Resolucion Y: ' + reseny.group(1)

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
