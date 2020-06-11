from claseProducto import Producto
from claseVenta import Venta



def monto_total(prod_comprados):
    total = 0
    for elemento in lista_productos:
        total = total + elemento.verPrecio()
    return total


def mayor_monto_vendido(total_facturado):
    return max(total_facturado)
           
           

lista_productos = []
p1 = Producto("papa", 10)
p2 = Producto("pera", 5)
lista_productos.append(p1)
lista_productos.append(p2)



total_facturado = []
c0 = 10
c1 = 15
c2 = 20
total_facturado.append(c0)
total_facturado.append(c1)
total_facturado.append(c2)


monto_vendido = monto_total ()


total_facturado.append(monto_vendido)

ventas = []
v0 = Venta("dom", "3", "qqq", total_facturado[0])
v1 = Venta("lunes", "9", "aaa", total_facturado[1])
v2 = Venta("martes", "5", "zzz", total_facturado[2])
ventas.append(v0)
ventas.append(v1)
ventas.append(v2)

maximo = mayor_monto_vendido(total_facturado)
posicion = total_facturado.index(maximo)


print("El mejor vendedor es: {}".format(ventas[posicion].ver_vendedor()))
