import os
import sqlite3
from contextlib import closing


DB_FILENAME = "CRUDMod.db"


def pedir_numero(mensaje: str) -> int:
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        print("❌ Por favor, ingrese solo números enteros.")


def pedir_opcion_sn(mensaje: str) -> str:
    while True:
        opcion = input(mensaje).strip().lower()
        if opcion in ("s", "n"):
            return opcion
        print("❌ Responda con S o N.")


def get_connection():
    needs_seed = not os.path.exists(DB_FILENAME)
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    create_tables(conn)
    if needs_seed:
        seed_data(conn)
    return conn


def create_tables(conn: sqlite3.Connection) -> None:
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS departamentos (
                torre TEXT NOT NULL CHECK(torre IN ('A','B','C')),
                piso INTEGER NOT NULL,
                numero INTEGER NOT NULL,
                habitaciones INTEGER NOT NULL,
                metros_cubiertos INTEGER NOT NULL,
                luz INTEGER NOT NULL,
                agua INTEGER NOT NULL,
                gas INTEGER NOT NULL,
                PRIMARY KEY (torre, piso, numero)
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS propietarios (
                torre TEXT NOT NULL CHECK(torre IN ('A','B','C')),
                piso INTEGER NOT NULL,
                numero INTEGER NOT NULL,
                nombre TEXT NOT NULL,
                habitantes INTEGER NOT NULL,
                fecha_compra TEXT NOT NULL,
                fecha_venta TEXT NOT NULL,
                cochera TEXT NOT NULL CHECK(cochera IN ('s','n')),
                gym TEXT NOT NULL CHECK(gym IN ('s','n')),
                sum TEXT NOT NULL CHECK(sum IN ('s','n')),
                dias_sum INTEGER NOT NULL,
                PRIMARY KEY (torre, piso, numero),
                FOREIGN KEY (torre, piso, numero) REFERENCES departamentos(torre, piso, numero)
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS cocheras (
                torre TEXT NOT NULL CHECK(torre IN ('A','B','C')),
                piso INTEGER NOT NULL,
                numero INTEGER NOT NULL,
                metros_cubiertos INTEGER NOT NULL,
                libre TEXT NOT NULL CHECK(libre IN ('s','n')),
                PRIMARY KEY (torre, piso, numero)
            )
            """
        )


def seed_data(conn: sqlite3.Connection) -> None:
    departamentos = [
        ("B", 2, 1, 4, 20, 15, 11, 18),
        ("C", 1, 2, 7, 20, 25, 22, 26),
        ("B", 7, 3, 4, 30, 35, 33, 34),
        ("A", 6, 4, 8, 100, 45, 44, 47),
        ("A", 5, 5, 9, 50, 55, 55, 51),
    ]
    propietarios = [
        ("B", 2, 1, "Juan Perez", 4, "01/01/2020", "00/00/0000", "s", "s", "s", 0),
        ("C", 1, 2, "Maria Lopez", 7, "02/02/2021", "00/00/0000", "n", "n", "n", 0),
        ("B", 7, 3, "Carlos Gomez", 4, "03/03/2022", "00/00/0000", "s", "s", "s", 0),
        ("A", 6, 4, "Ana Fernandez", 8, "04/04/2023", "00/00/0000", "n", "n", "n", 0),
        ("A", 5, 5, "Luis Martinez", 9, "05/05/2024", "00/00/0000", "s", "s", "s", 0),
    ]
    cocheras = [
        ("A", 1, 1, 20, "s"),
        ("B", 2, 2, 30, "n"),
        ("C", 3, 3, 40, "s"),
        ("A", 4, 4, 50, "n"),
        ("B", 5, 5, 60, "s"),
    ]
    with conn:
        conn.executemany(
            """
            INSERT OR IGNORE INTO departamentos
            (torre, piso, numero, habitaciones, metros_cubiertos, luz, agua, gas)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            departamentos,
        )
        conn.executemany(
            """
            INSERT OR IGNORE INTO propietarios
            (torre, piso, numero, nombre, habitantes, fecha_compra, fecha_venta, cochera, gym, sum, dias_sum)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            propietarios,
        )
        conn.executemany(
            """
            INSERT OR IGNORE INTO cocheras
            (torre, piso, numero, metros_cubiertos, libre)
            VALUES (?, ?, ?, ?, ?)
            """,
            cocheras,
        )


def obtener_departamento(conn, torre, piso, numero):
    cur = conn.execute(
        "SELECT * FROM departamentos WHERE torre = ? AND piso = ? AND numero = ?",
        (torre, piso, numero),
    )
    return cur.fetchone()


def obtener_propietario(conn, torre, piso, numero):
    cur = conn.execute(
        "SELECT * FROM propietarios WHERE torre = ? AND piso = ? AND numero = ?",
        (torre, piso, numero),
    )
    return cur.fetchone()


def obtener_cochera(conn, torre, piso, numero):
    cur = conn.execute(
        "SELECT * FROM cocheras WHERE torre = ? AND piso = ? AND numero = ?",
        (torre, piso, numero),
    )
    return cur.fetchone()


def solicitar_torre(mensaje="Ingrese la torre (A/B/C): ") -> str:
    while True:
        torre = input(mensaje).strip().upper()
        if torre in ("A", "B", "C"):
            return torre
        print("❌ Torre inválida. Debe ser A, B o C.")


def guardar_en_listado(texto: str) -> None:
    with open("listado.txt", "a", encoding="utf-8") as archivo:
        archivo.write(texto + "\n")


def cargar_departamento(conn):
    print("Cargar departamento")
    while True:
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        numero = pedir_numero("Ingrese el número de departamento: ")
        if obtener_departamento(conn, torre, piso, numero):
            print("❌ El departamento ya existe.")
            if pedir_opcion_sn("¿Desea intentar con otro departamento? (S/N): ") == "s":
                continue
            return
        break

    habitaciones = pedir_numero("Ingrese la cantidad de habitaciones: ")
    metros = pedir_numero("Ingrese los metros cubiertos: ")
    luz = pedir_numero("Ingrese el consumo de luz: ")
    agua = pedir_numero("Ingrese el consumo de agua: ")
    gas = pedir_numero("Ingrese el consumo de gas: ")

    if pedir_opcion_sn("Confirmar datos? (S/N): ") == "s":
        with conn:
            conn.execute(
                """
                INSERT INTO departamentos
                (torre, piso, numero, habitaciones, metros_cubiertos, luz, agua, gas)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (torre, piso, numero, habitaciones, metros, luz, agua, gas),
            )
        print("✅ Departamento cargado exitosamente.")
    else:
        print("ℹ️ Carga de departamento cancelada.")


def eliminar_departamento(_conn):
    print("ℹ️ No se puede eliminar un departamento.")


def modificar_departamento(conn):
    print("Modificar departamento")
    torre = solicitar_torre()
    piso = pedir_numero("Ingrese el piso: ")
    numero = pedir_numero("Ingrese el número de departamento: ")
    registro = obtener_departamento(conn, torre, piso, numero)
    if not registro:
        print("❌ El departamento no existe.")
        return

    print("---------------------------------------------------------------------")
    print("               Ingrese qué quiere modificar                         ")
    print("---------------------------------------------------------------------")
    print(" 1 - Habitaciones")
    print(" 2 - Metros cubiertos")
    print(" 3 - Consumo de luz")
    print(" 4 - Consumo de agua")
    print(" 5 - Consumo de gas")
    print("---------------------------------------------------------------------")
    opcion = input("Ingrese una opción: ").strip()

    campos = {
        "1": ("habitaciones", "Ingrese la nueva cantidad de habitaciones: "),
        "2": ("metros_cubiertos", "Ingrese los nuevos metros cubiertos: "),
        "3": ("luz", "Ingrese el nuevo consumo de luz: "),
        "4": ("agua", "Ingrese el nuevo consumo de agua: "),
        "5": ("gas", "Ingrese el nuevo consumo de gas: "),
    }

    if opcion not in campos:
        print("❌ Opción inválida.")
        return

    campo, mensaje = campos[opcion]
    nuevo_valor = pedir_numero(mensaje)
    if pedir_opcion_sn("Confirmar modificación? (S/N): ") == "s":
        with conn:
            conn.execute(
                f"""
                UPDATE departamentos
                SET {campo} = ?
                WHERE torre = ? AND piso = ? AND numero = ?
                """,
                (nuevo_valor, torre, piso, numero),
            )
        print("✅ Modificación de departamento confirmada.")
    else:
        print("ℹ️ Modificación de departamento cancelada.")


def consultar_departamento(conn):
    print("---------------------------------------------------------------------")
    print("                  Consultar departamento                             ")
    print("         Elija opción para filtrar la consulta                      ")
    print("---------------------------------------------------------------------")
    print(" 1 - Consultar por torre")
    print(" 2 - Consultar por torre y piso")
    print(" 3 - Consultar por torre, piso y departamento")
    print("---------------------------------------------------------------------")
    opcion = input("Ingrese una opción: ").strip()

    if opcion == "1":
        torre = solicitar_torre()
        registros = conn.execute(
            """
            SELECT * FROM departamentos
            WHERE torre = ?
            ORDER BY piso, numero
            """,
            (torre,),
        ).fetchall()
    elif opcion == "2":
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        registros = conn.execute(
            """
            SELECT * FROM departamentos
            WHERE torre = ? AND piso = ?
            ORDER BY numero
            """,
            (torre, piso),
        ).fetchall()
    elif opcion == "3":
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        numero = pedir_numero("Ingrese el número de departamento: ")
        registros = [
            obtener_departamento(conn, torre, piso, numero)
        ]
    else:
        print("❌ Opción inválida.")
        return

    encontrados = [r for r in registros if r]
    if not encontrados:
        print("ℹ️ No se encontraron registros.")
        return

    for registro in encontrados:
        print(
            f"Torre: {registro['torre']}, Piso: {registro['piso']}, Departamento: {registro['numero']}, "
            f"Habitaciones: {registro['habitaciones']}, Metros cubiertos: {registro['metros_cubiertos']}, "
            f"Luz: {registro['luz']}, Agua: {registro['agua']}, Gas: {registro['gas']}"
        )


def listar_departamentos(conn):
    print("---------------------------------------------------------------------")
    print("                   Listar departamentos                              ")
    print("         Elija opción para filtrar la consulta                      ")
    print("---------------------------------------------------------------------")
    print(" 1 - Consultar por torre")
    print(" 2 - Consultar por torre y piso")
    print(" 3 - Consultar por torre, piso y departamento")
    print("---------------------------------------------------------------------")
    opcion = input("Ingrese una opción: ").strip()

    if opcion == "1":
        torre = solicitar_torre()
        registros = conn.execute(
            """
            SELECT * FROM departamentos
            WHERE torre = ?
            ORDER BY piso, numero
            """,
            (torre,),
        ).fetchall()
    elif opcion == "2":
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        registros = conn.execute(
            """
            SELECT * FROM departamentos
            WHERE torre = ? AND piso = ?
            ORDER BY numero
            """,
            (torre, piso),
        ).fetchall()
    elif opcion == "3":
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        numero = pedir_numero("Ingrese el número de departamento: ")
        registro = obtener_departamento(conn, torre, piso, numero)
        registros = [registro] if registro else []
    else:
        print("❌ Opción inválida.")
        return

    if not registros:
        print("ℹ️ No se encontraron registros.")
        return

    for registro in registros:
        frase = (
            f"Torre: {registro['torre']}, Piso: {registro['piso']}, Departamento: {registro['numero']}, "
            f"Habitaciones: {registro['habitaciones']}, Metros cubiertos: {registro['metros_cubiertos']}, "
            f"Luz: {registro['luz']}, Agua: {registro['agua']}, Gas: {registro['gas']}"
        )
        print(frase)
        guardar_en_listado(frase)
    print("ℹ️ La información se ha guardado en listado.txt.")


def menu_departamentos(conn):
    while True:
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
        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            cargar_departamento(conn)
        elif opcion == "2":
            eliminar_departamento(conn)
        elif opcion == "3":
            modificar_departamento(conn)
        elif opcion == "4":
            consultar_departamento(conn)
        elif opcion == "5":
            listar_departamentos(conn)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")


def cargar_propietario(conn):
    print("Cargar propietario")
    while True:
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        numero = pedir_numero("Ingrese el número de departamento: ")
        if not obtener_departamento(conn, torre, piso, numero):
            print("❌ El departamento no existe.")
            if pedir_opcion_sn("¿Desea volver a intentar? (S/N): ") == "s":
                continue
            return
        if obtener_propietario(conn, torre, piso, numero):
            print("❌ El propietario ya está registrado para ese departamento.")
            return
        break

    nombre = input("Ingrese el nombre y apellido del propietario: ")
    habitantes = pedir_numero("Ingrese la cantidad de habitantes: ")
    dia = pedir_numero("Ingrese el día de compra del departamento: ")
    mes = pedir_numero("Ingrese el mes de compra del departamento: ")
    anio = pedir_numero("Ingrese el año de compra del departamento: ")
    fecha_compra = f"{dia:02d}/{mes:02d}/{anio}"
    fecha_venta = "00/00/0000"

    cochera = ""
    while cochera not in ("s", "n"):
        cochera = input("¿El propietario tiene cochera? (S/N): ").strip().lower()
    gym = ""
    while gym not in ("s", "n"):
        gym = input("¿El propietario tiene acceso al gimnasio? (S/N): ").strip().lower()
    sum_acceso = ""
    while sum_acceso not in ("s", "n"):
        sum_acceso = input("¿El propietario tiene acceso al SUM? (S/N): ").strip().lower()
    if sum_acceso == "s":
        dias_sum = pedir_numero("Ingrese la cantidad de días de uso del SUM: ")
    else:
        dias_sum = 0

    if pedir_opcion_sn("Confirmar datos? (S/N): ") == "s":
        with conn:
            conn.execute(
                """
                INSERT INTO propietarios
                (torre, piso, numero, nombre, habitantes, fecha_compra, fecha_venta,
                 cochera, gym, sum, dias_sum)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    torre,
                    piso,
                    numero,
                    nombre,
                    habitantes,
                    fecha_compra,
                    fecha_venta,
                    cochera,
                    gym,
                    sum_acceso,
                    dias_sum,
                ),
            )
        print("✅ Propietario cargado exitosamente.")
    else:
        print("ℹ️ Carga de propietario cancelada.")


def eliminar_propietario(conn):
    print("Eliminar propietario")
    torre = solicitar_torre()
    piso = pedir_numero("Ingrese el piso: ")
    numero = pedir_numero("Ingrese el número de departamento: ")
    registro = obtener_propietario(conn, torre, piso, numero)
    if not registro:
        print("❌ El propietario no existe.")
        return

    if pedir_opcion_sn("¿Está seguro que desea eliminar el propietario? (S/N): ") == "s":
        dia = pedir_numero("Ingrese el día de la venta del departamento: ")
        mes = pedir_numero("Ingrese el mes de la venta del departamento: ")
        anio = pedir_numero("Ingrese el año de la venta del departamento: ")
        fecha_venta = f"{dia:02d}/{mes:02d}/{anio}"
        with conn:
            conn.execute(
                """
                UPDATE propietarios
                SET fecha_venta = ?
                WHERE torre = ? AND piso = ? AND numero = ?
                """,
                (fecha_venta, torre, piso, numero),
            )
        print("✅ Propietario eliminado exitosamente.")
    else:
        print("ℹ️ Eliminación de propietario cancelada.")


def modificar_propietario(conn):
    print("Modificar propietario")
    torre = solicitar_torre()
    piso = pedir_numero("Ingrese el piso: ")
    numero = pedir_numero("Ingrese el número de departamento: ")
    registro = obtener_propietario(conn, torre, piso, numero)
    if not registro:
        print("❌ El propietario no existe.")
        return

    print("-------------------------------------------------------------------")
    print("                 Ingrese qué quiere modificar                      ")
    print("-------------------------------------------------------------------")
    print(" 1 - Habitantes")
    print(" 2 - Fecha de compra")
    print(" 3 - Gym")
    print(" 4 - Sum")
    print(" 5 - Días de uso del Sum")
    print("-------------------------------------------------------------------")
    opcion = input("Ingrese una opción: ").strip()

    if opcion == "1":
        nuevo_valor = pedir_numero("Ingrese la nueva cantidad de habitantes: ")
        campo = "habitantes"
    elif opcion == "2":
        dia = pedir_numero("Ingrese el nuevo día de compra: ")
        mes = pedir_numero("Ingrese el nuevo mes de compra: ")
        anio = pedir_numero("Ingrese el nuevo año de compra: ")
        nuevo_valor = f"{dia:02d}/{mes:02d}/{anio}"
        campo = "fecha_compra"
    elif opcion == "3":
        nuevo_valor = pedir_opcion_sn("¿El propietario tiene acceso al gimnasio? (S/N): ")
        campo = "gym"
    elif opcion == "4":
        nuevo_valor = pedir_opcion_sn("¿El propietario tiene acceso al SUM? (S/N): ")
        campo = "sum"
        if nuevo_valor == "n":
            with conn:
                conn.execute(
                    """
                    UPDATE propietarios
                    SET sum = 'n', dias_sum = 0
                    WHERE torre = ? AND piso = ? AND numero = ?
                    """,
                    (torre, piso, numero),
                )
            print("✅ Modificación de propietario confirmada.")
            return
    elif opcion == "5":
        nuevo_valor = pedir_numero("Ingrese la nueva cantidad de días de uso del SUM: ")
        campo = "dias_sum"
    else:
        print("❌ Opción inválida.")
        return

    if pedir_opcion_sn("Confirmar modificación? (S/N): ") == "s":
        with conn:
            conn.execute(
                f"""
                UPDATE propietarios
                SET {campo} = ?
                WHERE torre = ? AND piso = ? AND numero = ?
                """,
                (nuevo_valor, torre, piso, numero),
            )
        print("✅ Modificación de propietario confirmada.")
    else:
        print("ℹ️ Modificación de propietario cancelada.")


def consultar_propietario(conn):
    print("---------------------------------------------------------------------")
    print("                    Consultar propietario                            ")
    print("                Elija opción para filtrar la consulta                ")
    print("---------------------------------------------------------------------")
    print(" 1 - Consultar por nombre y apellido")
    print(" 2 - Consultar por torre y piso")
    print(" 3 - Consultar por torre, piso y departamento")
    print("---------------------------------------------------------------------")
    opcion = input("Ingrese una opción: ").strip()

    if opcion == "1":
        nombre = input("Ingrese el nombre y apellido del propietario: ")
        registros = conn.execute(
            """
            SELECT * FROM propietarios
            WHERE nombre = ?
            ORDER BY torre, piso, numero
            """,
            (nombre,),
        ).fetchall()
    elif opcion == "2":
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        registros = conn.execute(
            """
            SELECT * FROM propietarios
            WHERE torre = ? AND piso = ?
            ORDER BY numero
            """,
            (torre, piso),
        ).fetchall()
    elif opcion == "3":
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        numero = pedir_numero("Ingrese el número de departamento: ")
        registros = [
            obtener_propietario(conn, torre, piso, numero)
        ]
    else:
        print("❌ Opción inválida.")
        return

    encontrados = [r for r in registros if r]
    if not encontrados:
        print("ℹ️ No se encontraron registros.")
        return

    for registro in encontrados:
        print(
            f"Torre: {registro['torre']}, Piso: {registro['piso']}, Departamento: {registro['numero']}, "
            f"Nombre y Apellido: {registro['nombre']}, Habitantes: {registro['habitantes']}, "
            f"Fecha de compra: {registro['fecha_compra']}, Fecha de venta: {registro['fecha_venta']}, "
            f"Gym: {registro['gym']}, Sum: {registro['sum']}, Días de uso del Sum: {registro['dias_sum']}"
        )


def listar_propietarios(conn):
    print("---------------------------------------------------------------------")
    print("                    Listar propietarios                              ")
    print("                Elija opción para filtrar la consulta                ")
    print("---------------------------------------------------------------------")
    print(" 1 - Consultar por nombre y apellido")
    print(" 2 - Consultar por torre y piso")
    print(" 3 - Consultar por torre, piso y departamento")
    print("---------------------------------------------------------------------")
    opcion = input("Ingrese una opción: ").strip()

    if opcion == "1":
        nombre = input("Ingrese el nombre y apellido del propietario: ")
        registros = conn.execute(
            """
            SELECT * FROM propietarios
            WHERE nombre = ?
            ORDER BY torre, piso, numero
            """,
            (nombre,),
        ).fetchall()
    elif opcion == "2":
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        registros = conn.execute(
            """
            SELECT * FROM propietarios
            WHERE torre = ? AND piso = ?
            ORDER BY numero
            """,
            (torre, piso),
        ).fetchall()
    elif opcion == "3":
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        numero = pedir_numero("Ingrese el número de departamento: ")
        registro = obtener_propietario(conn, torre, piso, numero)
        registros = [registro] if registro else []
    else:
        print("❌ Opción inválida.")
        return

    if not registros:
        print("ℹ️ No se encontraron registros.")
        return

    for registro in registros:
        frase = (
            f"Torre: {registro['torre']}, Piso: {registro['piso']}, Departamento: {registro['numero']}, "
            f"Nombre y Apellido: {registro['nombre']}, Habitantes: {registro['habitantes']}, "
            f"Fecha de compra: {registro['fecha_compra']}, Fecha de venta: {registro['fecha_venta']}, "
            f"Gym: {registro['gym']}, Sum: {registro['sum']}, Días de uso del Sum: {registro['dias_sum']}"
        )
        print(frase)
        guardar_en_listado(frase)
    print("ℹ️ La información se ha guardado en listado.txt.")


def menu_propietarios(conn):
    while True:
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
        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            cargar_propietario(conn)
        elif opcion == "2":
            eliminar_propietario(conn)
        elif opcion == "3":
            modificar_propietario(conn)
        elif opcion == "4":
            consultar_propietario(conn)
        elif opcion == "5":
            listar_propietarios(conn)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")


def cargar_cochera(conn):
    print("Cargar cochera")
    while True:
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        numero = pedir_numero("Ingrese el número de departamento: ")
        if obtener_cochera(conn, torre, piso, numero):
            print("❌ La cochera ya existe.")
            if pedir_opcion_sn("¿Desea intentar con otra cochera? (S/N): ") == "s":
                continue
            return
        break

    metros = pedir_numero("Ingrese los metros cubiertos de la cochera: ")
    libre = pedir_opcion_sn("¿La cochera está libre? (S/N): ")

    if pedir_opcion_sn("Confirmar datos? (S/N): ") == "s":
        with conn:
            conn.execute(
                """
                INSERT INTO cocheras (torre, piso, numero, metros_cubiertos, libre)
                VALUES (?, ?, ?, ?, ?)
                """,
                (torre, piso, numero, metros, libre),
            )
        print("✅ Cochera cargada exitosamente.")
    else:
        print("ℹ️ Carga de cochera cancelada.")


def modificar_cochera(conn):
    print("Modificar cochera")
    torre = solicitar_torre()
    piso = pedir_numero("Ingrese el piso: ")
    numero = pedir_numero("Ingrese el número de departamento: ")
    registro = obtener_cochera(conn, torre, piso, numero)
    if not registro:
        print("❌ La cochera no existe.")
        return

    print("--------------------------------------------------------")
    print("                Ingrese qué quiere modificar            ")
    print("--------------------------------------------------------")
    print(" 1 - Metros cubiertos")
    print(" 2 - Cochera libre (S/N)")
    print("--------------------------------------------------------")
    opcion = input("Ingrese una opción: ").strip()

    if opcion == "1":
        nuevo_valor = pedir_numero("Ingrese los nuevos metros cubiertos de la cochera: ")
        campo = "metros_cubiertos"
    elif opcion == "2":
        nuevo_valor = pedir_opcion_sn("¿La cochera está libre? (S/N): ")
        campo = "libre"
    else:
        print("❌ Opción inválida.")
        return

    if pedir_opcion_sn("Confirmar modificación? (S/N): ") == "s":
        with conn:
            conn.execute(
                f"""
                UPDATE cocheras
                SET {campo} = ?
                WHERE torre = ? AND piso = ? AND numero = ?
                """,
                (nuevo_valor, torre, piso, numero),
            )
        print("✅ Modificación de cochera confirmada.")
    else:
        print("ℹ️ Modificación de cochera cancelada.")


def consultar_cochera(conn):
    print("---------------------------------------------------------------------")
    print("                    Consultar cochera                               ")
    print("                Elija opción para filtrar la consulta               ")
    print("---------------------------------------------------------------------")
    print(" 1 - Consultar por torre")
    print(" 2 - Consultar por torre y piso")
    print(" 3 - Consultar por torre, piso y departamento")
    print("---------------------------------------------------------------------")
    opcion = input("Ingrese una opción: ").strip()

    if opcion == "1":
        torre = solicitar_torre()
        registros = conn.execute(
            """
            SELECT * FROM cocheras
            WHERE torre = ?
            ORDER BY piso, numero
            """,
            (torre,),
        ).fetchall()
    elif opcion == "2":
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        registros = conn.execute(
            """
            SELECT * FROM cocheras
            WHERE torre = ? AND piso = ?
            ORDER BY numero
            """,
            (torre, piso),
        ).fetchall()
    elif opcion == "3":
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        numero = pedir_numero("Ingrese el número de departamento: ")
        registros = [
            obtener_cochera(conn, torre, piso, numero)
        ]
    else:
        print("❌ Opción inválida.")
        return

    encontrados = [r for r in registros if r]
    if not encontrados:
        print("ℹ️ No se encontraron registros.")
        return

    for registro in encontrados:
        print(
            f"Torre: {registro['torre']}, Piso: {registro['piso']}, Departamento: {registro['numero']}, "
            f"Metros cubiertos: {registro['metros_cubiertos']}, Libre: {registro['libre']}"
        )


def listar_cocheras(conn):
    print("---------------------------------------------------------------------")
    print("                      Listar cocheras                               ")
    print("                 Elija opción para filtrar la consulta              ")
    print("---------------------------------------------------------------------")
    print(" 1 - Consultar por torre")
    print(" 2 - Consultar por torre y piso")
    print(" 3 - Consultar por torre, piso y departamento")
    print("---------------------------------------------------------------------")
    opcion = input("Ingrese una opción: ").strip()

    if opcion == "1":
        torre = solicitar_torre()
        registros = conn.execute(
            """
            SELECT * FROM cocheras
            WHERE torre = ?
            ORDER BY piso, numero
            """,
            (torre,),
        ).fetchall()
    elif opcion == "2":
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        registros = conn.execute(
            """
            SELECT * FROM cocheras
            WHERE torre = ? AND piso = ?
            ORDER BY numero
            """,
            (torre, piso),
        ).fetchall()
    elif opcion == "3":
        torre = solicitar_torre()
        piso = pedir_numero("Ingrese el piso: ")
        numero = pedir_numero("Ingrese el número de departamento: ")
        registro = obtener_cochera(conn, torre, piso, numero)
        registros = [registro] if registro else []
    else:
        print("❌ Opción inválida.")
        return

    if not registros:
        print("ℹ️ No se encontraron registros.")
        return

    for registro in registros:
        frase = (
            f"Torre: {registro['torre']}, Piso: {registro['piso']}, Departamento: {registro['numero']}, "
            f"Metros cubiertos: {registro['metros_cubiertos']}, Libre: {registro['libre']}"
        )
        print(frase)
        guardar_en_listado(frase)
    print("ℹ️ La información se ha guardado en listado.txt.")


def menu_cocheras(conn):
    while True:
        print("------------------------------------------------------------")
        print("                     Menú de cocheras                       ")
        print("------------------------------------------------------------")
        print(" 1 - ➕ Cargar cochera")
        print(" 2 - ✏️ Modificar cochera")
        print(" 3 - 🔍 Consultar cochera")
        print(" 4 - 📋 Listar cocheras")
        print(" 0 - ⛔ Volver")
        print("------------------------------------------------------------")
        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            cargar_cochera(conn)
        elif opcion == "2":
            modificar_cochera(conn)
        elif opcion == "3":
            consultar_cochera(conn)
        elif opcion == "4":
            listar_cocheras(conn)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")


def calcular_liquidacion(conn):
    departamentos = conn.execute("SELECT * FROM departamentos").fetchall()
    propietarios = conn.execute("SELECT * FROM propietarios").fetchall()
    cocheras = conn.execute("SELECT * FROM cocheras").fetchall()

    if not departamentos:
        print("ℹ️ No hay departamentos para liquidar.")
        return

    torres = [d["torre"] for d in departamentos]
    cant_depas_por_torre = {torre: torres.count(torre) for torre in ("A", "B", "C")}

    seguridad_torre = {
        torre: (150000 / cant if cant else 0) for torre, cant in cant_depas_por_torre.items()
    }
    seguridad_cochera = {torre: valor / 2 for torre, valor in seguridad_torre.items()}

    paga_doble = {"A": 0, "B": 0, "C": 0}
    for depa in departamentos:
        if depa["metros_cubiertos"] >= 100:
            torre = depa["torre"]
            paga_doble[torre] += seguridad_torre[torre] * 2

    luz_consumida = [d["luz"] * 15000 for d in departamentos]
    agua_consumida = [d["agua"] * 1000 for d in departamentos]
    gas_consumido = [d["gas"] * 5000 for d in departamentos]

    sum_total = sum(1 for propietario in propietarios if propietario["sum"] == "s") or 1
    sum_consumo = 80000 / sum_total
    dias_sum_consumo = [propietario["dias_sum"] * 40000 for propietario in propietarios]
    impuesto_departamentos = [d["metros_cubiertos"] * 400 for d in departamentos]
    impuesto_cocheras = [c["metros_cubiertos"] * 200 for c in cocheras]

    pagannormaldepa = []
    pagandobledepa = []
    for depa in departamentos:
        if depa["piso"] < 5:
            pagannormaldepa.append(depa)
        elif depa["piso"] > 5:
            pagandobledepa.append(depa)

    pagannormalcoch = []
    paga20coch = []
    propietario_index = {(p["torre"], p["piso"], p["numero"]): p for p in propietarios}
    for cochera in cocheras:
        key = (cochera["torre"], cochera["piso"], cochera["numero"])
        if key in propietario_index:
            paga20coch.append(cochera)
        else:
            pagannormalcoch.append(cochera)

    print("\n--- Liquidación por Torre ---")
    for torre in ("A", "B", "C"):
        print(f"Torre {torre} paga por seguridad:")
        factor = 2 if torre == "C" else 1
        print(f" - Por departamento: {int(seguridad_torre[torre] * factor)}")
        print(f" - Por cochera: {int(seguridad_cochera[torre] * factor)}")
        print(f"Departamentos mayores a 100m2 pagan el doble en Torre {torre}: {int(paga_doble[torre])}")
    print()

    print("--- Liquidación por Departamento ---")
    for idx, depa in enumerate(departamentos):
        print(f"Depto {depa['torre']} - {depa['piso']} - {depa['numero']}")
        agua = agua_consumida[idx]
        gas = gas_consumido[idx]
        luz = luz_consumida[idx]
        impuesto = impuesto_departamentos[idx]
        propietario = propietario_index.get((depa["torre"], depa["piso"], depa["numero"]))
        dias_sum = dias_sum_consumo[idx] if idx < len(dias_sum_consumo) else 0

        if propietario and propietario["sum"] == "s":
            uso_sum = sum_consumo
        else:
            uso_sum = 0

        if depa["torre"] == "C":
            uso_sum *= 2

        luz_comun = seguridad_torre[depa["torre"]] * (2 if depa["torre"] == "C" else 1)

        total = agua + gas + luz + impuesto + uso_sum + dias_sum + luz_comun

        print(f"  Agua: {int(agua)}")
        print(f"  Gas: {int(gas)}")
        print(f"  Luz: {int(luz)}")
        print(f"  Impuesto especial: {int(impuesto)}")
        print(f"  SUM: {int(uso_sum)}")
        print(f"  Días de SUM: {int(dias_sum)}")
        print(f"  Luz común: {int(luz_comun)}")
        print(f"  Total a pagar: {int(total)}\n")

    print("--- Liquidación por Cochera ---")
    for idx, cochera in enumerate(cocheras):
        print(f"Cochera {cochera['torre']} - {cochera['piso']} - {cochera['numero']}")
        impuesto = impuesto_cocheras[idx]
        seguridad = seguridad_cochera[cochera["torre"]] * (2 if cochera["torre"] == "C" else 1)
        total = impuesto + seguridad

        print(f"  Impuesto especial: {int(impuesto)}")
        print(f"  Seguridad: {int(seguridad)}")
        print(f"  Total a pagar: {int(total)}\n")

    total_departamentos = 0
    for idx, depa in enumerate(departamentos):
        agua = agua_consumida[idx]
        gas = gas_consumido[idx]
        luz = luz_consumida[idx]
        impuesto = impuesto_departamentos[idx]
        propietario = propietario_index.get((depa["torre"], depa["piso"], depa["numero"]))
        dias_sum = dias_sum_consumo[idx] if idx < len(dias_sum_consumo) else 0

        if propietario and propietario["sum"] == "s":
            uso_sum = sum_consumo
        else:
            uso_sum = 0

        if depa["torre"] == "C":
            uso_sum *= 2

        luz_comun = seguridad_torre[depa["torre"]] * (2 if depa["torre"] == "C" else 1)
        total_departamentos += agua + gas + luz + impuesto + uso_sum + dias_sum + luz_comun

    total_cocheras = 0
    for idx, cochera in enumerate(cocheras):
        impuesto = impuesto_cocheras[idx]
        seguridad = seguridad_cochera[cochera["torre"]] * (2 if cochera["torre"] == "C" else 1)
        total_cocheras += impuesto + seguridad

    print("--- Resumen Final ---")
    print(f"Total departamentos: {int(total_departamentos)}")
    print(f"Total cocheras: {int(total_cocheras)}")
    print(f"Total general: {int(total_departamentos + total_cocheras)}")


def menu_principal(conn):
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
        opcion = input("Ingrese una opción: ").strip()
        if opcion == "1":
            menu_departamentos(conn)
        elif opcion == "2":
            menu_propietarios(conn)
        elif opcion == "3":
            menu_cocheras(conn)
        elif opcion == "4":
            calcular_liquidacion(conn)
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")


def main():
    with closing(get_connection()) as conn:
        menu_principal(conn)


if __name__ == "__main__":
    main()


