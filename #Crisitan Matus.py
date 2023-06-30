#Crisitan Matus
# ---- Construir soluciones de algoritmos de acuerdo con las instrucciones necesarias que den solución al requerimiento del cliente
# ---- Un liceo técnico profesional necesita registrar todos los datos de sus alumnos matriculados para las carreras de técnico 
#   enenfermería y contabilidad. Se requiere construir un programa con un MENU que contenga las siguientes opciones:
# 
# 3) GRABAR: Corresponde a guardar ciertos datos de un Alumno, entre ellos: 
#    LEND[Rut, Nombre, Apellido, Fecha de nacimiento, carrera,asignaturas (nombre y promedio)].
#   Además, debe //VERIFICAR// que el Rut tenga 8 dígitos, seguidos de un guion, y luego una letra ‘k’ o un número,
#   el nombre considere entre 2 y 12 caracteres y el [promedio] sea entre (1.0 y 7.0) IF
# 
# 4) BUSCAR: Corresponde buscar un [alumno] por su [Rut] y mostrar toda su información almacenada.
# 
# 5) IMPRIMIR CERTIFICADO: Esta opción permite imprimir los certificados de Alumno regular, de notas o de matrícula. 
#   Estos debenser previamente ingresados con valores aleatorios entre $1.000 y $5.000 (RANDINT). 
#   Al imprimir el certificado, debe mostrar el nombre del certificado, el Rut del alumno, el nombre y la carrera. 
#   Además, si el certificado es de notas, debe mostrar las [asignatura y su promedio].

from random import randint

Alumno = [] 
asignatura = []
matricula = randint(1000, 5000) #valor aleatorio
# Rut = rut
# nomb = nombre del alumno
# apell = apellido
# Fnacimiento = fecha de nacimiento
# carrera = nombre de la carrera
# Asig = nombre de la asignatura asignatura
# Prom = promedio


def grabar():
    try:
        while True:
            rut = input(
                "Por favor ingrese su Rut de la siguiente de esta manera ""16643492-0"" (sin las comillas). \n")
            if len(rut) == 10 and rut[:7].isdigit() and rut[8] == "-" and rut[9:].isalnum:
                print("-----------------------------------")
                print(f"Rut: {rut} ingresado correctamente")
                print("-----------------------------------")
                break
            else:
                print("-----------------------------------------------")
                print("Dato ingresado erroneamente, intente nuevamente")
                print("-----------------------------------------------")
        while True:
            nomb = str(input("Su nombre debe contener de 2 a 12 caracteres* \n ingrese nombre :\n "))
            if 2 < len(nomb) < 12:
                print("----------------------------")
                print(f"Dato {nomb} ingresado correctamente")
                print("----------------------------")
                break
            else:
                print("Dato ingresado erroneamente, intente nuevamente")
        while True:
            apell = str(input("ingrese su apellido este debe contener de 2 a 12 caracteres* \n ingrese apellido :\n "))
            if 2 < len(apell) < 12:
                print("----------------------------")
                print(f"Dato {apell} ingresado correctamente")
                print("----------------------------")
                break
            else:
                print("Dato ingresado erroneamente, intente nuevamente")
        
        while True:
            print("Ingrese fecha de nacimiento")
            dia = int(input("ingrese dia:\n"))
            if 0<=dia<=30:
                
                break
            else:
                print("Dato ingresado erroneamente, intente nuevamente")
        while True:
            mes = int(input("ingrese mes:\n"))
            if 1<=mes<=12:
                break
            else:
                print("Dato ingresado erroneamente, intente nuevamente")
        while True:
            ano = int(input("ingrese año:\n"))
            if 0<=ano<=2023:
                break
            else:
                print("Dato ingresado erroneamente, intente nuevamente")
        Fnacimiento = (dia +"/"+ mes + "/" + ano)        
                
        while True:
            carrera = str(input("Ingrese su carrera: "))
            if carrera != int:
                print("----------------------------")
                print(f"Dato {carrera} ingresado correctamente")
                print("----------------------------")
                break
            else:
                print("Dato ingresado erroneamente, intente nuevamente")  
        while True:
            Nlista = int(input("Ingrese su numero de lista: "))
            if carrera != str:
                print("----------------------------")
                print(f"Dato {Nlista} ingresado correctamente")
                print("----------------------------")
                break
            else:
                print("Dato ingresado erroneamente, intente nuevamente")
       
        Alumno.append([rut, nomb, apell, Fnacimiento, carrera, Nlista])
        asignaturaprom(rut)
    except ValueError:
        print("--------------------")
        print("Error dato no valido")
        print("--------------------")


