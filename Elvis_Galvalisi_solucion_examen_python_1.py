
#función Menu. 
def verMenu(opc):
    print("----------------------------------------")
    print("MENÚ------------------------------------")
    print(" 1. Alta de Socio-----------------------")
    print(" 2. Datos de Socios---------------------")
    print(" 3. Mostrar Legajos---------------------")
    print(" 4. Cambiar Condición-------------------")
    print(" 5. Recaudación Mensual / Anual---------")
    print(" 6. Salir-------------------------------")
    print("----------------------------------------")
    
    opcion = int(input("Ingrese una opción del menú: "))
    
    while opcion < 1 or opcion > 6:
        print("¡ERROR!")
        opcion = int(input("Debe ingresar una opción válidad [1 al 6]: "))
    

    return opcion


#función para agregar socios.
def agregarSocio(cant):
    #se crea lista para guardar socios
    listaSocios = []
    print("----------------------------------------")
    print("Opción 1: Agregar Socios:---------------")
    print("----------------------------------------")
    for cont in range(cant):
        nom = input("Ingrese Nombre: ")
        ape = input("Ingrese Apellido: ")
        leg = cont + 1 
        tel = int(input("Ingrese Teléfono: "))
        mail = input("Ingrese un e-mail: ")
        tip = input("Tipo de socio: (0-Estándar / 1-Premium) ")
        #control de ingreso de valores
        while tip != '0' and tip != '1':
            print("¡ERROR!, debe ingresar '0' o '1'")
            tip = input("Tipo de Socio: ")
        if tip == '0':
            tip = False
        else:
            tip = True
        
        #se almacena en lista los datos cagados por socio.
        listaSocios.append([nom, ape, leg, tel, mail, tip])
    
    return listaSocios


#se crea la función para mostrar socios.
def mostrarSocio(sociosAgregados):
    print("----------------------------------------")
    print("Opción 2: Datos de Socios: ")
    print("----------------------------------------")
    for i in range(len(sociosAgregados)):
        print("----------------------------------------") 
        print(f"Nombre: {sociosAgregados[i][0]} - Apellido: {sociosAgregados[i][1]}")
        print(f"Legajo: {sociosAgregados[i][2]}")
        print(f"Mail: {sociosAgregados[i][4]}")
        print(f"Teléfono: {sociosAgregados[i][3]}")
        print()  

def mostarLegajos(sociosAgregados):
    print("----------------------------------------")
    print("Opción 3: Legajos de Socios: ")
    print("----------------------------------------")
    cantidad = len(sociosAgregados)
    print(f"Los socios existentes son: {cantidad}")
    print("----------------------------------------")
    listaLegajos = []
    for d in range(cantidad):
        listaLegajos.append(sociosAgregados[d][2])
    print(f"Legajos Ordenados:")
    listaLegajos.sort()
    print(listaLegajos)


def modificarCondicion(sociosAgregados):
    print("----------------------------------------")
    print("Opción 4: Modificar Condición de socio: ")
    
    print("----------------------------------------")
    nroLeg =int(input("Indique el legajo del Socio: "))
    '''
    #se valida la respuesta a modificación
    for j in range(len(sociosAgregados)):
        
        bandera = False
        
        while bandera != True:
            while nroLeg != sociosAgregados[j][2]:
                 bandera = False
        if bandera == False:
            nroLeg = input(f"¡ERROR!, Debe ingresar un legajo válido entre [0-{len(sociosAgregados)}]: ")
        else:
            bandera = True
    
    '''
    print("----------------------------------------")
    
    for z in range(len(sociosAgregados)):
        if nroLeg == sociosAgregados[z][2]:
            print(f"Socio: {sociosAgregados[z][0]} {sociosAgregados[z][1]} ")
            print(f"Legajo: {sociosAgregados[z][2]}")
            if sociosAgregados[z][5]== True:
                condic = 'PREMIUM'
            else:
                condic = 'ESTANDAR'
                print(f"Condición Actual: {condic}")
            
            resp = input("¿Desea cambiar la condición? (s/n) ").lower() #se agrega funcion para dejar minúsculas
            
            #se valida la respuesta a modificación
            while resp != 's' and resp != 'n':
                resp = input("¡ERROR!, Debe ingresar 's' o 'n': ")
            
            #se cambia el estado
            if resp == 's':
                if condic == 'PREMIUM':
                    sociosAgregados[z][5] = False
                    condic = 'ESTANDAR'
                else:
                    sociosAgregados[z][5] = True
                    condic = 'PREMIUM'
                print("----------------------------------------")      
                print("Socio actualizado con Éxito:")
                print(f"El socio {sociosAgregados[z][0]} {sociosAgregados[z][1]} cambió su condición a {condic} ")
                print("----------------------------------------") 

