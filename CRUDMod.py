from io import open
from fpdf import FPDF
import os

h=0
torres=["B","C","B","A","A"]
pisos=["2","1","7","6","5"]
dptos=["1","2","3","4","5"]
habitacioness=["4","7","4","8","9"]
mtcubiertoss=["20","20","30","100","50"]
luzz=["15","25","35","45","55"]
aguas=["11","22","33","44","55"]
gass=["18","26","34","47","51"]
luzzconsumida = []
aguasconsumida = []
gassconsumida = []
pagannormaldepa = []
pagandobledepa = []

torresp = ["B","C","B","A","A"]
pisosp = ["2","1","7","6","5"]
dptosp = ["1","2","3","4","5"]
nombresyapellidos = ["Juan Perez","Maria Lopez","Carlos Gomez","Ana Fernandez","Luis Martinez"]
habitantess = ["4","7","4","8","9"]
fechasc = ["01/01/2020","02/02/2021","03/03/2022","04/04/2023","05/05/2024"]
fechasv = ["00/00/0000","00/00/0000","00/00/0000","00/00/0000","00/00/0000"]
cocheras = ["s","n","s","n","s"]
gyms= ["s","n","s","n","s"]
sums= ["s","n","s","n","s"]
dsums = ["0","0","0","0","0"]
dsumsconsumo = []

torresc = ["A","B","C","A","B"]
pisosc = ["1","2","3","4","5"]
dptosc = ["1","2","3","4","5"]
mtcubiertossc = ["20","30","40","50","60"]
libres = ["s","n","s","n","s"]
impuestopcialdepas = []
impuestopcialcochs = []
pagannormalcoch = []
paga20pcientomascoch = []

def pedir_numero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print("❌ Por favor, ingrese solo números enteros.")

