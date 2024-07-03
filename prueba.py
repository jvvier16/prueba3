from funciones import*
import time,csv
while True:
    print("""menu
    1. Registrar pedido.
    2. Listar todos los pedidos.
    3. Buscar pedido por RUT.
    4. Imprimir hoja de ruta.
    5. Salir del programa.""")
    opc = int(input("que opcion desea usar:"))
    if opc == 1 :
        opc_1()
    elif opc == 2:
        opc_2()
    elif opc == 3:
        opc_3()
    elif opc ==4:
        opc_4()
    elif opc == 5:
        opc_5()   
    else:
        print ("opcion no existe ")