def asignaturaprom(rut):
    try:
        Asig = str(input("Ingrese la asignatura: "))
        while True:
            prom = float(input("Ingrese su promedio de notas: "))
            if 1 <=prom<= 7:
                break
            else:
                print("Promedio debe ser entre 1.0 a 7.0")
        for i in range(len(Alumno)):
            if Alumno[i][0] == rut:
                asignatura.insert(i, [Asig, prom])
                break
            elif Alumno[i][0] != rut:
                print("-------------")
                print("Rut no valido")
                print("--------------")
    except ValueError:
        print("-------------------")
        print("ingrese solo Numero")
        print("-------------------")


def buscar():
    if not Alumno:
        print("-------------")
        print("no encontrado")
        print("-------------")
        return
    for i in range(len(Alumno)):
        if Alumno[i][0] == rut:
            print(f"Rut: {Alumno[i][0]}")
            print(f"Nombre: {Alumno[i][1]}")
            print(f"Apellido: {Alumno[i][2]}")
            print(f"Fecha nacimiento: {Alumno[i][3]}")
            print(f"Carrera: {Alumno[i][4]}")
            print(f"Numero lista: {Alumno[i][5]}")
            print(f"Asignatura: {asignatura[i][0]}")
            print(f"Promedio: {asignatura[i][1]}")
            break
        elif Alumno[i][0] != rut:
            print("----------------")
            print("rut no encontrado")
            print("----------------")


def certificados():
    if not Alumno:
        print("-----------------")
        print("rut no registrado")
        print("-----------------")
        return
    try:
        print("--------------------------")
        print("1) Certificado de notas.\n")
        print("2) Certificado de matricula.\n")
        print("3) Certificado alumno regular.")
        print("---------------------------")
        opCert = int(input("Elija una opc "))
        if opCert == 1:
            print("Certificado de notas")
            for i in range(len(Alumno)):
                if Alumno[i][0] == rut:
                    print(f"Rut: {Alumno[i][0]}")
                    print(f"Nombre: {Alumno[i][1]}")
                    print(f"Carrera: {Alumno[i][4]}")
                    for i in range(len(Alumno)):
                        if Alumno[i][0] == rut:
                            print(f"Asignatura: {asignatura[i][0]}")
                            print(f"Promedio: {asignatura[i][1]}")
                            break
                        elif Alumno[i][0] != rut:
                            print("Rut no registrado")
        elif opCert == 2:
            print("certificado matricula")
            for i in range(len(Alumno)):
                if Alumno[i][0] == rut:
                    print(f"Rut: {Alumno[i][0]}")
                    print(f"Nombre: {Alumno[i][1]}")
                    print(f"Carrera: {Alumno[i][4]}")
                    print(f"Matricula ${matricula}")
                    break
                elif Alumno[i][0] != rut:
                    print("Rut no registrado")
        elif opCert == 3:
            print("Certificado alumno regular")
            for i in range(len(Alumno)):
                if Alumno[i][0] == rut:
                    print("\n-------------------------")
                    print(f"* Rut: {Alumno[i][0]}")
                    print(f"* Nombre: {Alumno[i][1]}")
                    print(f"* Carrera: {Alumno[i][4]}")
                    print("-------------------------\n")
                    break
                elif Alumno[i][0] != rut:
                    print("Rut no encontrado")
        else:
            print("-----------------------------------")
            print("Opcion no valida ingrese nuevamente")
            print("-----------------------------------")
    except ValueError:
        print("--------------------")
        print("Ingrese solo NUMEROS")
        print("--------------------")


while True:
    try:
        print("Bienvenido")
        print("1) Ingresar  Nombre del alumno")
        print("2) Buscar alumno por RUT")
        print("3) Buscar certificado")
        print("4) Salir")

        opcM = int(input("Ingrese una opcion : "))  
        if opcM == 1:
            grabar()
        elif opcM == 2:
            rut = input("Ingrese Rut: ")
            buscar()
        elif opcM == 3:
            rut = input("Ingrese Rut del cestificado a buscar: ")
            certificados()
        elif opcM == 4:
            print("Que tenga un buen dia")
            break
        else:
            print("Opcion no valida, intente nuevamente")
    except ValueError:
        print("dato ingresado erroneamente ")
