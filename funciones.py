import csv,time

acumulador = 0
cilindro5= 12500
cilindro15=25500
nombre= []
rut = []
direccion = []
comuna=[]
cili_5 =[]
cili_15=[]
def opc_1():
    nom = input("ingrese su nombre ")
    nombre.append(nom)
    ru = int(input("ingrese su rut sin puntos ni -"))
    rut.append(ru)
    dire = input("ingrese su direccion")
    direccion.append(dire)
    comu = input("ingrese la comuna")
    comuna.append(comu)
    while True:
        print("""que desea perdir
                 1.cilindro de 5kg
                 2.cilindro de 15kg
                 3.salir""")
        opcionci= int(input)
        if opcionci ==1:
            cantidad = int(input("cuantos desea pedir"))
            cili_5.append(cantidad)
            acumulador=cantidad * cilindro5
        elif opcionci==2: 
            cantidad = int(input("cuantos desea pedir"))
            cili_15.append(cantidad)
            acumulador=cantidad * cilindro15
        elif opcionci==3:
            print("pedido con exito")
            time.sleep(3)
            break
def opc_2():
    if rut == 0:
        print("error no hay ningun perdido")
    else:
        print(nombre)
        print(rut)
        print(direccion)
        print(comuna)
        print(cili_5)
        print(cili_15)
def opc_3():
    buscar = int(input("ingrese el rut que esta buscando"))
    rut.index(buscar)
    print(nombre)
    print(rut)
    print(direccion)
    print(comuna)
    print(cili_5)
    print(cili_15)
def opc_4():
    pass
def opc_5():
    print ("su pedido fue realisado adios")
    time.sleep(3)
    exit


