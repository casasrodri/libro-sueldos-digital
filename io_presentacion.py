import design_tables as dt
from table_elements import TIPO

class Reader:

    def __init__(self, archivo):
        self.archivo = archivo
        self.diseños = [dt.DISEÑO1, dt.DISEÑO2, dt.DISEÑO3, dt.DISEÑO4]
        self.txt = None

    def parser_diseño(self, diseño):
        pass

    def cortar_linea(self, linea):
        
        num_diseño = int(linea[0:2])
        try:
            diseño_aplicable = self.diseños[num_diseño-1]
        except:
            print(linea)
            raise TypeError("Tipo de registro no aceptado (debe comenzar con 01 al 04).")

        out = {}
        ini = 0
        for d in diseño_aplicable.campos:

            fin = ini + d.ancho

            # Obtención del valor
            valor = linea[ini:fin]

            # Transformación del valor (según TIPO.ITEMS)
            if d.tipo == TIPO.NUM:
                valor = int(valor)

            if d.tipo == TIPO.STR:
                valor = valor.strip()

            if d.tipo == TIPO.FLOAT:
                valor = int(valor)/100

            if d.tipo == TIPO.BOOL:
                valor = True if valor == '1' else False

            if d.tipo == TIPO.DATE:
                pass
            
            # Incorporación al hash
            out[d.nombre] = valor

            ini = fin
        
        return out




txt = Reader(r"presentaciones\A10_AUS_A16.txt")

# print(txt.__dict__)

# Si es 1: Crear ArchivoPresentacion()
# Si es 2: Buscar o crear un Empleado() e incorporar la info
# Si es 3: Crear ConceptoLiquidado()
# Si es 4: Buscar o crear un Empleado() e incorporar la info


print(txt.cortar_linea("0427257004290000010100501049008001801010509000030000000000000040080000000000000000000000000000000000000000000000000000000000000000000000000000000000000041852333000000014612331000000014557331000000014557331000000014557331000000014557331000000014557331000000000000000000000000000000000000014557331000000014557331000000000000000000000000000000000000014393912000000000163419"))