while True:
    print("-----------------------------------------------------------------------")
    print("                 Menu principal de departamento                       ")
    print("-----------------------------------------------------------------------")
    print(" 1 - 🏠 Departamentos")
    print(" 2 - 👤 Propietarios")
    print(" 3 - 🚗 Cocheras")
    print(" 4 - 💰 Liquidación")
    print(" 0 - ⛔ Salir")
    print("-----------------------------------------------------------------------")
    op = input("Ingrese una opción: ")
    if op == "1":
        while True:
            torre = ""
            piso = ""
            ndpto = ""
            habitaciones = ""
            mtcubiertos = ""
            luz = ""
            agua = ""
            gas = ""
            dt= ""
            h= 0
            op = ""
            print("-------------------------------------------------------------")
            print("                       Menu de departamentos                 ")
            print("-------------------------------------------------------------")
            print(" 1 - ➕ Cargar departamento")
            print(" 2 - ❌ Eliminar departamento")
            print(" 3 - ✏️ Modificar departamento")
            print(" 4 - 🔍 Consultar departamento")
            print(" 5 - 📋 Listar departamentos")
            print(" 0 - ⛔ Volver")
            print("-------------------------------------------------------------")
            op = input("Ingrese una opción: ")

            if op == "1":
                print("Cargar departamento")
                while True:
                    while torre != "A" and torre != "B" and torre != "C":
                        torre= input("Ingrese la torre (A/B/C): ").upper()
                    piso = pedir_numero("Ingrese el piso: ")
                    ndpto = pedir_numero("Ingrese el numero de departamento: ")

                    existe = False
                    for h in range(len(torres)):
                        if torres[h] == torre and pisos[h] == piso and dptos[h] == ndpto:
                            existe = True
                            break
                    if existe == True:
                        print("El departamento ya existe.")
                        torre = ""
                        continue
                    else:
                        break
                habitaciones = pedir_numero("Ingrese la cantidad de habitaciones: ")
                mtcubiertos = pedir_numero("Ingrese los metros cubiertos: ")
                luz = pedir_numero("Ingrese el consumo de luz: ")
                agua = pedir_numero("Ingrese el consumo de agua: ")
                gas = pedir_numero("Ingrese el consumo de gas: ")
                while op != "s" and op != "n":
                    op= input("Confirmar datos? (S/N): ").lower()
                if op == "s":
                    torres.append(torre)
                    pisos.append(piso)
                    dptos.append(ndpto)
                    habitacioness.append(habitaciones)
                    mtcubiertoss.append(mtcubiertos)
                    luzz.append(luz)
                    aguas.append(agua)
                    gass.append(gas)
                    print("Departamento cargado exitosamente.")
                else:
                    print("Carga de departamento cancelada.")
            elif op == "2":
                print("Eliminar departamento")
                while True:
                    while torre != "A" and torre != "B" and torre != "C":
                        torre= input("Ingrese la torre (A/B/C): ").upper()
                    piso =  pedir_numero("Ingrese el piso: ")
                    ndpto =  pedir_numero("Ingrese el numero de departamento: ")

                    existe = False
                    for i in range(len(torres)):
                        if torres[i] == torre and pisos[i] == piso and dptos[i] == ndpto:
                            existe = True
                            break
                    if existe == False:
                        print("El departamento no existe.")
                        op = ""
                        while op != "s" and op != "n":
                            op = input("¿Desea volver al menú de departamentos? (S/N): ").lower()
                        if op == "s":
                            op = "regresar"
                            break
                        torre = ""
                        continue
                    else:
                        break
                if op == "regresar":
                    continue
                while op != "s" and op != "n":
                    op = input("Esta seguro que desea eliminar el departamento? (S/N): ").lower()
                if op == "s":
                    print("No se puede eliminar un departamento")
                else:
                    print("Eliminacion de departamento cancelada.")
            elif op == "3":
                print("Modificar departamento")
                while True:
                    while torre != "A" and torre != "B" and torre != "C":
                        torre= input("Ingrese la torre (A/B/C): ").upper()
                    piso =  pedir_numero("Ingrese el piso: ")
                    ndpto =  pedir_numero("Ingrese el numero de departamento: ")

                    existe = False
                    for h in range(len(torres)):
                        if torres[h] == torre and pisos[h] == piso and dptos[h] == ndpto:
                            existe = True
                            break
                        else:
                            break
                    if existe == False:
                        print("El departamento no existe.")
                        op = ""
                        while op != "s" and op != "n":
                            op = input("¿Desea volver al menú de propietarios? (S/N): ").lower()
                        if op == "s":
                            op = "regresar"
                            break
                        torre = ""
                        continue
                    else:
                        break
                if op == "regresar":
                    continue
                print("---------------------------------------------------------------------")
                print("               Ingrese qué quiere modificar                         ")
                print("---------------------------------------------------------------------")
                print(" 1 - Habitaciones")
                print(" 2 - Metros cubiertos")
                print(" 3 - Consumo de luz")
                print(" 4 - Consumo de agua")
                print(" 5 - Consumo de gas")
                print("---------------------------------------------------------------------")
                op = input("Ingrese una opción: ")
                if op == "1":
                    dt= "1"
                    habitaciones = pedir_numero("Ingrese la nueva cantidad de habitaciones: ")
                elif op == "2":
                    dt = "2"
                    mtcubiertos = pedir_numero("Ingrese los nuevos metros cubiertos: ")
                elif op == "3":
                    dt= "3"
                    luz = pedir_numero("Ingrese el nuevo consumo de luz: ")
                elif op == "4":
                    dt = "4"
                    agua = pedir_numero("Ingrese el nuevo consumo de agua: ")
                elif op == "5":
                    dt = "5"
                    gas = pedir_numero("Ingrese el nuevo consumo de gas: ")
                else:
                    print("Opcion invalida.")
                while op != "s" and op != "n":
                    op = input("Confirmar modificacion? (S/N): ").lower()
                if op == "s":
                    print("Modificacion de departamento confirmada.")
                    if dt == "1":
                        habitacioness[h] = habitaciones
                    elif dt == "2":
                        mtcubiertoss[h] = mtcubiertos
                    elif dt == "3":
                        luzz[h] = luz
                    elif dt == "4":
                        aguas[h] = agua
                    elif dt == "5":
                        gass[h] = gas
                else:
                    print("Modificacion de departamento cancelada.")
            elif op == "4":
                print("---------------------------------------------------------------------")
                print("                  Consultar departamento                             ")
                print("         Elija opción para filtrar la consulta                      ")
                print("---------------------------------------------------------------------")
                print(" 1 - Consultar por torre")
                print(" 2 - Consultar por torre y piso")
                print(" 3 - Consultar por torre, piso y departamento")
                print("---------------------------------------------------------------------")
                op = input("Ingrese una opción: ")
                if op == "1":
                    while torre != "A" and torre != "B" and torre != "C":
                        torre= input("Ingrese la torre (A/B/C): ").upper()
                    encontrado = False
                    for h in range(len(torres)):
                        if torres[h] == torre:
                            print(f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}")
                            encontrado = True
                    if encontrado == False:
                        print("No se encontraron departamentos en la torre", torre)
                elif op == "2":
                    while torre != "A" and torre != "B" and torre != "C":
                        torre= input("Ingrese la torre (A/B/C): ").upper()
                    piso = pedir_numero("Ingrese el piso: ")  
                    encontrado = False
                    for h in range(len(torres)):
                        if torres[h] == torre and pisos[h] == piso:
                            print(f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}")
                            encontrado = True
                    if encontrado == False:
                        print(f"No se encontraron departamentos en la torre {torre}, piso {piso}")
                elif op == "3":
                    while torre != "A" and torre != "B" and torre != "C":
                        torre= input("Ingrese la torre (A/B/C): ").upper()
                    piso = pedir_numero("Ingrese el piso: ")
                    ndpto = pedir_numero("Ingrese el numero de departamento: ")
                    encontrado = False
                    for h in range(len(torres)):
                        if torres[h] == torre and pisos[h] == piso and dptos[h] == ndpto:
                            print(f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}")
                    if encontrado == False:
                        print(f"No se encontraron departamentos en la torre {torre}, piso {piso}, departamento {ndpto}")
            elif op == "5":
                print("---------------------------------------------------------------------")
                print("                   Listar departamentos                              ")
                print("         Elija opción para filtrar la consulta                      ")
                print("---------------------------------------------------------------------")
                print(" 1 - Consultar por torre")
                print(" 2 - Consultar por torre y piso")
                print(" 3 - Consultar por torre, piso y departamento")
                print("---------------------------------------------------------------------")
                op = input("Ingrese una opción: ")
                if op == "1":
                    while torre != "A" and torre != "B" and torre != "C":
                        torre= input("Ingrese la torre (A/B/C): ").upper()
                    for h in range(len(torres)):
                        if torres[h] == torre:
                            frase = f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}"
                            print(frase)
                            archivo = open("listado.txt", "a")
                            archivo.write(frase + '\n')
                            archivo.close()
                elif op == "2":
                    while torre != "A" and torre != "B" and torre != "C":
                        torre= input("Ingrese la torre (A/B/C): ").upper()
                    piso = pedir_numero("Ingrese el piso: ")
                    for h in range(len(torres)):
                        if torres[h] == torre and pisos[h] == piso:
                            frase = f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}"
                            print(frase)
                            archivo = open("listado.txt", "a")
                            archivo.write(frase + '\n')
                            archivo.close()
                elif op == "3":
                    while torre != "A" and torre != "B" and torre != "C":
                        torre= input("Ingrese la torre (A/B/C): ").upper()
                    piso = pedir_numero("Ingrese el piso: ")
                    ndpto = pedir_numero("Ingrese el numero de departamento: ")
                    for h in range(len(torres)):
                        if torres[h] == torre and pisos[h] == piso and dptos[h] == ndpto:
                            frase = f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}"
                            print(frase)
                            archivo = open("listado.txt", "a")
                            archivo.write(frase + '\n')
                            archivo.close()
                print("La información se ha guardado en listado.txt.")
            elif op == "0":
                break
            else:
                print("Opcion invalida. Intente de nuevo.")
    elif op == "2":
        while True:
            torrep = ""
            pisop = ""
            ndptop = ""
            habitantes = ""
            nombreyapellido = ""
            fechac = ""
            fechav = ""
            gym = ""
            sum = ""
            dsum = ""
            dt= ""
            h= 0
            op = ""
            print("-----------------------------------------------------------------")
            print("                     Menú de propietarios                       ")
            print("-----------------------------------------------------------------")
            print(" 1 - ➕ Cargar propietario")
            print(" 2 - ➖ Eliminar propietario")
            print(" 3 - ✏️ Modificar propietario")
            print(" 4 - 🔍 Consultar propietario")
            print(" 5 - 📋 Listar propietarios")
            print(" 0 - ⛔ Volver")
            print("-----------------------------------------------------------------")
            op = input("Ingrese una opción: ")
            if op == "1":
                print("Cargar propietario")
                while True:
                    while torrep != "A" and torrep != "B" and torrep != "C":
                        torrep= input("Ingrese la torre (A/B/C): ").upper()
                    pisop = pedir_numero("Ingrese el piso: ")
                    ndptop = pedir_numero("Ingrese el numero de departamento: ")

                    existe = True
                    for h in range(len(torres)):
                        if torres[h] == torrep and pisos[h] == pisop and dptos[h] == ndptop:
                            existe = True
                            break
                        else:
                            existe = False
                            break
                    if existe == False:
                        print("El departamento no existe.")
                        op = ""
                        while op != "s" and op != "n":
                            op = input("¿Desea volver al menú de propietarios? (S/N): ").lower()
                        if op == "s":
                            op = "regresar"
                            break
                        torrep = ""
                        continue
                    else:
                        break
                if op == "regresar":
                    continue
                nombreyapellido = input("Ingrese el nombre y apellido del propietario: ")
                habitantes = pedir_numero("Ingrese la cantidad de habitantes: ")
                dia = pedir_numero("Ingrese el dia de compra del departamento: ")
                mes = pedir_numero("Ingrese el mes de compra del departamento: ")
                anio = pedir_numero("Ingrese el año de compra del departamento: ")
                fechac = f"{dia}/{mes}/{anio}"
                fechav = "00/00/0000"  
                while gym != "s" and gym != "n":
                    gym = input("¿El propietario tiene acceso al gimnasio? (S/N): ").lower()
                while sum != "s" and sum != "n":
                    sum = input("¿El propietario tiene acceso al SUM? (S/N): ").lower()
                while cochera != "s" and cochera != "n":
                    cochera = input("¿El propietario tiene cochera? (S/N): ").lower()
                if sum == "s":
                    dsum = pedir_numero("Ingrese la cantidad de dias de uso del SUM: ")
                else:
                    dsum = "0"
                while op != "s" and op != "n":
                    op= input("Confirmar datos? (S/N): ").lower()
                if op == "s":
                    torresp.append(torrep)
                    pisosp.append(pisop)
                    dptosp.append(ndptop)
                    nombresyapellidos.append(nombreyapellido)
                    habitantess.append(habitantes)
                    fechasc.append(fechac)
                    fechasv.append(fechav)
                    cocheras.append(cochera)
                    gyms.append(gym)
                    sums.append(sum)
                    dsums.append(dsum)
                    print("Propietario cargado exitosamente.")
                else:
                    print("Carga de propietario cancelada.")
            elif op == "2":
                print("Eliminar propietario")
                while True:
                    while torrep != "A" and torrep != "B" and torrep != "C":
                        torrep= input("Ingrese la torre (A/B/C): ").upper()
                    pisop = pedir_numero("Ingrese el piso: ")
                    ndptop = pedir_numero("Ingrese el numero de departamento: ")
                    existe = False
                    for h in range(len(torresp)):
                        if torresp[h] == torrep and pisosp[h] == pisop and dptosp[h] == ndptop:
                            existe = True
                            break
                    if existe == False:
                        print("El propietario no existe.")
                        op = ""
                        while op != "s" and op != "n":
                            op = input("¿Desea volver al menú de propietarios? (S/N): ").lower()
                        if op == "s":
                            op = "regresar"
                            break
                        torrep = ""
                        continue
                    else:
                        break
                if op == "regresar":
                    continue
                while op != "s" and op != "n":
                    op = input("Esta seguro que desea eliminar el propietario? (S/N): ").lower()
                if op == "s":
                    dia = pedir_numero("Ingrese el dia de la venta del departamento: ")
                    mes = pedir_numero("Ingrese el mes de la venta del departamento: ")
                    anio = pedir_numero("Ingrese el año de la venta del departamento: ")
                    fechav = f"{dia}/{mes}/{anio}"
                    fechasv[h] = fechav
                    print("Propietario eliminado exitosamente.")
                else:
                    print("Eliminacion de propietario cancelada.")
            elif op == "3":
                print("Modificar propietario")
                while True:
                    while torrep != "A" and torrep != "B" and torrep != "C":
                        torrep= input("Ingrese la torre (A/B/C): ").upper()
                    pisop = pedir_numero("Ingrese el piso: ")
                    ndptop = pedir_numero("Ingrese el numero de departamento: ")

                    existe = False
                    for h in range(len(torresp)):
                        if torresp[h] == torrep and pisosp[h] == pisop and dptosp[h] == ndptop:
                            existe = True
                            break
                    if existe == False:
                        print("El propietario no existe.")
                        op = ""
                        while op != "s" and op != "n":
                            op = input("¿Desea volver al menú de propietarios? (S/N): ").lower()
                        if op == "s":
                            op = "regresar"
                            break
                        torrep = ""
                        continue
                    else:
                        break
                if op == "regresar":
                    continue
                print("-------------------------------------------------------------------")
                print("                 Ingrese qué quiere modificar                      ")
                print("-------------------------------------------------------------------")
                print(" 1 - Habitantes")
                print(" 2 - Fecha de compra")
                print(" 3 - Gym")
                print(" 4 - Sum")
                print(" 5 - Días de uso del Sum")
                print("-------------------------------------------------------------------")
                op = input("Ingrese una opción: ")

                if op == "1":
                    dt = "1"
                    habitantes = pedir_numero("Ingrese la nueva cantidad de habitantes: ")
                elif op == "2":
                    dt = "2"
                    dia = pedir_numero("Ingrese el nuevo dia de compra del departamento: ")
                    mes = pedir_numero("Ingrese el nuevo mes de compra del departamento: ")
                    anio = pedir_numero("Ingrese el nuevo año de compra del departamento: ")
                    fechac = f"{dia}/{mes}/{anio}"
                elif op == "3":
                    dt = "3"
                    while gym != "s" and gym != "n":
                        gym = input("¿El propietario tiene acceso al gimnasio? (S/N): ").lower()
                elif op == "4":
                    dt = "4"
                    while sum != "s" and sum != "n":
                        sum = input("¿El propietario tiene acceso al SUM? (S/N): ").lower()
                elif op == "5":
                    dt = "5"
                    dsum = pedir_numero("Ingrese la nueva cantidad de dias de uso del SUM: ")
                else:
                    print("Opcion invalida.")
                while op != "s" and op != "n":
                    op = input("Confirmar modificacion? (S/N): ").lower()
                if op == "s":
                    print("Modificacion de propietario confirmada.")
                    if dt == "1":
                        habitantess[h] = habitantes
                    elif dt == "2":
                        fechasc[h] = fechac
                    elif dt == "3":
                        gyms[h] = gym
                    elif dt == "4":
                        sums[h] = sum
                    elif dt == "5":
                        dsums[h] = dsum
                else:
                    print("Modificacion de propietario cancelada.")
            elif op == "4":
                print("---------------------------------------------------------------------")
                print("                    Consultar propietario                            ")
                print("                Elija opción para filtrar la consulta                ")
                print("---------------------------------------------------------------------")
                print(" 1 - Consultar por nombre y apellido")
                print(" 2 - Consultar por torre y piso")
                print(" 3 - Consultar por torre, piso y departamento")
                print("---------------------------------------------------------------------")
                op = input("Ingrese una opción: ")
                if op == "1":
                    nombreyapellido = input("Ingrese el nombre y apellido del propietario: ")
                    encontrado = False
                    for h in range(len(nombresyapellidos)):
                        if nombresyapellidos[h] == nombreyapellido:
                            print(f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre y Apellido: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Fecha de compra: {fechasc[h]}, Fecha de venta: {fechasv[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Dias de uso del Sum: {dsums[h]}")
                            encontrado = True
                    if not encontrado:
                        print(f"No se encontraron propietarios con nombre y apellido: {nombreyapellido}")
                elif op == "2":
                    while torrep != "A" and torrep != "B" and torrep != "C":
                        torrep= input("Ingrese la torre (A/B/C): ").upper()
                    pisop = pedir_numero("Ingrese el piso: ")
                    encontrado = False
                    for h in range(len(torresp)):
                        if torresp[h] == torrep and pisosp[h] == pisop:
                            print(f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre y Apellido: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Fecha de compra: {fechasc[h]}, Fecha de venta: {fechasv[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Dias de uso del Sum: {dsums[h]}")
                            encontrado = True
                    if not encontrado:
                        print(f"No se encontraron propietarios en la torre {torrep}, piso {pisop}")
                elif op == "3":
                    while torrep != "A" and torrep != "B" and torrep != "C":
                        torrep= input("Ingrese la torre (A/B/C): ").upper()
                    pisop = pedir_numero("Ingrese el piso: ")
                    ndptop = pedir_numero("Ingrese el numero de departamento: ")
                    encontrado = False
                    for h in range(len(torresp)):
                        if torresp[h] == torrep and pisosp[h] == pisop and dptosp[h] == ndptop:
                            print(f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre y Apellido: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Fecha de compra: {fechasc[h]}, Fecha de venta: {fechasv[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Dias de uso del Sum: {dsums[h]}")
                            encontrado = True
                    if not encontrado:
                        print(f"No se encontraron propietarios en la torre {torrep}, piso {pisop}, departamento {ndptop}")
            elif op == "5":
                print("---------------------------------------------------------------------")
                print("                    Listar propietarios                              ")
                print("                Elija opción para filtrar la consulta                ")
                print("---------------------------------------------------------------------")
                print(" 1 - Consultar por nombre y apellido")
                print(" 2 - Consultar por torre y piso")
                print(" 3 - Consultar por torre, piso y departamento")
                print("---------------------------------------------------------------------")
                op = input("Ingrese una opción: ")
                if op == "1":
                    nombreyapellido = input("Ingrese el nombre y apellido del propietario: ")
                    for h in range(len(nombresyapellidos)):
                        if nombresyapellidos[h] == nombreyapellido:
                            frase = f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre y Apellido: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Fecha de compra: {fechasc[h]}, Fecha de venta: {fechasv[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Dias de uso del Sum: {dsums[h]}"
                            print(frase)
                            archivo = open("listado.txt", "a")
                            archivo.write(frase + '\n')
                            archivo.close()
                elif op == "2":
                    while torrep != "A" and torrep != "B" and torrep != "C":
                        torrep= input("Ingrese la torre (A/B/C): ").upper()
                    pisop = pedir_numero("Ingrese el piso: ")
                    for h in range(len(torresp)):
                        if torresp[h] == torrep and pisosp[h] == pisop:
                            frase = f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre y Apellido: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Fecha de compra: {fechasc[h]}, Fecha de venta: {fechasv[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Dias de uso del Sum: {dsums[h]}"
                            print(frase)
                            archivo = open("listado.txt", "a")
                            archivo.write(frase + '\n')
                            archivo.close()
                elif op == "3":
                    while torrep != "A" and torrep != "B" and torrep != "C":
                        torrep= input("Ingrese la torre (A/B/C): ").upper()
                    pisop = pedir_numero("Ingrese el piso: ")
                    ndptop = pedir_numero("Ingrese el numero de departamento: ")
                    for h in range(len(torresp)):
                        if torresp[h] == torrep and pisosp[h] == pisop and dptosp[h] == ndptop:
                            frase = f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre y Apellido: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Fecha de compra: {fechasc[h]}, Fecha de venta: {fechasv[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Dias de uso del Sum: {dsums[h]}"
                            print(frase)
                            archivo = open("listado.txt", "a")
                            archivo.write(frase + '\n')
                            archivo.close()
            elif op == "0":
                break
            else:
                print("Opcion invalida. Intente de nuevo.")
    elif op == "3":
        while True:
            h = 0
            op = ""
            torrec = ""
            pisoc = ""
            dptoc = ""
            mtcubiertosc = ""
            libre = ""
            dt= ""
            print("------------------------------------------------------------")
            print("                     Menú de cocheras                       ")
            print("------------------------------------------------------------")
            print(" 1 - ➕ Cargar cochera")
            print(" 2 - ✏️ Modificar cochera")
            print(" 3 - 🔍 Consultar cochera")
            print(" 4 - 📋 Listar cocheras")
            print(" 0 - ⛔ Volver")
            print("------------------------------------------------------------")
            op = input("Ingrese una opción: ")
            if op == "1":
                print("Cargar cochera")
                while True:
                    while torrec != "A" and torrec != "B" and torrec != "C":
                        torrec = input("Ingrese la torre (A/B/C): ").upper()
                    pisoc = pedir_numero("Ingrese el piso: ")
                    dptoc = pedir_numero("Ingrese el numero de departamento: ")
                    existe = False
                    for h in range(len(torresc)):
                        if torresc[h] == torrec and pisosc[h] == pisoc and dptosc[h] == dptoc:
                            existe = True
                            break
                        else:
                            existe = False
                            break
                    if existe == True:
                        print("La cochera ya existe.")
                        torrec = ""
                        continue
                    else:
                        break
                mtcubiertosc = pedir_numero("Ingrese los metros cubiertos de la cochera: ")
                while libre != "s" and libre != "n":
                    libre = input("¿La cochera esta libre? (S/N): ").lower()
                while op != "s" and op != "n":
                    op= input("Confirmar datos? (S/N): ").lower()
                if op == "s":
                    torresc.append(torrec)
                    pisosc.append(pisoc)
                    dptosc.append(dptoc)
                    mtcubiertossc.append(mtcubiertosc)
                    libres.append(libre)
                    print("Cochera cargada exitosamente.")
                else:
                    print("Carga de cochera cancelada.")                     
            elif op == "2":
                print("Modificar cochera")
                while True:
                    while torrec != "A" and torrec != "B" and torrec != "C":
                        torrec = input("Ingrese la torre (A/B/C): ").upper()
                    pisoc = pedir_numero("Ingrese el piso: ")
                    dptoc = pedir_numero("Ingrese el numero de departamento: ")

                    existe = False
                    for h in range(len(torresc)):
                        if torresc[h] == torrec and pisosc[h] == pisoc and dptosc[h] == dptoc:
                            existe = True
                            break
                    if existe == False:
                        print("La cochera no existe.")
                        op = ""
                        while op != "s" and op != "n":
                            op = input("¿Desea volver al menú de cocheras? (S/N): ").lower()
                        if op == "s":
                            op = "regresar"
                            break
                        torrec = ""
                        continue
                    else:
                        break
                if op == "regresar":
                    continue
                print("--------------------------------------------------------")
                print("                Ingrese qué quiere modificar            ")
                print("--------------------------------------------------------")
                print(" 1 - Metros cubiertos")
                print(" 2 - Cochera libre (S/N)")
                print("--------------------------------------------------------")
                op = input("Ingrese una opción: ")
                if op == "1":
                    dt = "1"
                    mtcubiertosc = pedir_numero("Ingrese los nuevos metros cubiertos de la cochera: ")
                elif op == "2":
                    dt = "2"
                    while libre != "s" and libre != "n":
                        libre = input("¿La cochera esta libre? (S/N): ").lower()
                else:
                    print("Opcion invalida.")
                while op != "s" and op != "n":
                    op = input("Confirmar modificacion? (S/N): ").lower()
                if op == "s":
                    print("Modificacion de cochera confirmada.")
                    if dt == "1":
                        mtcubiertossc[h] = mtcubiertosc
                    elif dt == "2":
                        libres[h] = libre
                else:
                    print("Modificacion de cochera cancelada.")
            elif op == "3":
                print("---------------------------------------------------------------------")
                print("                    Consultar cochera                               ")
                print("                Elija opción para filtrar la consulta               ")
                print("---------------------------------------------------------------------")
                print(" 1 - Consultar por torre")
                print(" 2 - Consultar por torre y piso")
                print(" 3 - Consultar por torre, piso y departamento")
                print("---------------------------------------------------------------------")
                op = input("Ingrese una opción: ")
                if op == "1":
                    while torrec != "A" and torrec != "B" and torrec != "C":
                        torrec = input("Ingrese la torre: ").upper()
                    for h in range(len(torresc)):
                        if torresc[h] == torrec:
                            print(f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Departamento: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}")
                elif op == "2":
                    while torrec != "A" and torrec != "B" and torrec != "C":
                        torrec = input("Ingrese la torre: ").upper()
                    pisoc = pedir_numero("Ingrese el piso: ")
                    for h in range(len(torresc)):
                        if torresc[h] == torrec and pisosc[h] == pisoc:
                            print(f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Departamento: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}")
                elif op == "3":
                    while torrec != "A" and torrec != "B" and torrec != "C":
                        torrec = input("Ingrese la torre: ").upper()
                    pisoc = pedir_numero("Ingrese el piso: ")
                    dptoc = pedir_numero("Ingrese el numero de departamento: ")
                    for h in range(len(torresc)):
                        if torresc[h] == torrec and pisosc[h] == pisoc and dptosc[h] == dptoc:
                            print(f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Departamento: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}")
            elif op == "4":
                print("---------------------------------------------------------------------")
                print("                      Listar cocheras                               ")
                print("                 Elija opción para filtrar la consulta              ")
                print("---------------------------------------------------------------------")
                print(" 1 - Consultar por torre")
                print(" 2 - Consultar por torre y piso")
                print(" 3 - Consultar por torre, piso y departamento")
                print("---------------------------------------------------------------------")
                op = input("Ingrese una opción: ")
                if op == "1":
                    while torrec != "A" and torrec != "B" and torrec != "C":
                        torrec = input("Ingrese la torre: ").upper()
                    for h in range(len(torresc)):
                        if torresc[h] == torrec:
                            frase = f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Departamento: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}"
                            print(frase)
                            archivo = open("listado.txt", "a")
                            archivo.write(frase + '\n')
                            archivo.close()
                elif op == "2":
                    while torrec != "A" and torrec != "B" and torrec != "C":
                        torrec = input("Ingrese la torre: ").upper()
                    pisoc = pedir_numero("Ingrese el piso: ")
                    for h in range(len(torresc)):
                        if torresc[h] == torrec and pisosc[h] == pisoc:
                            frase = f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Departamento: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}"
                            print(frase)
                            archivo = open("listado.txt", "a")
                            archivo.write(frase + '\n')
                            archivo.close()
                elif op == "3":
                    while torrec != "A" and torrec != "B" and torrec != "C":
                        torrec = input("Ingrese la torre: ").upper()
                    pisoc = pedir_numero("Ingrese el piso: ")
                    dptoc = pedir_numero("Ingrese el numero de departamento: ")
                    for h in range(len(torresc)):
                        if torresc[h] == torrec and pisosc[h] == pisoc and dptosc[h] == dptoc:
                            frase = f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Departamento: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}"
                            print(frase)
                            archivo = open("listado.txt", "a")
                            archivo.write(frase + '\n')
                            archivo.close()
                print("La información se ha guardado en listado.txt.")
            elif op == "0":
                break
            else:
                print("Opcion invalida. Intente de nuevo.")
    elif op == "0":
        print("Saliendo del programa.")
        break
    elif op == "4":
        # Punto 1 
        pagaeldobleA = 0
        pagaeldobleB = 0
        pagaeldobleC = 0

        cantidaDeptosA=torres.count("A")
        cantidaDeptosB=torres.count("B")
        cantidaDeptosC=torres.count("C")
        seguridadA=150000/cantidaDeptosA
        seguridadB=150000/cantidaDeptosB
        seguridadC=150000/cantidaDeptosC
        seguridadCocheraA=seguridadA /2
        seguridadCocheraB=seguridadB /2 
        seguridadCocheraC=seguridadC /2
        for i in range(len(mtcubiertoss)):
            if int(mtcubiertoss[i]) >= 100:
                torre = torres[i]
                if torre == "A":
                    pagaeldobleA += seguridadA * 2
                elif torre == "B":
                    pagaeldobleB += seguridadB * 2
                elif torre == "C":
                    pagaeldobleC += seguridadC * 2
        # Punto 2 
        for i in luzz:
            kwconsumido = int(i) * 15000
            luzzconsumida.append(kwconsumido)
        # Punto 3
        for i in aguas:
            m3aguaconsumido = int(i) * 1000
            aguasconsumida.append(m3aguaconsumido)
        # Punto 4
        for i in gass:
            m3gasconsumido = int(i) * 5000
            gassconsumida.append(m3gasconsumido)
        # Punto 5
        sumtotal = sums.count("s")
        sumconsumo = 80000 / sumtotal 
        # Punto 6
        for i in dsums:
            ddsumconsumo = int(i) * 40000
            dsumsconsumo.append(ddsumconsumo)
        # Punto 7
        for i in mtcubiertoss:
            impuestopcialdepa = int(i) * 400
            impuestopcialdepas.append(impuestopcialdepa)
        for i in mtcubiertossc:
            impuestopcialcoch = int(i) * 200
            impuestopcialcochs.append(impuestopcialcoch)
        # Punto 8
        for i in range(len(pisos)):
            if int(pisos[i]) < 5:
                pagannormaldepa.append(i)
            if int(pisos[i]) > 5:
                pagandobledepa.append(i)
        for h in range(len(torresc)):
            if torresc[h] != torresp[h] or pisosc[h] != pisosp[h] or dptosc[h] != dptosp[h]:
                pagannormalcoch.append(h)
            else:
                paga20pcientomascoch.append(h)

        # Punto 9
        aguacomun= len(torresc) * 2000

        print("\n--- Liquidación por Torre ---")
        print("Torre A paga por seguridad:")
        print(" - Por departamento:", int(seguridadA))
        print(" - Por cochera:", int(seguridadCocheraA))
        print("Torre B paga por seguridad:")
        print(" - Por departamento:", int(seguridadB))
        print(" - Por cochera:", int(seguridadCocheraB))
        print("Torre C paga por seguridad (doble):")
        print(" - Por departamento:", int(seguridadC * 2))
        print(" - Por cochera:", int(seguridadCocheraC * 2))
        print("Departamentos mayores a 100m2 pagan el doble:")
        print(" - Torre A:", int(pagaeldobleA))
        print(" - Torre B:", int(pagaeldobleB))
        print(" - Torre C:", int(pagaeldobleC))
        print()

        print("--- Liquidación por Departamento ---")
        for i in range(len(torres)):
            print("Depto", torres[i], "-", pisos[i], "-", dptos[i])
            
            agua = aguasconsumida[i]
            gas = gassconsumida[i]
            luz = luzzconsumida[i]
            impuesto = impuestopcialdepas[i]
            dias_sum = dsumsconsumo[i]

            if sums[i] == "s":
                uso_sum = int(sumconsumo)
            else:
                uso_sum = 0

            if torres[i] == "A":
                luz_comun = seguridadA
            elif torres[i] == "B":
                luz_comun = seguridadB
            else:
                luz_comun = seguridadC * 2  

            if torres[i] == "C":
                uso_sum = uso_sum * 2

            total = agua + gas + luz + impuesto + uso_sum + dias_sum + luz_comun

            print("  Agua:", agua)
            print("  Gas:", gas)
            print("  Luz:", luz)
            print("  Impuesto especial:", impuesto)
            print("  SUM:", uso_sum)
            print("  Días de SUM:", dias_sum)
            print("  Luz común:", int(luz_comun))
            print("  Total a pagar:", int(total))
            print()

        print("--- Liquidación por Cochera ---")
        for i in range(len(torresc)):
            print("Cochera", torresc[i], "-", pisosc[i], "-", dptosc[i])

            impuesto = impuestopcialcochs[i]

            if torresc[i] == "A":
                seguridad = seguridadCocheraA
            elif torresc[i] == "B":
                seguridad = seguridadCocheraB
            else:
                seguridad = seguridadCocheraC * 2  

            total = impuesto + seguridad

            print("  Impuesto especial:", impuesto)
            print("  Seguridad:", int(seguridad))
            print("  Total a pagar:", int(total))
            print()

        print("--- Resumen Final ---")
        total_departamentos = 0
        for i in range(len(torres)):
            agua = aguasconsumida[i]
            gas = gassconsumida[i]
            luz = luzzconsumida[i]
            impuesto = impuestopcialdepas[i]
            dias_sum = dsumsconsumo[i]

            if sums[i] == "s":
                uso_sum = sumconsumo
            else:
                uso_sum = 0

            if torres[i] == "A":
                luz_comun = seguridadA
            elif torres[i] == "B":
                luz_comun = seguridadB
            else:
                luz_comun = seguridadC * 2
                uso_sum = uso_sum * 2

            total = agua + gas + luz + impuesto + uso_sum + dias_sum + luz_comun
            total_departamentos += total

        total_cocheras = 0
        for i in range(len(torresc)):
            impuesto = impuestopcialcochs[i]

            if torresc[i] == "A":
                seguridad = seguridadCocheraA
            elif torresc[i] == "B":
                seguridad = seguridadCocheraB
            else:
                seguridad = seguridadCocheraC * 2 

            total = impuesto + seguridad
            total_cocheras += total

        print("Total departamentos:", int(total_departamentos))
        print("Total cocheras:", int(total_cocheras))
        print("Total general:", int(total_departamentos + total_cocheras))
