from io import open
h=0
torres=["B","C","B","A","A"]
pisos=["2","1","7","6","5"]
dptos=["1","2","3","4","5"]
habitacioness=["4","7","4","8","9"]
mtcubiertoss=["20","20","30","40","50"]
luzz=["15","25","35","45","55"]
aguas=["11","22","33","44","55"]
gass=["18","26","34","47","51"]

torresp = ["B","C","B","A","A"]
pisosp = ["2","1","7","6","5"]
dptosp = ["1","2","3","4","5"]
nombresyapellidos = ["Juan Perez","Maria Lopez","Carlos Gomez","Ana Fernandez","Luis Martinez"]
habitantess = ["4","7","4","8","9"]
fechasc = ["01/01/2020","02/02/2021","03/03/2022","04/04/2023","05/05/2024"]
fechasv = ["00/00/0000","00/00/0000","00/00/0000","00/00/0000","00/00/0000"]
gyms= ["s","n","s","n","s"]
sums= ["s","n","s","n","s"]
dsums = ["0","0","0","0","0"]

torresc = ["A","B","C","A","B"]
pisosc = ["1","2","3","4","5"]
dptosc = ["1","2","3","4","5"]
mtcubiertossc = ["20","30","40","50","60"]
libres = ["s","n","s","n","s"]

