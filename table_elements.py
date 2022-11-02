# Enums
class Enum:
    @classmethod
    def valor(cls, valor):
        di = dict(cls.__dict__)

        try:
            pos = list(di.values()).index(valor)
        except ValueError:
            raise ValueError(f"No existe el valor '{valor}' como constante de la clase {cls}.")

        return list(di.keys())[pos]

class TIPO(Enum):
    ITEMS = range(0,5)
    NUM, STR, FLOAT, BOOL, DATE = ITEMS

class LADO(Enum):
    ITEMS = range(0,3)
    NO, IZQ, DER = ITEMS

class RELLENO(Enum):
    ITEMS = range(0,3)
    NO, CERO, ESPACIO = ITEMS


class Campo:    
    def __init__(self, nombre, ancho, tipo, lado_relleno=LADO.NO, char_relleno=RELLENO.NO):
        self.nombre = nombre
        self.ancho = ancho

        self.tipo = tipo
        assert tipo in TIPO.ITEMS, "Tipo inválido: '{}'".format(TIPO.valor(tipo))

        self.lado_relleno = lado_relleno
        assert lado_relleno in LADO.ITEMS, "Lado relleno inválido: '{}'".format(LADO.valor(lado_relleno))

        self.char_relleno = char_relleno
        assert char_relleno in RELLENO.ITEMS, "Carater relleno inválido: '{}'".format(RELLENO.valor(char_relleno))
    
    def __repr__(self) -> str:
        return f"{TIPO.valor(self.tipo).rjust(10)} | {self.nombre}"
    

class Tabla:
    def __init__(self, arr) -> None:
        self.campos = arr
    
    def __repr__(self) -> str:
        out = '<Diseño>\n'
        for campo in self.campos:
            out += f"  {campo}\n"

        return out

    def get_dict(self):
        out = {}
        for campo in self.campos:
            out[campo.nombre] = campo.ancho
        return out