def recaudacion(sociosAgregados):
    
    objetivo = int(input("Ingrese Objetivo de abono anual: "))
    
    abonoE = 1800
    abonoP = 5800
    socioEstandar = 0
    socioPremium = 0


    for m in range(len(sociosAgregados)):
        if sociosAgregados[m][5] == False:
            socioEstandar += 1
        
        if sociosAgregados[m][5] == True:
            socioPremium += 1
            
    
    totalMensualPremium = abonoP * socioPremium
    
    totalMensualEstandar = abonoE * socioEstandar

    totalMensual = totalMensualEstandar + totalMensualPremium
    totalAnual = totalMensual * 12
    



    print()
    print("---------INFORME RECAUDACIÓN------------")
    print("----------------------------------------")
    print("----------------------------------------")
    print("PREMIUM")
    print(f"Los socios premium tienen un abono mensual de ${abonoP}")
    print(f"El club cuenta con {socioPremium} socios premium")
    print(f"El club recauda ${totalMensualPremium} mensual")
    print("----------------------------------------")
    print("ESTANDAR")
    print(f"Los socios Estandar tienen un abono mensual de ${abonoE}")
    print(f"El club cuenta con {socioEstandar} socios estandar")
    print(f"El club recauda ${totalMensualEstandar} mensual")
    print("----------------------------------------")
    print(f"Recaudación Mensual final: ${totalMensual}")
    print()
    print(f"Recaudación Anual final: ${totalAnual}")
    print("----------------------------------------")
    
    if totalAnual > objetivo:
        print(f"El objetivo anual de ${objetivo} ha sido superado con ${totalAnual}, objetivo obtenido")
    else:
        print(f"Objetivo no alcanzado por ${totalAnual-objetivo}.")








#main
#se define la variable que hace ingreso al programa.
opcion = 0
print("--------inicio del Programa-------------")

op = verMenu(opcion) #se inicia mostrando el menú definido en función. Recibe valor por referencia.


while op != 6:
    
    if op == 1:
        cant = int(input("Ingrese cantidad de Socios a registrar: "))
        # se pasa por parámetro la cantidad y se guarda el resultado devuelto por la función.
        sociosAgregados = agregarSocio(cant)

        #una vez ejecutada la función se muestra el MENU nuevamente.
        op = verMenu(op)
    

    if op == 2:
        #se llama a la función y se pasan los datos de la lista cargada anteriormente.
        mostrarSocio(sociosAgregados)

        #una vez ejecutada la función se muestra el MENU nuevamente.
        op = verMenu(op)
    
    if op == 3:
        
        mostarLegajos(sociosAgregados)

        #una vez ejecutada la función se muestra el MENU nuevamente.
        op = verMenu(op)
    
    if op == 4:

        modificarCondicion(sociosAgregados)

        #una vez ejecutada la función se muestra el MENU nuevamente.
        op = verMenu(op)
    if op == 5:
        
        recaudacion(sociosAgregados)

        #una vez ejecutada la función se muestra el MENU nuevamente.
        op = verMenu(op)


    #Salida del programa.
    if op == 6:
        print("----------------------------------------")

print("------------FIN DEL PROGRAMA--------------")



 