import datetime
import diseño_registro

class Empleado:
    def __init__(self, cuil):
        self.cuil = cuil
        self.conceptos = []

    def procesar_registro(self, dict):
        if dict['registro'] == '02' or dict['registro'] == '04':
            # self.registro2 = dict
            for campo, largo in dict.items():
                exec(f"self.{campo} = '{dict[campo]}'")

        # elif dict['registro'] == '04':

        #     for campo, largo in dict.items():
        #         exec(f"self.{campo} = '{dict[campo]}'")

        elif dict['registro'] == '03':
            self.conceptos.append(dict)

        # Se elimna el campo registro
        try:
            del self.registro
        except:
            pass
        

    def __eq__(self, other):
        return self.cuil == other

    def __repr__(self) -> str:
        return str(self.cuil)

    def __str__(self) -> str:
        
        out = '<Empleado>\n'

        variables = list(self.__dict__.keys())
        
        for var in sorted(variables):
            if var != 'conceptos':
                out += f'  {var.ljust(30)} : {self.__dict__[var]}\n'
        

        out += f'\n  {"Cant. conceptos liquidados:".ljust(30)} : {len(self.conceptos)}\n'

        return out


class ArchivoPresentacion:
    
    def __init__(self, archivo):
        self.archivo = archivo
        self.cargar_datos_archivo(archivo)
        self.leer_registro_1()
        self.empleados = []
        self.leer_empleados()

        del self.lineas

    def cargar_datos_archivo(self, archivo):
        self.lineas = open(archivo, 'r').readlines()

    def leer_registro_1(self):

        self.registro1 = diseño_registro.leer_registro(self.lineas[0])

        for campo, largo in self.registro1.items():
            exec(f"self.{campo} = '{self.registro1[campo]}'")

    def leer_empleados(self):
        for linea in self.lineas:
            leido = diseño_registro.leer_registro(linea)

            if leido['registro'] == '01':
                continue

            cuil = leido['cuil']
            empleado = None

            if cuil in self.empleados:
                for emp in self.empleados:
                    if emp == cuil:
                        empleado = emp
                        break
                pass
            else:
                empleado = Empleado(cuil)
                self.empleados.append(empleado)
                

            # Se procesa la linea con el empleado
            empleado.procesar_registro(leido)

    def guardar(self, inplace=False):
        if inplace:
            out_file = self.archivo
        else:
            ahora = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            out_file = self.archivo.replace('.txt', f"_{ahora}.txt")

        # Determinacion de registros
        reg1 = [diseño_registro.dict_to_linea(self.registro1)]

        reg2 = []
        for emp in self.empleados:
            linea = f"\n{diseño_registro.dict_to_linea(emp.registro2)}"
            reg2.append(linea)

        reg3 = []
        for emp in self.empleados:
            for conc in emp.conceptos:
                linea = f"\n{diseño_registro.dict_to_linea(conc)}"
                reg3.append(linea)

        reg4 = []
        for emp in self.empleados:
            linea = f"\n{diseño_registro.dict_to_linea(emp.registro4)}"
            reg4.append(linea)

        union = reg1 + reg2 + reg3 + reg4

        # Guardado en txt
        file = open(out_file, 'w')
        file.writelines(union)
        file.close()
        
        print("Se guardo el txt correctamente:")
        print(out_file)


