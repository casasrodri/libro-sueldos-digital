#import diseño_registro
from argparse import ArgumentError
from anterior.lector_archivo import ArchivoPresentacion

def dbl_con_ceros(num, cant):
    return "{:.2f}".format(num).replace('.','').zfill(cant)

#txt = ArchivoPresentacion(r"presentaciones\A10_AUS_A16.txt")


#print(txt.empleados[2])

# Hacer que en la lectura cada elemento se pase a un valor legible para humano
# Y lo mismo al guardarlo

# Crear la clase ConceptoLiquidado

import io_presentacion as io

pp = io.Reader('sasas')

print(pp)

