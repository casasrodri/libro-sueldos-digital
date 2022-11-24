class Contenedor():
    def __init__(self, dicc=None) -> None:
        if dicc != None:
            self.attrs(dicc)

    def attr(self, metodo, valor):
        if type(valor) == str:
            valor = f"'{valor}'"

        exec(f"self.{metodo} = {valor}")

    def attrs(self, dicc):
        for k,v in dicc.items():
            self.attr(k, v)

    def __repr__(self) -> str:
        return f"<Contenedor> {str(self.__dict__)}"


aa = {'ssss': 'Rodrigo', 'apellido': 'Casas', 'edad': 30.1, 'estudiante': True}

con = Contenedor(aa)

# print(con.__dict__)
print(con)

contened = Contenedor({'otro_valor': False, 'altura': 1.76})
contened.otro_contenedor = con
print(contened.otro_contenedor.apellido)
