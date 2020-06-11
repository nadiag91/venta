class Venta:
    def __init__ (self, dia, hora, vendedor, monto):
        self.dia = dia
        self.hora = hora
        self.vendedor = vendedor
        self.monto = monto
        

    def ver_vendedor(self):
        return self.vendedor
        
    def ver_monto(self):
        return self.monto
    