while True:
    print("-----------------------------------------------------------------------")
    print("                 Menu principal de departamento                       ")
    print("-----------------------------------------------------------------------")
    print(" 1 - Departamentos")
    print(" 2 - Propietarios")
    print(" 3 - Cocheras")
    print(" 4 - Liquidación")
    print(" 0 - Salir")
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
            print(" 1 - Cargar departamento")
            print(" 2 - Eliminar departamento")
            print(" 3 - Modificar departamento")
            print(" 4 - Consultar departamento")
            print(" 5 - Listar departamentos")
            print(" 0 - Salir")
            print("-------------------------------------------------------------")
            op = input("Ingrese una opción: ")

            if op == "1":
                print("Cargar departamento")
                while True:
                    while torre != "A" and torre != "B" and torre != "C":
                        torre= input("Ingrese la torre (A/B/C): ").upper()
                    piso = input("Ingrese el piso: ")
                    ndpto = input("Ingrese el numero de departamento: ")

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
                habitaciones = input("Ingrese la cantidad de habitaciones: ")
                mtcubiertos = input("Ingrese los metros cubiertos: ")
                luz = input("Ingrese el consumo de luz: ")
                agua = input("Ingrese el consumo de agua: ")
                gas = input("Ingrese el consumo de gas: ")
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
                    piso = input("Ingrese el piso: ")
                    ndpto = input("Ingrese el numero de departamento: ")

                    existe = False
                    for i in range(len(torres)):
                        if torres[i] == torre and pisos[i] == piso and dptos[i] == ndpto:
                            existe = True
                            break
                    if existe == False:
                        print("El departamento no existe.")
                        torre = ""
                        continue
                    else:
                        break
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
                    piso = input("Ingrese el piso: ")
                    ndpto = input("Ingrese el numero de departamento: ")

                    existe = False
                    for h in range(len(torres)):
                        if torres[h] == torre and pisos[h] == piso and dptos[h] == ndpto:
                            existe = True
                            break
                        else:
                            break
                    if existe == False:
                        print("El departamento no existe.")
                        torre = ""
                        continue
                    else:
                        break
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
                    habitaciones = input("Ingrese la nueva cantidad de habitaciones: ")
                elif op == "2":
                    dt = "2"
                    mtcubiertos = input("Ingrese los nuevos metros cubiertos: ")
                elif op == "3":
                    dt= "3"
                    luz = input("Ingrese el nuevo consumo de luz: ")
                elif op == "4":
                    dt = "4"
                    agua = input("Ingrese el nuevo consumo de agua: ")
                elif op == "5":
                    dt = "5"
                    gas = input("Ingrese el nuevo consumo de gas: ")
                else:
                    print("Opcion invalida.")
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
                    for h in range(len(torres)):
                        if torres[h] == torre:
                            print(f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}")
                elif op == "2":
                    while torre != "A" and torre != "B" and torre != "C":
                        torre= input("Ingrese la torre (A/B/C): ").upper()
                    piso = input("Ingrese el piso: ")
                    for h in range(len(torres)):
                        if torres[h] == torre and pisos[h] == piso:
                            print(f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}")
                elif op == "3":
                    while torre != "A" and torre != "B" and torre != "C":
                        torre= input("Ingrese la torre (A/B/C): ").upper()
                    piso = input("Ingrese el piso: ")
                    ndpto = input("Ingrese el numero de departamento: ")
                    for h in range(len(torres)):
                        if torres[h] == torre and pisos[h] == piso and dptos[h] == ndpto:
                            print(f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}")
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
                    piso = input("Ingrese el piso: ")
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
                    piso = input("Ingrese el piso: ")
                    ndpto = input("Ingrese el numero de departamento: ")
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
            print(" 1 - Cargar propietario")
            print(" 2 - Eliminar propietario")
            print(" 3 - Modificar propietario")
            print(" 4 - Consultar propietario")
            print(" 5 - Listar propietarios")
            print(" 0 - Salir")
            print("-----------------------------------------------------------------")
            op = input("Ingrese una opción: ")
            if op == "1":
                print("Cargar propietario")
                while True:
                    while torrep != "A" and torrep != "B" and torrep != "C":
                        torrep= input("Ingrese la torre (A/B/C): ").upper()
                    pisop = input("Ingrese el piso: ")
                    ndptop = input("Ingrese el numero de departamento: ")

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
                        torrep = ""
                        continue
                    else:
                        break

                nombreyapellido = input("Ingrese el nombre y apellido del propietario: ")
                habitantes = input("Ingrese la cantidad de habitantes: ")
                dia = input("Ingrese el dia de compra del departamento: ")
                mes = input("Ingrese el mes de compra del departamento: ")
                anio = input("Ingrese el año de compra del departamento: ")
                fechac = f"{dia}/{mes}/{anio}"
                fechav = "00/00/0000"  
                gym = input("¿El propietario tiene acceso al gimnasio? (S/N): ").lower()
                sum = input("¿El propietario tiene acceso al SUM? (S/N): ").lower()
                if sum == "s":
                    dsum = input("Ingrese la cantidad de dias de uso del SUM: ")
                else:
                    dsum = "0"
                op= input("Confirmar datos? (S/N): ").lower()
                if op == "s":
                    torresp.append(torrep)
                    pisosp.append(pisop)
                    dptosp.append(ndptop)
                    nombresyapellidos.append(nombreyapellido)
                    habitantess.append(habitantes)
                    fechasc.append(fechac)
                    fechasv.append(fechav)
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
                    pisop = input("Ingrese el piso: ")
                    ndptop = input("Ingrese el numero de departamento: ")
                    existe = False
                    for h in range(len(torresp)):
                        if torresp[h] == torrep and pisosp[h] == pisop and dptosp[h] == ndptop:
                            existe = True
                            break
                    if existe == False:
                        print("El propietario no existe.")
                        torrep = ""
                        continue
                    else:
                        break
                op = input("Esta seguro que desea eliminar el propietario? (S/N): ").lower()
                if op == "s":
                    dia = input("Ingrese el dia de la venta del departamento: ")
                    mes = input("Ingrese el mes de la venta del departamento: ")
                    anio = input("Ingrese el año de la venta del departamento: ")
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
                    pisop = input("Ingrese el piso: ")
                    ndptop = input("Ingrese el numero de departamento: ")

                    existe = False
                    for h in range(len(torresp)):
                        if torresp[h] == torrep and pisosp[h] == pisop and dptosp[h] == ndptop:
                            existe = True
                            break
                    if existe == False:
                        print("El propietario no existe.")
                        torrep = ""
                        continue
                    else:
                        break
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
                    habitantes = input("Ingrese la nueva cantidad de habitantes: ")
                elif op == "2":
                    dt = "2"
                    dia = input("Ingrese el nuevo dia de compra del departamento: ")
                    mes = input("Ingrese el nuevo mes de compra del departamento: ")
                    anio = input("Ingrese el nuevo año de compra del departamento: ")
                    fechac = f"{dia}/{mes}/{anio}"
                elif op == "3":
                    dt = "3"
                    gym = input("¿El propietario tiene acceso al gimnasio? (S/N): ").lower()
                elif op == "4":
                    dt = "4"
                    sum = input("¿El propietario tiene acceso al SUM? (S/N): ").lower()
                elif op == "5":
                    dt = "5"
                    dsum = input("Ingrese la nueva cantidad de dias de uso del SUM: ")
                else:
                    print("Opcion invalida.")
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
                    for h in range(len(nombresyapellidos)):
                        if nombresyapellidos[h] == nombreyapellido:
                            print(f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre y Apellido: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Fecha de compra: {fechasc[h]}, Fecha de venta: {fechasv[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Dias de uso del Sum: {dsums[h]}")
                elif op == "2":
                    while torrep != "A" and torrep != "B" and torrep != "C":
                        torrep= input("Ingrese la torre (A/B/C): ").upper()
                    pisop = input("Ingrese el piso: ")
                    for h in range(len(torresp)):
                        if torresp[h] == torrep and pisosp[h] == pisop:
                            print(f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre y Apellido: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Fecha de compra: {fechasc[h]}, Fecha de venta: {fechasv[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Dias de uso del Sum: {dsums[h]}")
                elif op == "3":
                    while torrep != "A" and torrep != "B" and torrep != "C":
                        torrep= input("Ingrese la torre (A/B/C): ").upper()
                    pisop = input("Ingrese el piso: ")
                    ndptop = input("Ingrese el numero de departamento: ")
                    for h in range(len(torresp)):
                        if torresp[h] == torrep and pisosp[h] == pisop and dptosp[h] == ndptop:
                            print(f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre y Apellido: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Fecha de compra: {fechasc[h]}, Fecha de venta: {fechasv[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Dias de uso del Sum: {dsums[h]}")
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
                    pisop = input("Ingrese el piso: ")
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
                    pisop = input("Ingrese el piso: ")
                    ndptop = input("Ingrese el numero de departamento: ")
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
            print(" 1 - Cargar cochera")
            print(" 2 - Modificar cochera")
            print(" 3 - Consultar cochera")
            print(" 4 - Listar cocheras")
            print(" 0 - Salir")
            print("------------------------------------------------------------")
            op = input("Ingrese una opción: ")
            if op == "1":
                print("Cargar cochera")
                while True:
                    while torrec != "A" and torrec != "B" and torrec != "C":
                        torrec = input("Ingrese la torre (A/B/C): ").upper()
                    pisoc = input("Ingrese el piso: ")
                    dptoc = input("Ingrese el numero de departamento: ")
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
                mtcubiertosc = input("Ingrese los metros cubiertos de la cochera: ")
                libre = input("¿La cochera esta libre? (S/N): ").lower()
                op = input("Confirmar datos? (S/N): ").lower()
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
                    pisoc = input("Ingrese el piso: ")
                    dptoc = input("Ingrese el numero de departamento: ")

                    existe = False
                    for h in range(len(torresc)):
                        if torresc[h] == torrec and pisosc[h] == pisoc and dptosc[h] == dptoc:
                            existe = True
                            break
                    if existe == False:
                        print("La cochera no existe.")
                        torrec = ""
                        continue
                    else:
                        break
                print("--------------------------------------------------------")
                print("                Ingrese qué quiere modificar            ")
                print("--------------------------------------------------------")
                print(" 1 - Metros cubiertos")
                print(" 2 - Cochera libre (S/N)")
                print("--------------------------------------------------------")
                op = input("Ingrese una opción: ")
                if op == "1":
                    dt = "1"
                    mtcubiertosc = input("Ingrese los nuevos metros cubiertos de la cochera: ")
                elif op == "2":
                    dt = "2"
                    libre = input("¿La cochera esta libre? (S/N): ").lower()
                else:
                    print("Opcion invalida.")
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
                    pisoc = input("Ingrese el piso: ")
                    for h in range(len(torresc)):
                        if torresc[h] == torrec and pisosc[h] == pisoc:
                            print(f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Departamento: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}")
                elif op == "3":
                    while torrec != "A" and torrec != "B" and torrec != "C":
                        torrec = input("Ingrese la torre: ").upper()
                    pisoc = input("Ingrese el piso: ")
                    dptoc = input("Ingrese el numero de departamento: ")
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
                    pisoc = input("Ingrese el piso: ")
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
                    pisoc = input("Ingrese el piso: ")
                    dptoc = input("Ingrese el numero de departamento: ")
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
    elif op == "4":
        print("Opcion no implementada.")
    elif op == "0":
        print("Saliendo del programa.")
        break
