import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Datos simulando CRUDMod.py
torres=["B","C","B","A","A"]
pisos=["2","1","7","6","5"]
dptos=["1","2","3","4","5"]
habitacioness=["4","7","4","8","9"]
mtcubiertoss=["20","20","30","100","50"]
luzz=["15","25","35","45","55"]
aguas=["11","22","33","44","55"]
gass=["18","26","34","47","51"]

# ================== DATOS PROPIETARIOS ==================
torresp = ["B","C","B","A","A"]
pisosp = ["2","1","7","6","5"]
dptosp = ["1","2","3","4","5"]
nombresyapellidos = ["Juan Perez","Maria Lopez","Carlos Gomez","Ana Fernandez","Luis Martinez"]
habitantess = ["4","7","4","8","9"]
fechasc = ["01/01/2020","02/02/2021","03/03/2022","04/04/2023","05/05/2024"]
fechasv = ["00/00/0000","00/00/0000","00/00/0000","00/00/0000","00/00/0000"]
cocheras_p = ["s","n","s","n","s"]
gyms = ["s","n","s","n","s"]
sums = ["s","n","s","n","s"]
dsums = ["0","0","0","0","0"]

# ================== DATOS COCHERAS ==================
torresc = ["A","B","C","A","B"]
pisosc = ["1","2","3","4","5"]
dptosc = ["1","2","3","4","5"]
mtcubiertossc = ["20","30","40","50","60"]
libres = ["s","n","s","n","s"]

# Crear ventana principal
root = tk.Tk()
root.title("Sistema de Consorcio")
root.geometry("600x800")
root.configure(bg="#1e3d59")

# Función para mostrar un frame y ocultar los demás
def mostrar_frame(frame):
    for f in (frame_principal, frame_departamentos, frame_propietarios, frame_cocheras):
        f.pack_forget()
    frame.pack(expand=True)

# ============ FRAME PRINCIPAL ===============
frame_principal = tk.Frame(root, bg="#1e3d59")

titulo = tk.Label(frame_principal, text="Menú Principal", font=("Arial", 20), bg="#1e3d59", fg="#7ec8e3")
titulo.pack(pady=30)

botones = [
    ("Departamentos", lambda: mostrar_frame(frame_departamentos)),
    ("Propietarios", lambda: mostrar_frame(frame_propietarios)),
    ("Cocheras", lambda: mostrar_frame(frame_cocheras)),
    ("Liquidación", lambda: liquidacion()),
    ("Salir", root.quit)
]

for texto, comando in botones:
    tk.Button(frame_principal, text=texto, command=comando, bg="#274472", fg="#7ec8e3",
              font=("Arial", 14), width=20, height=2).pack(pady=5)

# ============ FRAME DEPARTAMENTOS ===============
frame_departamentos = tk.Frame(root, bg="#1e3d59")
tk.Label(frame_departamentos, text="Menú Departamentos", font=("Arial", 18), bg="#1e3d59", fg="#7ec8e3").pack(pady=30)
tk.Button(frame_departamentos, text="Alta", command=lambda: mostrar_frame(frame_alta_dpto), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_departamentos, text="Baja", command=lambda: mostrar_frame(frame_baja_dpto), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_departamentos, text="Modificación", command=lambda: mostrar_frame(frame_mod_dpto), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_departamentos, text="Consulta", command=lambda: mostrar_frame(frame_consulta_dpto), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_departamentos, text="Listado", command=lambda: mostrar_frame(frame_listado_dpto), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_departamentos, text="Volver", command=lambda: mostrar_frame(frame_principal), bg="#c94c4c", fg="white", font=("Arial", 12)).pack(pady=20)

