def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar Producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion")
            if opcion >= 0 or opcion < 6:
                return opcion
            else:
                print("debe seleccionar una opcion valida")
        except ValueError:
            print("debe seleccionar una opcion valida")
            
def stock_categoria(categoria, productos, ventas):
    total_stock = 0
    
    

# --------------------------------------------------
# Diccionario de productos
# clave = codigo de producto (como P001, P002 y etc)
# valor =
# --------------------------------------------------
productos = {
}

# --------------------------------------------------
# Diccionario de ventas
# clave = codigo de producto (como P001, P002 y etc)
# valor =
# --------------------------------------------------
ventas = {
}

# CODIGO PRINCIPAL
empezar = True
while empezar:
    mostrar_menu()
    opcion = leer_opcion()



