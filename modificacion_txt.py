import diseño_registro
from lector_archivo import ArchivoPresentacion

# Funciones extras
def dbl_con_ceros(num, cant):
    return "{:.2f}".format(num).replace('.','').zfill(cant)

# Lectura del archivo a trabajar
txt = ArchivoPresentacion(r"A10_AUS_A16.txt")
#print(txt.__dict__)


# Ejemplo de modificación del código de liquidación para ciertos CUILs

#cuils_modificar = ['27257004290', '20220879144']
cuils_modificar = """
27257004290
20220879144
"""
cuils_modificar = cuils_modificar.strip().split('\n')

for emp in txt.empleados:
    if emp in cuils_modificar: # Si es para todos, esta comprobación no se haría.
        for concepto in emp.conceptos:
            if concepto['codigo_concepto_liquidado'] == '/321      ':
                concepto['codigo_concepto_liquidado'] = '/XXXxxx   '


# Verificación de que la remuneracion 10 no sea menor al MNI

MINIMO_NO_IMPONIBLE = 14601.14
for emp in txt.empleados:
    base10 = int(emp.registro4['base_imponible10'])/100.0
    
    if base10 < MINIMO_NO_IMPONIBLE:

        print(f"CUIL: {emp}")
        print("La base_imponible10 es menor al mínimo no imponible.")
        
        base8 = int(emp.registro4['base_imponible8'])/100.0
        detraccion = max(0,round(base10 - base8,2))
        
        emp.registro4['base_imponible10'] = dbl_con_ceros(MINIMO_NO_IMPONIBLE, diseño_registro.DISEÑO4['base_imponible10'])
        emp.registro4['importe_detraer'] = dbl_con_ceros(detraccion, diseño_registro.DISEÑO4['importe_detraer'])
        
        print("Se actualizaron los siguientes valores:")
        print(f" base_imponible10: {emp.registro4['base_imponible10']}")
        print(f" importe_detraer: {emp.registro4['importe_detraer']}")


# Agrego el SAC a determinados CUILs
info = """
27257004290 120 29389.84
20220879144 10 3923.84
"""

info = info.strip().split('\n')

cuils_agregar = {}
for i in info:
    cortado = i.split(' ')
    
    cuils_agregar[cortado[0]] = {'dias': cortado[1], 'importe': float(cortado[2])}


for emp in txt.empleados:
    if emp in list(cuils_agregar.keys()):

        dias = str(cuils_agregar[emp.cuit]['dias']).zfill(5)
        importe = dbl_con_ceros(cuils_agregar[emp.cuit]['importe'], 15)

        emp.conceptos.append({
            'registro':                     '03',
            'cuil':                         emp.cuit,
            'codigo_concepto_liquidado':    '/S13      ',
            'cantidad':                     dias,
            'unidades':                     'D',
            'importe':                      importe,
            'debcre':                       'C',
            'periodo_retro':                '      '
        })



#txt.guardar(inplace=True)
#txt.guardar()