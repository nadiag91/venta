from claseProducto import Producto
from claseVenta import Venta

#en esta lista se almacenan las ventas realizadas con su dia, hora, nombre del vendedor y monto pagado
total_ventas = []

#con esta funcion se busca el precio de cada producto ingresado en la venta
def buscar_precio_producto(prod_a_pagar):
    precio_encontrado = 0
    for productos in lista_productos:
        if prod_a_pagar == productos.verNombre():
            precio_encontrado = productos.verPrecio() 
    return precio_encontrado


#esta funcion encuentra el mayor monto vendido de la lista de ventas totales y devuelve tambien la posicion de ese
# mayor monto encontrado  
def mayor_monto(total_ventas):
    mayor_valor = 0
    posicion_encontrada = 0
    posicion_actual = 0
    for montos in total_ventas:
        if montos.ver_monto() > mayor_valor:
            mayor_valor = montos.ver_monto()
            posicion_encontrada = posicion_actual 
        posicion_actual = posicion_actual + 1
    return mayor_valor, posicion_encontrada
        

#esta lista contiene los productos a la venta con sus respectivos precios
lista_productos = []
p1 = Producto("papa", 10)
p2 = Producto("pera", 5)
p3 = Producto("coco", 3)
lista_productos.append(p1)
lista_productos.append(p2)
lista_productos.append(p3)



while(True):
    opciones = int(input("Ingrese 1 para registrar una nueva compra, 2 para encontrar el mayor monto vendido "))


    if opciones == 1:
        #Comienza la venta determinando la cantidad de productos a vender para determinar de cada uno de ellos, su precio
        #y conocer el monto total a pagar
        cant_prod = int(input("Ingrese cantidad de productos comprados: "))
        monto_a_pagar = 0 
        for i in range(cant_prod):
            prod_a_pagar = input("Ingrese nombre producto: ")
            monto_total = buscar_precio_producto(prod_a_pagar)
            monto_a_pagar = monto_total + monto_a_pagar

        dia_ingresado = input("Ingrese día: ")
        hora_ingresada = input("Ingrese hora: ")
        vendedor_ingresado =input("Ingrese nombre del vendedor: ")

        #se almacenan los datos de la venta efectuada en la lista total_ventas
        datos_de_venta = Venta(dia_ingresado, hora_ingresada, vendedor_ingresado, monto_a_pagar)
        total_ventas.append(datos_de_venta)
            
        print ("El monto total a pagar es de $ {}". format(monto_a_pagar))
        for n in total_ventas:
            print(n.ver_monto())


    if opciones == 2:
        #en esta opcion se puede conocer cuál fue el mayor monto vendido del total de ventas
        #en la lista total_ventas y con la posicion encontrada se conoce al vendedor que la realizó
        mayor_monto_vendido, posicion_vendedor = mayor_monto(total_ventas)
        print("El mayor monto vendido fue de $ {}".format(mayor_monto_vendido))
        
        
        mejor_vendedor = total_ventas[posicion_vendedor].ver_vendedor()

        print("El vendedor de mayor monto es: {}".format(mejor_vendedor))