# ============ ALTA DEPARTAMENTO ===============
frame_alta_dpto = tk.Frame(root, bg="#1e3d59")
tk.Label(frame_alta_dpto, text="Alta Departamento", font=("Arial", 18), bg="#1e3d59", fg="#7ec8e3").pack(pady=20)
alta_vars = {campo: tk.StringVar() for campo in ["Torre (A/B/C)", "Piso", "Número", "Habitaciones", "Metros Cubiertos", "Luz", "Agua", "Gas"]}
for campo, var in alta_vars.items():
    tk.Label(frame_alta_dpto, text=campo, bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
    tk.Entry(frame_alta_dpto, textvariable=var, font=("Arial", 12)).pack()
def alta_departamento():
    torre = alta_vars["Torre (A/B/C)"].get().upper()
    piso = alta_vars["Piso"].get()
    ndpto = alta_vars["Número"].get()
    if torre not in ("A", "B", "C"):
        messagebox.showerror("Error", "Torre inválida.")
        return
    if any(torres[i] == torre and pisos[i] == piso and dptos[i] == ndpto for i in range(len(torres))):
        messagebox.showerror("Error", "El departamento ya existe.")
        return
    torres.append(torre)
    pisos.append(piso)
    dptos.append(ndpto)
    habitacioness.append(alta_vars["Habitaciones"].get())
    mtcubiertoss.append(alta_vars["Metros Cubiertos"].get())
    luzz.append(alta_vars["Luz"].get())
    aguas.append(alta_vars["Agua"].get())
    gass.append(alta_vars["Gas"].get())
    messagebox.showinfo("Éxito", "Departamento cargado exitosamente.")
    mostrar_frame(frame_departamentos)
tk.Button(frame_alta_dpto, text="Guardar", command=alta_departamento, bg="#274472", fg="#7ec8e3", font=("Arial", 12)).pack(pady=10)
tk.Button(frame_alta_dpto, text="Volver", command=lambda: mostrar_frame(frame_departamentos), bg="#c94c4c", fg="white", font=("Arial", 12)).pack(pady=10)

# ============ BAJA DEPARTAMENTO ===============
frame_baja_dpto = tk.Frame(root, bg="#1e3d59")
tk.Label(frame_baja_dpto, text="Baja Departamento", font=("Arial", 18), bg="#1e3d59", fg="#7ec8e3").pack(pady=20)
baja_vars = {campo: tk.StringVar() for campo in ["Torre (A/B/C)", "Piso", "Número"]}
for campo, var in baja_vars.items():
    tk.Label(frame_baja_dpto, text=campo, bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
    tk.Entry(frame_baja_dpto, textvariable=var, font=("Arial", 12)).pack()
def baja_departamento():
    torre = baja_vars["Torre (A/B/C)"].get().upper()
    piso = baja_vars["Piso"].get()
    ndpto = baja_vars["Número"].get()
    for i in range(len(torres)):
        if torres[i] == torre and pisos[i] == piso and dptos[i] == ndpto:
            messagebox.showinfo("Info", "No se puede eliminar un departamento.")
            mostrar_frame(frame_departamentos)
            return
    messagebox.showerror("Error", "El departamento no existe.")
tk.Button(frame_baja_dpto, text="Eliminar", command=baja_departamento, bg="#c94c4c", fg="white", font=("Arial", 12)).pack(pady=10)
tk.Button(frame_baja_dpto, text="Volver", command=lambda: mostrar_frame(frame_departamentos), bg="#c94c4c", fg="white", font=("Arial", 12)).pack(pady=10)

# ============ MODIFICACION DEPARTAMENTO ===============
frame_mod_dpto = tk.Frame(root, bg="#1e3d59")
tk.Label(frame_mod_dpto, text="Modificar Departamento", font=("Arial", 18), bg="#1e3d59", fg="#7ec8e3").pack(pady=20)
mod_vars = {campo: tk.StringVar() for campo in ["Torre (A/B/C)", "Piso", "Número"]}
for campo, var in mod_vars.items():
    tk.Label(frame_mod_dpto, text=campo, bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
    tk.Entry(frame_mod_dpto, textvariable=var, font=("Arial", 12)).pack()
opcion_mod = tk.StringVar()
nuevo_valor = tk.StringVar()
def buscar_modificar():
    torre = mod_vars["Torre (A/B/C)"].get().upper()
    piso = mod_vars["Piso"].get()
    ndpto = mod_vars["Número"].get()
    for i in range(len(torres)):
        if torres[i] == torre and pisos[i] == piso and dptos[i] == ndpto:
            frame_mod_opciones.pack()
            frame_mod_dpto.mod_index = i
            return
    messagebox.showerror("Error", "El departamento no existe.")
frame_mod_opciones = tk.Frame(frame_mod_dpto, bg="#1e3d59")
tk.Label(frame_mod_opciones, text="¿Qué desea modificar?", bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
for campo in ["Habitaciones", "Metros Cubiertos", "Luz", "Agua", "Gas"]:
    tk.Radiobutton(frame_mod_opciones, text=campo, variable=opcion_mod, value=campo, bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack(anchor="w")
tk.Label(frame_mod_opciones, text="Nuevo valor:", bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
tk.Entry(frame_mod_opciones, textvariable=nuevo_valor, font=("Arial", 12)).pack()
def modificar_departamento():
    i = frame_mod_dpto.mod_index
    campo = opcion_mod.get()
    valor = nuevo_valor.get()
    if campo == "Habitaciones":
        habitacioness[i] = valor
    elif campo == "Metros Cubiertos":
        mtcubiertoss[i] = valor
    elif campo == "Luz":
        luzz[i] = valor
    elif campo == "Agua":
        aguas[i] = valor
    elif campo == "Gas":
        gass[i] = valor
    else:
        messagebox.showerror("Error", "Opción inválida.")
        return
    messagebox.showinfo("Éxito", "Modificación realizada.")
    frame_mod_opciones.pack_forget()
    mostrar_frame(frame_departamentos)
tk.Button(frame_mod_dpto, text="Buscar", command=buscar_modificar, bg="#274472", fg="#7ec8e3", font=("Arial", 12)).pack(pady=10)
tk.Button(frame_mod_opciones, text="Modificar", command=modificar_departamento, bg="#274472", fg="#7ec8e3", font=("Arial", 12)).pack(pady=10)
tk.Button(frame_mod_opciones, text="Volver", command=lambda: [frame_mod_opciones.pack_forget(), mostrar_frame(frame_departamentos)], bg="#c94c4c", fg="white", font=("Arial", 12)).pack(pady=10)
tk.Button(frame_mod_dpto, text="Volver", command=lambda: mostrar_frame(frame_departamentos), bg="#c94c4c", fg="white", font=("Arial", 12)).pack(pady=10)

# ============ CONSULTA DEPARTAMENTO ===============
frame_consulta_dpto = tk.Frame(root, bg="#1e3d59")
tk.Label(frame_consulta_dpto, text="Consulta Departamento", font=("Arial", 18), bg="#1e3d59", fg="#7ec8e3").pack(pady=20)
consulta_var = tk.StringVar()
tk.Label(frame_consulta_dpto, text="Filtrar por:", bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
tk.Radiobutton(frame_consulta_dpto, text="Torre", variable=consulta_var, value="torre", bg="#1e3d59", fg="#7ec8e3").pack(anchor="w")
tk.Radiobutton(frame_consulta_dpto, text="Torre y Piso", variable=consulta_var, value="torre_piso", bg="#1e3d59", fg="#7ec8e3").pack(anchor="w")
tk.Radiobutton(frame_consulta_dpto, text="Torre, Piso y Número", variable=consulta_var, value="torre_piso_num", bg="#1e3d59", fg="#7ec8e3").pack(anchor="w")
consulta_entry1 = tk.Entry(frame_consulta_dpto, font=("Arial", 12))
consulta_entry2 = tk.Entry(frame_consulta_dpto, font=("Arial", 12))
consulta_entry3 = tk.Entry(frame_consulta_dpto, font=("Arial", 12))
def consulta_departamento():
    filtro = consulta_var.get()
    torre = consulta_entry1.get().upper()
    piso = consulta_entry2.get()
    ndpto = consulta_entry3.get()
    resultados = []
    if filtro == "torre":
        resultados = [f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}" for h in range(len(torres)) if torres[h] == torre]
    elif filtro == "torre_piso":
        resultados = [f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}" for h in range(len(torres)) if torres[h] == torre and pisos[h] == piso]
    elif filtro == "torre_piso_num":
        resultados = [f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}" for h in range(len(torres)) if torres[h] == torre and pisos[h] == piso and dptos[h] == ndpto]
    else:
        resultados = ["Seleccione un filtro."]
    messagebox.showinfo("Consulta", "\n".join(resultados) if resultados else "Sin resultados.")
tk.Label(frame_consulta_dpto, text="Torre:", bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
consulta_entry1.pack()
tk.Label(frame_consulta_dpto, text="Piso:", bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
consulta_entry2.pack()
tk.Label(frame_consulta_dpto, text="Número:", bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
consulta_entry3.pack()
tk.Button(frame_consulta_dpto, text="Consultar", command=consulta_departamento, bg="#274472", fg="#7ec8e3", font=("Arial", 12)).pack(pady=10)
tk.Button(frame_consulta_dpto, text="Volver", command=lambda: mostrar_frame(frame_departamentos), bg="#c94c4c", fg="white", font=("Arial", 12)).pack(pady=10)

# ============ LISTADO DEPARTAMENTO ===============
frame_listado_dpto = tk.Frame(root, bg="#1e3d59")
tk.Label(frame_listado_dpto, text="Listado Departamentos", font=("Arial", 18), bg="#1e3d59", fg="#7ec8e3").pack(pady=20)
listado_var = tk.StringVar()
tk.Label(frame_listado_dpto, text="Filtrar por:", bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
tk.Radiobutton(frame_listado_dpto, text="Torre", variable=listado_var, value="torre", bg="#1e3d59", fg="#7ec8e3").pack(anchor="w")
tk.Radiobutton(frame_listado_dpto, text="Torre y Piso", variable=listado_var, value="torre_piso", bg="#1e3d59", fg="#7ec8e3").pack(anchor="w")
tk.Radiobutton(frame_listado_dpto, text="Torre, Piso y Número", variable=listado_var, value="torre_piso_num", bg="#1e3d59", fg="#7ec8e3").pack(anchor="w")
listado_entry1 = tk.Entry(frame_listado_dpto, font=("Arial", 12))
listado_entry2 = tk.Entry(frame_listado_dpto, font=("Arial", 12))
listado_entry3 = tk.Entry(frame_listado_dpto, font=("Arial", 12))
def listado_departamento():
    filtro = listado_var.get()
    torre = listado_entry1.get().upper()
    piso = listado_entry2.get()
    ndpto = listado_entry3.get()
    resultados = []
    if filtro == "torre":
        resultados = [f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}" for h in range(len(torres)) if torres[h] == torre]
    elif filtro == "torre_piso":
        resultados = [f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}" for h in range(len(torres)) if torres[h] == torre and pisos[h] == piso]
    elif filtro == "torre_piso_num":
        resultados = [f"Torre: {torres[h]}, Piso: {pisos[h]}, Departamento: {dptos[h]}, Habitaciones: {habitacioness[h]}, Metros cubiertos: {mtcubiertoss[h]}, Luz: {luzz[h]}, Agua: {aguas[h]}, Gas: {gass[h]}" for h in range(len(torres)) if torres[h] == torre and pisos[h] == piso and dptos[h] == ndpto]
    else:
        resultados = ["Seleccione un filtro."]
    with open("listado.txt", "a") as archivo:
        for r in resultados:
            archivo.write(r + '\n')
    messagebox.showinfo("Listado", "\n".join(resultados) if resultados else "Sin resultados.")
tk.Label(frame_listado_dpto, text="Torre:", bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
listado_entry1.pack()
tk.Label(frame_listado_dpto, text="Piso:", bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
listado_entry2.pack()
tk.Label(frame_listado_dpto, text="Número:", bg="#1e3d59", fg="#7ec8e3", font=("Arial", 12)).pack()
listado_entry3.pack()
tk.Button(frame_listado_dpto, text="Listar", command=listado_departamento, bg="#274472", fg="#7ec8e3", font=("Arial", 12)).pack(pady=10)
tk.Button(frame_listado_dpto, text="Volver", command=lambda: mostrar_frame(frame_departamentos), bg="#c94c4c", fg="white", font=("Arial", 12)).pack(pady=10)

# ============ LIQUIDACION ===============
def liquidacion():
    # Aquí puedes copiar la lógica de liquidación de CRUDMod.py y mostrarla en un messagebox
    messagebox.showinfo("Liquidación", "Aquí irá la liquidación detallada.")

# ============ FRAMES PROPIETARIOS Y COCHERAS ===============
frame_propietarios = tk.Frame(root, bg="#1e3d59")
tk.Label(frame_propietarios, text="Menú Propietarios", font=("Arial", 18), bg="#1e3d59", fg="#7ec8e3").pack(pady=30)
tk.Button(frame_propietarios, text="Alta", command=lambda: mostrar_frame(frame_alta_prop), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_propietarios, text="Baja", command=lambda: mostrar_frame(frame_baja_prop), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_propietarios, text="Modificación", command=lambda: mostrar_frame(frame_mod_prop), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_propietarios, text="Consulta", command=lambda: mostrar_frame(frame_consulta_prop), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_propietarios, text="Listado", command=lambda: mostrar_frame(frame_listado_prop), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_propietarios, text="Volver", command=lambda: mostrar_frame(frame_principal), bg="#c94c4c", fg="white", font=("Arial", 12)).pack(pady=20)

frame_cocheras = tk.Frame(root, bg="#1e3d59")
tk.Label(frame_cocheras, text="Menú Cocheras", font=("Arial", 18), bg="#1e3d59", fg="#7ec8e3").pack(pady=30)
tk.Button(frame_cocheras, text="Alta", command=lambda: mostrar_frame(frame_alta_coch), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_cocheras, text="Modificación", command=lambda: mostrar_frame(frame_mod_coch), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_cocheras, text="Consulta", command=lambda: mostrar_frame(frame_consulta_coch), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_cocheras, text="Listado", command=lambda: mostrar_frame(frame_listado_coch), bg="#274472", fg="#7ec8e3", font=("Arial", 14), width=20, height=2).pack(pady=5)
tk.Button(frame_cocheras, text="Volver", command=lambda: mostrar_frame(frame_principal), bg="#c94c4c", fg="white", font=("Arial", 12)).pack(pady=20)

# Mostrar el menú principal al iniciar
mostrar_frame(frame_principal)

# Iniciar la interfaz
root.mainloop()
