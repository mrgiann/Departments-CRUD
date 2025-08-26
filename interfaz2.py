import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

torres=["B","C","B","A","A"]
pisos=["2","1","7","6","5"]
dptos=["1","2","3","4","5"]
habitacioness=["4","7","4","8","9"]
mtcubiertoss=["20","20","30","100","50"]
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
cocheras_p = ["s","n","s","n","s"]
gyms = ["s","n","s","n","s"]
sums = ["s","n","s","n","s"]
dsums = ["0","0","0","0","0"]

torresc = ["A","B","C","A","B"]
pisosc = ["1","2","3","4","5"]
dptosc = ["1","2","3","4","5"]
mtcubiertossc = ["20","30","40","50","60"]
libres = ["s","n","s","n","s"]

grisfondo = "#4F4D46"
griscuadros= "#3F3D37"
colortexto= "#EDE8D0"
colorvolver = "#000000"
colorborrar = "#c94c4c"

root = tk.Tk()
root.title("Aministracion departamentos")
root.geometry("600x800")
root.configure(bg=grisfondo)

def mostrar_frame(frame):
    frame_principal.pack_forget()
    frame_departamentos.pack_forget()
    frame_propietarios.pack_forget()
    frame_cocheras.pack_forget()
    frame_alta_departamentos.pack_forget()
    frame_baja_departamentos.pack_forget()
    frame_modificacion_departamentos.pack_forget()
    frame_consulta_departamentos.pack_forget()
    frame_listado_departamentos.pack_forget()
    frame_alta_propietarios.pack_forget()
    frame_baja_propietarios.pack_forget()
    frame_modificacion_propietarios.pack_forget()
    frame_consulta_propietarios.pack_forget()
    frame_listado_propietarios.pack_forget()
    frame_alta_cocheras.pack_forget()
    frame_baja_cocheras.pack_forget()
    frame_modificacion_cocheras.pack_forget()
    frame_consulta_cocheras.pack_forget()
    frame_listado_cocheras.pack_forget()
    if frame == frame_alta_departamentos:
        alta_departamento()
    elif frame == frame_baja_departamentos:
        baja_departamento()
    elif frame == frame_modificacion_departamentos:
        modificacion_departamento()
    elif frame == frame_consulta_departamentos:
        consulta_departamento()
    elif frame == frame_listado_departamentos:
        listado_departamento()
    elif frame == frame_alta_propietarios:
        alta_propietario()
    elif frame == frame_baja_propietarios:
        baja_propietario()
    elif frame == frame_modificacion_propietarios:
        modificacion_propietario()
    elif frame == frame_consulta_propietarios:
        consulta_propietario()
    elif frame == frame_listado_propietarios:
        listado_propietario()
    elif frame == frame_alta_cocheras:
        alta_cochera()
    elif frame == frame_modificacion_cocheras:
        modificacion_cochera()
    elif frame == frame_consulta_cocheras:
        consulta_cochera()
    elif frame == frame_listado_cocheras:
        listado_cochera()
    frame.pack()
    
def crear_frame():
    return tk.Frame(root, bg=grisfondo)

def crear_titulo(frame, texto):
    tk.Label(frame, text=texto, font=("Arial", 18), bg=grisfondo, fg=colortexto).pack(pady=20)

frame_principal = crear_frame()
titulo = tk.Label(frame_principal, text="Menú Principal", font=("Arial", 20), bg=grisfondo, fg=colortexto)
titulo.pack(pady=30)
frame_principal.pack()
botones = [
    ("Departamentos", lambda: mostrar_frame(frame_departamentos)),
    ("Propietarios", lambda: mostrar_frame(frame_propietarios)),
    ("Cocheras", lambda: mostrar_frame(frame_cocheras)),
    ("Liquidación", lambda: liquidacion()),
    ("Salir", root.quit)
]
for texto, comando in botones:
    tk.Button(frame_principal, text=texto, command=comando, bg=griscuadros, fg=colortexto,
              font=("Arial", 14), width=20, height=2).pack(pady=5)

frame_departamentos = crear_frame()
frame_propietarios = crear_frame()
frame_cocheras = crear_frame()
frame_alta_departamentos = crear_frame()
frame_baja_departamentos = crear_frame()
frame_modificacion_departamentos = crear_frame()
frame_consulta_departamentos = crear_frame()
frame_listado_departamentos = crear_frame()
frame_alta_propietarios = crear_frame()
frame_baja_propietarios = crear_frame()
frame_modificacion_propietarios = crear_frame()
frame_consulta_propietarios = crear_frame()
frame_listado_propietarios = crear_frame()
frame_alta_cocheras = crear_frame()
frame_baja_cocheras = crear_frame()
frame_modificacion_cocheras = crear_frame()
frame_consulta_cocheras = crear_frame()
frame_listado_cocheras = crear_frame()

crear_titulo(frame_departamentos, "Menu de Departamento")
crear_titulo(frame_propietarios, "Menu de Propietario")
crear_titulo(frame_cocheras, "Menu de Cochera")

botones_departamento = [
    ("Alta", lambda: mostrar_frame(frame_alta_departamentos)),
    ("Baja", lambda: mostrar_frame(frame_baja_departamentos)),
    ("Modificacion", lambda: mostrar_frame(frame_modificacion_departamentos)),
    ("Consulta", lambda: mostrar_frame(frame_consulta_departamentos)),
    ("Listado", lambda: mostrar_frame(frame_listado_departamentos)),
    ("Salir", lambda: mostrar_frame(frame_principal))
]
botones_propietario = [
    ("Alta", lambda: mostrar_frame(frame_alta_propietarios)),
    ("Baja", lambda: mostrar_frame(frame_baja_propietarios)),
    ("Modificacion", lambda: mostrar_frame(frame_modificacion_propietarios)),
    ("Consulta", lambda: mostrar_frame(frame_consulta_propietarios)),
    ("Listado", lambda: mostrar_frame(frame_listado_propietarios)),
    ("Salir", lambda: mostrar_frame(frame_principal))
]
botones_cochera = [
    ("Alta", lambda: mostrar_frame(frame_alta_cocheras)),
    ("Modificacion", lambda: mostrar_frame(frame_modificacion_cocheras)),
    ("Consulta", lambda: mostrar_frame(frame_consulta_cocheras)),
    ("Listado", lambda: mostrar_frame(frame_listado_cocheras)),
    ("Salir", lambda: mostrar_frame(frame_principal))
]
for texto, comando in botones_departamento:
    tk.Button(frame_departamentos, text=texto, command=comando, bg=griscuadros, fg=colortexto,
              font=("Arial", 14), width=20, height=2).pack(pady=5)
for texto, comando in botones_propietario:
    tk.Button(frame_propietarios, text=texto, command=comando, bg=griscuadros, fg=colortexto,
              font=("Arial", 14), width=20, height=2).pack(pady=5)
for texto, comando in botones_cochera:
    tk.Button(frame_cocheras, text=texto, command=comando, bg=griscuadros, fg=colortexto,
              font=("Arial", 14), width=20, height=2).pack(pady=5)

def alta_departamento():
    for widget in frame_alta_departamentos.winfo_children():
        widget.destroy()

    # Alta departamentos
    alta_torre = tk.StringVar()
    alta_piso = tk.StringVar()
    alta_numero = tk.StringVar()
    alta_habitaciones = tk.StringVar()
    alta_metros = tk.StringVar()
    alta_luz = tk.StringVar()
    alta_agua = tk.StringVar()
    alta_gas = tk.StringVar()

    crear_titulo(frame_alta_departamentos, "Alta Departamento")
    tk.Label(frame_alta_departamentos, text="Torre (A/B/C)", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    torre_frame = tk.Frame(frame_alta_departamentos, bg=grisfondo)
    rb_torre_a = tk.Radiobutton(torre_frame, text="A", variable=alta_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_b = tk.Radiobutton(torre_frame, text="B", variable=alta_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_c = tk.Radiobutton(torre_frame, text="C", variable=alta_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    torre_frame.pack(pady=2)
    rb_torre_a.pack(side=tk.LEFT, padx=10)
    rb_torre_b.pack(side=tk.LEFT, padx=10)
    rb_torre_c.pack(side=tk.LEFT, padx=10)

    tk.Label(frame_alta_departamentos, text="Piso", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    entry_piso = tk.Entry(frame_alta_departamentos, textvariable=alta_piso, font=("Arial", 12))
    entry_piso.pack(pady=2)
    tk.Label(frame_alta_departamentos, text="Número", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    entry_numero = tk.Entry(frame_alta_departamentos, textvariable=alta_numero, font=("Arial", 12))
    entry_numero.pack(pady=2)
    tk.Label(frame_alta_departamentos, text="Habitaciones", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    entry_habitaciones = tk.Entry(frame_alta_departamentos, textvariable=alta_habitaciones, font=("Arial", 12))
    entry_habitaciones.pack(pady=2)
    tk.Label(frame_alta_departamentos, text="Metros Cubiertos", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    entry_metros = tk.Entry(frame_alta_departamentos, textvariable=alta_metros, font=("Arial", 12))
    entry_metros.pack(pady=2)
    tk.Label(frame_alta_departamentos, text="Luz", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    entry_luz = tk.Entry(frame_alta_departamentos, textvariable=alta_luz, font=("Arial", 12))
    entry_luz.pack(pady=2)
    tk.Label(frame_alta_departamentos, text="Agua", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    entry_agua = tk.Entry(frame_alta_departamentos, textvariable=alta_agua, font=("Arial", 12))
    entry_agua.pack(pady=2)
    tk.Label(frame_alta_departamentos, text="Gas", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    entry_gas = tk.Entry(frame_alta_departamentos, textvariable=alta_gas, font=("Arial", 12))
    entry_gas.pack(pady=2)

    def guardar_departamento():
        t = alta_torre.get().upper()
        p = alta_piso.get()
        n = alta_numero.get()
        h = alta_habitaciones.get()
        m = alta_metros.get()
        l = alta_luz.get()
        a = alta_agua.get()
        g = alta_gas.get()
        if t not in "ABC":
            messagebox.showerror("Error", "Torre inválida.")
            return
        existe = False
        for i in range(len(torres)):
            if torres[i] == t and pisos[i] == p and dptos[i] == n:
                existe = True
                break
        if existe:
            messagebox.showerror("Error", "El departamento ya existe.")
            return
        datos = f"Torre: {t}\nPiso: {p}\nNúmero: {n}\nHabitaciones: {h}\nMetros Cubiertos: {m}\nLuz: {l}\nAgua: {a}\nGas: {g}"
        confirmar = messagebox.askyesno("Confirmar datos", f"¿Desea guardar estos datos?\n\n{datos}")
        if not confirmar:
            return
        torres.append(t)
        pisos.append(p)
        dptos.append(n)
        habitacioness.append(h)
        mtcubiertoss.append(m)
        luzz.append(l)
        aguas.append(a)
        gass.append(g)
        messagebox.showinfo("Éxito", "Departamento cargado exitosamente.")
        alta_torre.set("")
        alta_piso.set("")
        alta_numero.set("")
        alta_habitaciones.set("")
        alta_metros.set("")
        alta_luz.set("")
        alta_agua.set("")
        alta_gas.set("")
        frame_alta_departamentos.pack_forget()
        mostrar_frame(frame_departamentos)

    btn_guardar = tk.Button(frame_alta_departamentos, text="Guardar", command=guardar_departamento, bg=griscuadros, fg=colortexto, font=("Arial", 12))
    btn_guardar.pack(pady=10)
    btn_volver = tk.Button(frame_alta_departamentos, text="Volver", command=lambda: mostrar_frame(frame_departamentos), bg=colorvolver, fg="white", font=("Arial", 12))
    btn_volver.pack(pady=10)

def baja_departamento():
    for widget in frame_baja_departamentos.winfo_children():
        widget.destroy()

    baja_torre = tk.StringVar()
    baja_piso = tk.StringVar()
    baja_numero = tk.StringVar()

    crear_titulo(frame_baja_departamentos, "Baja Departamento")
    tk.Label(frame_baja_departamentos, text="Torre (A/B/C)", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    torre_frame = tk.Frame(frame_baja_departamentos, bg=grisfondo)
    rb_torre_a = tk.Radiobutton(torre_frame, text="A", variable=baja_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_b = tk.Radiobutton(torre_frame, text="B", variable=baja_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_c = tk.Radiobutton(torre_frame, text="C", variable=baja_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    torre_frame.pack(pady=2)
    rb_torre_a.pack(side=tk.LEFT, padx=10)
    rb_torre_b.pack(side=tk.LEFT, padx=10)
    rb_torre_c.pack(side=tk.LEFT, padx=10)

    tk.Label(frame_baja_departamentos, text="Piso", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    entry_piso = tk.Entry(frame_baja_departamentos, textvariable=baja_piso, font=("Arial", 12))
    entry_piso.pack(pady=2)
    tk.Label(frame_baja_departamentos, text="Número", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    entry_numero = tk.Entry(frame_baja_departamentos, textvariable=baja_numero, font=("Arial", 12))
    entry_numero.pack(pady=2)

    def eliminar_departamento():
        torre = baja_torre.get().upper()
        piso = baja_piso.get()
        ndpto = baja_numero.get()
        for i in range(len(torres)):
            if torres[i] == torre and pisos[i] == piso and dptos[i] == ndpto:
                torres.pop(i)
                pisos.pop(i)
                dptos.pop(i)
                habitacioness.pop(i)
                mtcubiertoss.pop(i)
                luzz.pop(i)
                aguas.pop(i)
                gass.pop(i)
                messagebox.showinfo("Éxito", "Departamento eliminado exitosamente.")
                frame_baja_departamentos.pack_forget()
                mostrar_frame(frame_departamentos)
                return
        messagebox.showerror("Error", "El departamento no existe.")

    btn_eliminar = tk.Button(frame_baja_departamentos, text="Eliminar", command=eliminar_departamento, bg=colorborrar, fg="white", font=("Arial", 12))
    btn_eliminar.pack(pady=10)
    btn_volver = tk.Button(frame_baja_departamentos, text="Volver", command=lambda: mostrar_frame(frame_departamentos), bg=colorvolver, fg="white", font=("Arial", 12))
    btn_volver.pack(pady=10)

def modificacion_departamento():
    for widget in frame_modificacion_departamentos.winfo_children():
        widget.destroy()

    mod_torre = tk.StringVar()
    mod_piso = tk.StringVar()
    mod_numero = tk.StringVar()
    opcion_mod = tk.StringVar()
    nuevo_valor = tk.StringVar()
    mod_index = [None]

    crear_titulo(frame_modificacion_departamentos, "Modificacion Departamento")
    tk.Label(frame_modificacion_departamentos, text="Torre (A/B/C)", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    torre_frame = tk.Frame(frame_modificacion_departamentos, bg=grisfondo)
    rb_torre_a = tk.Radiobutton(torre_frame, text="A", variable=mod_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_b = tk.Radiobutton(torre_frame, text="B", variable=mod_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_c = tk.Radiobutton(torre_frame, text="C", variable=mod_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    torre_frame.pack(pady=2)
    rb_torre_a.pack(side=tk.LEFT, padx=10)
    rb_torre_b.pack(side=tk.LEFT, padx=10)
    rb_torre_c.pack(side=tk.LEFT, padx=10)

    tk.Label(frame_modificacion_departamentos, text="Piso", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    entry_piso = tk.Entry(frame_modificacion_departamentos, textvariable=mod_piso, font=("Arial", 12))
    entry_piso.pack(pady=2)
    tk.Label(frame_modificacion_departamentos, text="Número", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    entry_numero = tk.Entry(frame_modificacion_departamentos, textvariable=mod_numero, font=("Arial", 12))
    entry_numero.pack(pady=2)

    def buscar_modificar():
        torre = mod_torre.get().upper()
        piso = mod_piso.get()
        ndpto = mod_numero.get()
        for i in range(len(torres)):
            if torres[i] == torre and pisos[i] == piso and dptos[i] == ndpto:
                mod_index[0] = i
                frame_mod_opciones.pack()
                return
        messagebox.showerror("Error", "El departamento no existe.")

    btn_buscar = tk.Button(frame_modificacion_departamentos, text="Buscar", command=buscar_modificar, bg=griscuadros, fg=colortexto, font=("Arial", 12))
    btn_buscar.pack(pady=10)

    frame_mod_opciones = tk.Frame(frame_modificacion_departamentos, bg=grisfondo)
    tk.Label(frame_mod_opciones, text="¿Qué desea modificar?", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    for campo in ["Habitaciones", "Metros Cubiertos", "Luz", "Agua", "Gas"]:
        tk.Radiobutton(frame_mod_opciones, text=campo, variable=opcion_mod, value=campo, bg=grisfondo, fg=colorvolver, font=("Arial", 12)).pack(anchor="w")
    tk.Label(frame_mod_opciones, text="Nuevo valor:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    tk.Entry(frame_mod_opciones, textvariable=nuevo_valor, font=("Arial", 12)).pack()

    def modificar_departamento():
        i = mod_index[0]
        campo = opcion_mod.get()
        valor = nuevo_valor.get()
        if i is None:
            messagebox.showerror("Error", "Debe buscar un departamento primero.")
            return
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
        frame_modificacion_departamentos.pack_forget()
        mostrar_frame(frame_departamentos)

    btn_modificar = tk.Button(frame_mod_opciones, text="Modificar", command=modificar_departamento, bg=griscuadros, fg=colortexto, font=("Arial", 12))
    btn_modificar.pack(pady=10)
    btn_volver_opciones = tk.Button(frame_mod_opciones, text="Volver", command=lambda: frame_mod_opciones.pack_forget(), bg=colorvolver, fg="white", font=("Arial", 12))
    btn_volver_opciones.pack(pady=10)
    btn_volver = tk.Button(frame_modificacion_departamentos, text="Volver", command=lambda: mostrar_frame(frame_departamentos), bg=colorvolver, fg="white", font=("Arial", 12))
    btn_volver.pack(pady=10)

def consulta_departamento():
    for widget in frame_consulta_departamentos.winfo_children():
        widget.destroy()

    consulta_var = tk.StringVar()
    consulta_torre = tk.StringVar()
    consulta_entry2 = tk.Entry(frame_consulta_departamentos, font=("Arial", 12))
    consulta_entry3 = tk.Entry(frame_consulta_departamentos, font=("Arial", 12))

    crear_titulo(frame_consulta_departamentos, "Consulta Departamento")
    tk.Label(frame_consulta_departamentos, text="Filtrar por:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    tk.Radiobutton(frame_consulta_departamentos, text="Torre", variable=consulta_var, value="torre", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Radiobutton(frame_consulta_departamentos, text="Torre y Piso", variable=consulta_var, value="torre_piso", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Radiobutton(frame_consulta_departamentos, text="Torre, Piso y Número", variable=consulta_var, value="torre_piso_num", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Label(frame_consulta_departamentos, text="Torre:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    torre_frame = tk.Frame(frame_consulta_departamentos, bg=grisfondo)
    rb_torre_a = tk.Radiobutton(torre_frame, text="A", variable=consulta_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_b = tk.Radiobutton(torre_frame, text="B", variable=consulta_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_c = tk.Radiobutton(torre_frame, text="C", variable=consulta_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    torre_frame.pack(pady=2)
    rb_torre_a.pack(side=tk.LEFT, padx=10)
    rb_torre_b.pack(side=tk.LEFT, padx=10)
    rb_torre_c.pack(side=tk.LEFT, padx=10)
    tk.Label(frame_consulta_departamentos, text="Piso:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    consulta_entry2.pack()
    tk.Label(frame_consulta_departamentos, text="Número:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    consulta_entry3.pack()

    def consultar():
        filtro = consulta_var.get()
        torre = consulta_torre.get().upper()
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

    btn_consultar = tk.Button(frame_consulta_departamentos, text="Consultar", command=consultar, bg=griscuadros, fg=colortexto, font=("Arial", 12))
    btn_consultar.pack(pady=10)
    btn_volver = tk.Button(frame_consulta_departamentos, text="Volver", command=lambda: mostrar_frame(frame_departamentos), bg=colorvolver, fg="white", font=("Arial", 12))
    btn_volver.pack(pady=10)

def listado_departamento():
    for widget in frame_listado_departamentos.winfo_children():
        widget.destroy()

    listado_var = tk.StringVar()
    listado_torre = tk.StringVar()
    listado_entry2 = tk.Entry(frame_listado_departamentos, font=("Arial", 12))
    listado_entry3 = tk.Entry(frame_listado_departamentos, font=("Arial", 12))

    crear_titulo(frame_listado_departamentos, "Listado Departamento")
    tk.Label(frame_listado_departamentos, text="Filtrar por:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    tk.Radiobutton(frame_listado_departamentos, text="Torre", variable=listado_var, value="torre", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Radiobutton(frame_listado_departamentos, text="Torre y Piso", variable=listado_var, value="torre_piso", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Radiobutton(frame_listado_departamentos, text="Torre, Piso y Número", variable=listado_var, value="torre_piso_num", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Label(frame_listado_departamentos, text="Torre:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    torre_frame = tk.Frame(frame_listado_departamentos, bg=grisfondo)
    rb_torre_a = tk.Radiobutton(torre_frame, text="A", variable=listado_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_b = tk.Radiobutton(torre_frame, text="B", variable=listado_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_c = tk.Radiobutton(torre_frame, text="C", variable=listado_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    torre_frame.pack(pady=2)
    rb_torre_a.pack(side=tk.LEFT, padx=10)
    rb_torre_b.pack(side=tk.LEFT, padx=10)
    rb_torre_c.pack(side=tk.LEFT, padx=10)
    tk.Label(frame_listado_departamentos, text="Piso:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    listado_entry2.pack()
    tk.Label(frame_listado_departamentos, text="Número:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    listado_entry3.pack()

    def listar():
        filtro = listado_var.get()
        torre = listado_torre.get().upper()
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

    btn_listar = tk.Button(frame_listado_departamentos, text="Listar", command=listar, bg=griscuadros, fg=colortexto, font=("Arial", 12))
    btn_listar.pack(pady=10)
    btn_volver = tk.Button(frame_listado_departamentos, text="Volver", command=lambda: mostrar_frame(frame_departamentos), bg=colorvolver, fg="white", font=("Arial", 12))
    btn_volver.pack(pady=10)
    
def alta_propietario():
    for widget in frame_alta_propietarios.winfo_children():
        widget.destroy()

    alta_torre = tk.StringVar()
    alta_piso = tk.StringVar()
    alta_numero = tk.StringVar()
    alta_nombre = tk.StringVar()
    alta_habitantes = tk.StringVar()
    alta_fechac = tk.StringVar()
    alta_fechav = tk.StringVar()
    alta_cochera = tk.StringVar()
    alta_gym = tk.StringVar()
    alta_sum = tk.StringVar()
    alta_consumosum = tk.StringVar()

    crear_titulo(frame_alta_propietarios, "Alta Propietario")
    tk.Label(frame_alta_propietarios, text="Torre (A/B/C)", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    torre_frame = tk.Frame(frame_alta_propietarios, bg=grisfondo)
    rb_torre_a = tk.Radiobutton(torre_frame, text="A", variable=alta_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_b = tk.Radiobutton(torre_frame, text="B", variable=alta_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_c = tk.Radiobutton(torre_frame, text="C", variable=alta_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    torre_frame.pack(pady=2)
    rb_torre_a.pack(side=tk.LEFT, padx=10)
    rb_torre_b.pack(side=tk.LEFT, padx=10)
    rb_torre_c.pack(side=tk.LEFT, padx=10)

    tk.Label(frame_alta_propietarios, text="Piso", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_propietarios, textvariable=alta_piso, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_alta_propietarios, text="Número", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_propietarios, textvariable=alta_numero, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_alta_propietarios, text="Nombre y Apellido", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_propietarios, textvariable=alta_nombre, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_alta_propietarios, text="Habitantes", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_propietarios, textvariable=alta_habitantes, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_alta_propietarios, text="Fecha Compra", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_propietarios, textvariable=alta_fechac, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_alta_propietarios, text="Fecha Venta", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_propietarios, textvariable=alta_fechav, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_alta_propietarios, text="Cochera (s/n)", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_propietarios, textvariable=alta_cochera, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_alta_propietarios, text="Gym (s/n)", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_propietarios, textvariable=alta_gym, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_alta_propietarios, text="Sum (s/n)", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_propietarios, textvariable=alta_sum, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_alta_propietarios, text="Consumo Sum", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_propietarios, textvariable=alta_consumosum, font=("Arial", 12)).pack(pady=2)

    def guardar_propietario():
        torre = alta_torre.get().upper()
        piso = alta_piso.get()
        ndpto = alta_numero.get()
        # Validar que exista el departamento
        existe_departamento = any(
            torres[i] == torre and pisos[i] == piso and dptos[i] == ndpto
            for i in range(len(torres))
        )
        if torre not in ("A", "B", "C"):
            messagebox.showerror("Error", "Torre inválida.")
            return
        if not existe_departamento:
            messagebox.showerror("Error", "El departamento no existe. Debe cargar primero el departamento.")
            return
        if any(torresp[i] == torre and pisosp[i] == piso and dptosp[i] == ndpto for i in range(len(torresp))):
            messagebox.showerror("Error", "El propietario ya existe.")
            return
        torresp.append(torre)
        pisosp.append(piso)
        dptosp.append(ndpto)
        nombresyapellidos.append(alta_nombre.get())
        habitantess.append(alta_habitantes.get())
        fechasc.append(alta_fechac.get())
        fechasv.append(alta_fechav.get())
        cocheras_p.append(alta_cochera.get())
        gyms.append(alta_gym.get())
        sums.append(alta_sum.get())
        dsums.append(alta_consumosum.get())
        messagebox.showinfo("Éxito", "Propietario cargado exitosamente.")
        frame_alta_propietarios.pack_forget()
        mostrar_frame(frame_propietarios)

    btn_guardar = tk.Button(frame_alta_propietarios, text="Guardar", command=guardar_propietario, bg=griscuadros, fg=colortexto, font=("Arial", 12))
    btn_guardar.pack(pady=10)
    btn_volver = tk.Button(frame_alta_propietarios, text="Volver", command=lambda: mostrar_frame(frame_propietarios), bg=colorvolver, fg="white", font=("Arial", 12))
    btn_volver.pack(pady=10)

def baja_propietario():
    for widget in frame_baja_propietarios.winfo_children():
        widget.destroy()

    baja_torre = tk.StringVar()
    baja_piso = tk.StringVar()
    baja_numero = tk.StringVar()

    crear_titulo(frame_baja_propietarios, "Baja Propietario")
    tk.Label(frame_baja_propietarios, text="Torre (A/B/C)", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    torre_frame = tk.Frame(frame_baja_propietarios, bg=grisfondo)
    rb_torre_a = tk.Radiobutton(torre_frame, text="A", variable=baja_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_b = tk.Radiobutton(torre_frame, text="B", variable=baja_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_c = tk.Radiobutton(torre_frame, text="C", variable=baja_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    torre_frame.pack(pady=2)
    rb_torre_a.pack(side=tk.LEFT, padx=10)
    rb_torre_b.pack(side=tk.LEFT, padx=10)
    rb_torre_c.pack(side=tk.LEFT, padx=10)

    tk.Label(frame_baja_propietarios, text="Piso", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_baja_propietarios, textvariable=baja_piso, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_baja_propietarios, text="Número", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_baja_propietarios, textvariable=baja_numero, font=("Arial", 12)).pack(pady=2)

    def eliminar_propietario():
        torre = baja_torre.get().upper()
        piso = baja_piso.get()
        ndpto = baja_numero.get()
        for i in range(len(torresp)):
            if torresp[i] == torre and pisosp[i] == piso and dptosp[i] == ndpto:
                torresp.pop(i)
                pisosp.pop(i)
                dptosp.pop(i)
                nombresyapellidos.pop(i)
                habitantess.pop(i)
                fechasc.pop(i)
                fechasv.pop(i)
                cocheras_p.pop(i)
                gyms.pop(i)
                sums.pop(i)
                dsums.pop(i)
                messagebox.showinfo("Éxito", "Propietario eliminado.")
                frame_baja_propietarios.pack_forget()
                mostrar_frame(frame_propietarios)
                return
        messagebox.showerror("Error", "El propietario no existe.")

    btn_eliminar = tk.Button(frame_baja_propietarios, text="Eliminar", command=eliminar_propietario, bg=colorborrar, fg="white", font=("Arial", 12))
    btn_eliminar.pack(pady=10)
    btn_volver = tk.Button(frame_baja_propietarios, text="Volver", command=lambda: mostrar_frame(frame_propietarios), bg=colorvolver, fg="white", font=("Arial", 12))
    btn_volver.pack(pady=10)

def modificacion_propietario():
    for widget in frame_modificacion_propietarios.winfo_children():
        widget.destroy()

    mod_torre = tk.StringVar()
    mod_piso = tk.StringVar()
    mod_numero = tk.StringVar()
    opcion_mod = tk.StringVar()
    nuevo_valor = tk.StringVar()
    mod_index = [None]

    crear_titulo(frame_modificacion_propietarios, "Modificacion Propietario")
    tk.Label(frame_modificacion_propietarios, text="Torre (A/B/C)", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    torre_frame = tk.Frame(frame_modificacion_propietarios, bg=grisfondo)
    rb_torre_a = tk.Radiobutton(torre_frame, text="A", variable=mod_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_b = tk.Radiobutton(torre_frame, text="B", variable=mod_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_c = tk.Radiobutton(torre_frame, text="C", variable=mod_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    torre_frame.pack(pady=2)
    rb_torre_a.pack(side=tk.LEFT, padx=10)
    rb_torre_b.pack(side=tk.LEFT, padx=10)
    rb_torre_c.pack(side=tk.LEFT, padx=10)

    tk.Label(frame_modificacion_propietarios, text="Piso", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_modificacion_propietarios, textvariable=mod_piso, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_modificacion_propietarios, text="Número", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_modificacion_propietarios, textvariable=mod_numero, font=("Arial", 12)).pack(pady=2)

    def buscar_modificar():
        torre = mod_torre.get().upper()
        piso = mod_piso.get()
        ndpto = mod_numero.get()
        for i in range(len(torresp)):
            if torresp[i] == torre and pisosp[i] == piso and dptosp[i] == ndpto:
                mod_index[0] = i
                frame_mod_opciones.pack()
                return
        messagebox.showerror("Error", "El propietario no existe.")

    btn_buscar = tk.Button(frame_modificacion_propietarios, text="Buscar", command=buscar_modificar, bg=griscuadros, fg=colortexto, font=("Arial", 12))
    btn_buscar.pack(pady=10)

    frame_mod_opciones = tk.Frame(frame_modificacion_propietarios, bg=grisfondo)
    tk.Label(frame_mod_opciones, text="¿Qué desea modificar?", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    for campo in ["Nombre y Apellido", "Habitantes", "Fecha Compra", "Fecha Venta", "Cochera (s/n)", "Gym (s/n)", "Sum (s/n)", "Consumo Sum"]:
        tk.Radiobutton(frame_mod_opciones, text=campo, variable=opcion_mod, value=campo, bg=grisfondo, fg=colorvolver, font=("Arial", 12)).pack(anchor="w")
    tk.Label(frame_mod_opciones, text="Nuevo valor:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    tk.Entry(frame_mod_opciones, textvariable=nuevo_valor, font=("Arial", 12)).pack()

    def modificar_propietario():
        i = mod_index[0]
        campo = opcion_mod.get()
        valor = nuevo_valor.get()
        if i is None:
            messagebox.showerror("Error", "Debe buscar un propietario primero.")
            return
        if campo == "Nombre y Apellido":
            nombresyapellidos[i] = valor
        elif campo == "Habitantes":
            habitantess[i] = valor
        elif campo == "Fecha Compra":
            fechasc[i] = valor
        elif campo == "Fecha Venta":
            fechasv[i] = valor
        elif campo == "Cochera (s/n)":
            cocheras_p[i] = valor
        elif campo == "Gym (s/n)":
            gyms[i] = valor
        elif campo == "Sum (s/n)":
            sums[i] = valor
        elif campo == "Consumo Sum":
            dsums[i] = valor
        else:
            messagebox.showerror("Error", "Opción inválida.")
            return
        messagebox.showinfo("Éxito", "Modificación realizada.")
        frame_mod_opciones.pack_forget()
        frame_modificacion_propietarios.pack_forget()
        mostrar_frame(frame_propietarios)

    btn_modificar = tk.Button(frame_mod_opciones, text="Modificar", command=modificar_propietario, bg=griscuadros, fg=colortexto, font=("Arial", 12))
    btn_modificar.pack(pady=10)
    btn_volver_opciones = tk.Button(frame_mod_opciones, text="Volver", command=lambda: frame_mod_opciones.pack_forget(), bg=colorvolver, fg="white", font=("Arial", 12))
    btn_volver_opciones.pack(pady=10)
    btn_volver = tk.Button(frame_modificacion_propietarios, text="Volver", command=lambda: mostrar_frame(frame_propietarios), bg=colorvolver, fg="white", font=("Arial", 12))
    btn_volver.pack(pady=10)

def consulta_propietario():
    for widget in frame_consulta_propietarios.winfo_children():
        widget.destroy()

    consulta_var = tk.StringVar()
    consulta_torre = tk.StringVar()
    consulta_entry2 = tk.Entry(frame_consulta_propietarios, font=("Arial", 12))
    consulta_entry3 = tk.Entry(frame_consulta_propietarios, font=("Arial", 12))

    crear_titulo(frame_consulta_propietarios, "Consulta Propietario")
    tk.Label(frame_consulta_propietarios, text="Filtrar por:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    tk.Radiobutton(frame_consulta_propietarios, text="Torre", variable=consulta_var, value="torre", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Radiobutton(frame_consulta_propietarios, text="Torre y Piso", variable=consulta_var, value="torre_piso", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Radiobutton(frame_consulta_propietarios, text="Torre, Piso y Número", variable=consulta_var, value="torre_piso_num", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Label(frame_consulta_propietarios, text="Torre:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    torre_frame = tk.Frame(frame_consulta_propietarios, bg=grisfondo)
    rb_torre_a = tk.Radiobutton(torre_frame, text="A", variable=consulta_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_b = tk.Radiobutton(torre_frame, text="B", variable=consulta_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_c = tk.Radiobutton(torre_frame, text="C", variable=consulta_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    torre_frame.pack(pady=2)
    rb_torre_a.pack(side=tk.LEFT, padx=10)
    rb_torre_b.pack(side=tk.LEFT, padx=10)
    rb_torre_c.pack(side=tk.LEFT, padx=10)
    tk.Label(frame_consulta_propietarios, text="Piso:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    consulta_entry2.pack()
    tk.Label(frame_consulta_propietarios, text="Número:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    consulta_entry3.pack()

    def consultar():
        filtro = consulta_var.get()
        torre = consulta_torre.get().upper()
        piso = consulta_entry2.get()
        ndpto = consulta_entry3.get()
        resultados = []
        if filtro == "torre":
            resultados = [f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Compra: {fechasc[h]}, Venta: {fechasv[h]}, Cochera: {cocheras_p[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Consumo Sum: {dsums[h]}" for h in range(len(torresp)) if torresp[h] == torre]
        elif filtro == "torre_piso":
            resultados = [f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Compra: {fechasc[h]}, Venta: {fechasv[h]}, Cochera: {cocheras_p[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Consumo Sum: {dsums[h]}" for h in range(len(torresp)) if torresp[h] == torre and pisosp[h] == piso]
        elif filtro == "torre_piso_num":
            resultados = [f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Compra: {fechasc[h]}, Venta: {fechasv[h]}, Cochera: {cocheras_p[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Consumo Sum: {dsums[h]}" for h in range(len(torresp)) if torresp[h] == torre and pisosp[h] == piso and dptosp[h] == ndpto]
        else:
            resultados = ["Seleccione un filtro."]
        messagebox.showinfo("Consulta", "\n".join(resultados) if resultados else "Sin resultados.")

    btn_consultar = tk.Button(frame_consulta_propietarios, text="Consultar", command=consultar, bg=griscuadros, fg=colortexto, font=("Arial", 12))
    btn_consultar.pack(pady=10)
    btn_volver = tk.Button(frame_consulta_propietarios, text="Volver", command=lambda: mostrar_frame(frame_propietarios), bg=colorvolver, fg="white", font=("Arial", 12))
    btn_volver.pack(pady=10)

def listado_propietario():
    for widget in frame_listado_propietarios.winfo_children():
        widget.destroy()

    listado_var = tk.StringVar()
    listado_torre = tk.StringVar()
    listado_entry2 = tk.Entry(frame_listado_propietarios, font=("Arial", 12))
    listado_entry3 = tk.Entry(frame_listado_propietarios, font=("Arial", 12))

    crear_titulo(frame_listado_propietarios, "Listado Propietarios")
    tk.Label(frame_listado_propietarios, text="Filtrar por:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    tk.Radiobutton(frame_listado_propietarios, text="Torre", variable=listado_var, value="torre", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Radiobutton(frame_listado_propietarios, text="Torre y Piso", variable=listado_var, value="torre_piso", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Radiobutton(frame_listado_propietarios, text="Torre, Piso y Número", variable=listado_var, value="torre_piso_num", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Label(frame_listado_propietarios, text="Torre:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    torre_frame = tk.Frame(frame_listado_propietarios, bg=grisfondo)
    rb_torre_a = tk.Radiobutton(torre_frame, text="A", variable=listado_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_b = tk.Radiobutton(torre_frame, text="B", variable=listado_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_c = tk.Radiobutton(torre_frame, text="C", variable=listado_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    torre_frame.pack(pady=2)
    rb_torre_a.pack(side=tk.LEFT, padx=10)
    rb_torre_b.pack(side=tk.LEFT, padx=10)
    rb_torre_c.pack(side=tk.LEFT, padx=10)
    tk.Label(frame_listado_propietarios, text="Piso:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    listado_entry2.pack()
    tk.Label(frame_listado_propietarios, text="Número:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    listado_entry3.pack()

    def listar():
        filtro = listado_var.get()
        torre = listado_torre.get().upper()
        piso = listado_entry2.get()
        ndpto = listado_entry3.get()
        resultados = []
        if filtro == "torre":
            resultados = [f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Compra: {fechasc[h]}, Venta: {fechasv[h]}, Cochera: {cocheras_p[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Consumo Sum: {dsums[h]}" for h in range(len(torresp)) if torresp[h] == torre]
        elif filtro == "torre_piso":
            resultados = [f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Compra: {fechasc[h]}, Venta: {fechasv[h]}, Cochera: {cocheras_p[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Consumo Sum: {dsums[h]}" for h in range(len(torresp)) if torresp[h] == torre and pisosp[h] == piso]
        elif filtro == "torre_piso_num":
            resultados = [f"Torre: {torresp[h]}, Piso: {pisosp[h]}, Departamento: {dptosp[h]}, Nombre: {nombresyapellidos[h]}, Habitantes: {habitantess[h]}, Compra: {fechasc[h]}, Venta: {fechasv[h]}, Cochera: {cocheras_p[h]}, Gym: {gyms[h]}, Sum: {sums[h]}, Consumo Sum: {dsums[h]}" for h in range(len(torresp)) if torresp[h] == torre and pisosp[h] == piso and dptosp[h] == ndpto]
        else:
            resultados = ["Seleccione un filtro."]
        with open("listado_prop.txt", "a") as archivo:
            for r in resultados:
                archivo.write(r + '\n')
        messagebox.showinfo("Listado", "\n".join(resultados) if resultados else "Sin resultados.")

    btn_listar = tk.Button(frame_listado_propietarios, text="Listar", command=listar, bg=griscuadros, fg=colortexto, font=("Arial", 12))
    btn_listar.pack(pady=10)
    btn_volver = tk.Button(frame_listado_propietarios, text="Volver", command=lambda: mostrar_frame(frame_propietarios), bg=colorvolver, fg="white", font=("Arial", 12))
    btn_volver.pack(pady=10)

def alta_cochera():
    for widget in frame_alta_cocheras.winfo_children():
        widget.destroy()

    alta_torre = tk.StringVar()
    alta_piso = tk.StringVar()
    alta_numero = tk.StringVar()
    alta_metros = tk.StringVar()
    alta_libre = tk.StringVar()

    crear_titulo(frame_alta_cocheras, "Alta Cochera")
    tk.Label(frame_alta_cocheras, text="Torre (A/B/C)", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    torre_frame = tk.Frame(frame_alta_cocheras, bg=grisfondo)
    tk.Radiobutton(torre_frame, text="A", variable=alta_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
    tk.Radiobutton(torre_frame, text="B", variable=alta_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
    tk.Radiobutton(torre_frame, text="C", variable=alta_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
    torre_frame.pack(pady=2)
    tk.Label(frame_alta_cocheras, text="Piso", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_cocheras, textvariable=alta_piso, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_alta_cocheras, text="Número", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_cocheras, textvariable=alta_numero, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_alta_cocheras, text="Metros Cubiertos", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_cocheras, textvariable=alta_metros, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_alta_cocheras, text="Libre (s/n)", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_alta_cocheras, textvariable=alta_libre, font=("Arial", 12)).pack(pady=2)

    def guardar_cochera():
        torre = alta_torre.get().upper()
        piso = alta_piso.get()
        ndpto = alta_numero.get()
        if torre not in ("A", "B", "C"):
            messagebox.showerror("Error", "Torre inválida.")
            return
        if any(torresc[i] == torre and pisosc[i] == piso and dptosc[i] == ndpto for i in range(len(torresc))):
            messagebox.showerror("Error", "La cochera ya existe.")
            return
        torresc.append(torre)
        pisosc.append(piso)
        dptosc.append(ndpto)
        mtcubiertossc.append(alta_metros.get())
        libres.append(alta_libre.get())
        messagebox.showinfo("Éxito", "Cochera cargada exitosamente.")
        frame_alta_cocheras.pack_forget()
        mostrar_frame(frame_cocheras)

    tk.Button(frame_alta_cocheras, text="Guardar", command=guardar_cochera, bg=griscuadros, fg=colortexto, font=("Arial", 12)).pack(pady=10)
    tk.Button(frame_alta_cocheras, text="Volver", command=lambda: mostrar_frame(frame_cocheras), bg=colorvolver, fg="white", font=("Arial", 12)).pack(pady=10)

def modificacion_cochera():
    for widget in frame_modificacion_cocheras.winfo_children():
        widget.destroy()

    mod_torre = tk.StringVar()
    mod_piso = tk.StringVar()
    mod_numero = tk.StringVar()
    opcion_mod = tk.StringVar()
    nuevo_valor = tk.StringVar()
    mod_index = [None]

    crear_titulo(frame_modificacion_cocheras, "Modificacion Cochera")
    tk.Label(frame_modificacion_cocheras, text="Torre (A/B/C)", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    torre_frame = tk.Frame(frame_modificacion_cocheras, bg=grisfondo)
    tk.Radiobutton(torre_frame, text="A", variable=mod_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
    tk.Radiobutton(torre_frame, text="B", variable=mod_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
    tk.Radiobutton(torre_frame, text="C", variable=mod_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
    torre_frame.pack(pady=2)
    tk.Label(frame_modificacion_cocheras, text="Piso", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_modificacion_cocheras, textvariable=mod_piso, font=("Arial", 12)).pack(pady=2)
    tk.Label(frame_modificacion_cocheras, text="Número", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack(pady=2)
    tk.Entry(frame_modificacion_cocheras, textvariable=mod_numero, font=("Arial", 12)).pack(pady=2)

    def buscar_modificar():
        torre = mod_torre.get().upper()
        piso = mod_piso.get()
        ndpto = mod_numero.get()
        for i in range(len(torresc)):
            if torresc[i] == torre and pisosc[i] == piso and dptosc[i] == ndpto:
                mod_index[0] = i
                frame_mod_opciones.pack()
                return
        messagebox.showerror("Error", "La cochera no existe.")

    tk.Button(frame_modificacion_cocheras, text="Buscar", command=buscar_modificar, bg=griscuadros, fg=colortexto, font=("Arial", 12)).pack(pady=10)

    frame_mod_opciones = tk.Frame(frame_modificacion_cocheras, bg=grisfondo)
    tk.Label(frame_mod_opciones, text="¿Qué desea modificar?", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    for campo in ["Metros Cubiertos", "Libre (s/n)"]:
        tk.Radiobutton(frame_mod_opciones, text=campo, variable=opcion_mod, value=campo, bg=grisfondo, fg=colorvolver, font=("Arial", 12)).pack(anchor="w")
    tk.Label(frame_mod_opciones, text="Nuevo valor:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    tk.Entry(frame_mod_opciones, textvariable=nuevo_valor, font=("Arial", 12)).pack()

    def modificar_cochera():
        i = mod_index[0]
        campo = opcion_mod.get()
        valor = nuevo_valor.get()
        if i is None:
            messagebox.showerror("Error", "Debe buscar una cochera primero.")
            return
        if campo == "Metros Cubiertos":
            mtcubiertossc[i] = valor
        elif campo == "Libre (s/n)":
            libres[i] = valor
        else:
            messagebox.showerror("Error", "Opción inválida.")
            return
        messagebox.showinfo("Éxito", "Modificación realizada.")
        frame_mod_opciones.pack_forget()
        frame_modificacion_cocheras.pack_forget()
        mostrar_frame(frame_cocheras)

    tk.Button(frame_mod_opciones, text="Modificar", command=modificar_cochera, bg=griscuadros, fg=colortexto, font=("Arial", 12)).pack(pady=10)
    tk.Button(frame_mod_opciones, text="Volver", command=lambda: frame_mod_opciones.pack_forget(), bg=colorvolver, fg="white", font=("Arial", 12)).pack(pady=10)
    tk.Button(frame_modificacion_cocheras, text="Volver", command=lambda: mostrar_frame(frame_cocheras), bg=colorvolver, fg="white", font=("Arial", 12)).pack(pady=10)

def consulta_cochera():
    for widget in frame_consulta_cocheras.winfo_children():
        widget.destroy()

    consulta_var = tk.StringVar()
    consulta_torre = tk.StringVar()
    consulta_entry2 = tk.Entry(frame_consulta_cocheras, font=("Arial", 12))
    consulta_entry3 = tk.Entry(frame_consulta_cocheras, font=("Arial", 12))

    crear_titulo(frame_consulta_cocheras, "Consulta Cochera")
    tk.Label(frame_consulta_cocheras, text="Filtrar por:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    tk.Radiobutton(frame_consulta_cocheras, text="Torre", variable=consulta_var, value="torre", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Radiobutton(frame_consulta_cocheras, text="Torre y Piso", variable=consulta_var, value="torre_piso", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Radiobutton(frame_consulta_cocheras, text="Torre, Piso y Número", variable=consulta_var, value="torre_piso_num", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Label(frame_consulta_cocheras, text="Torre:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    torre_frame = tk.Frame(frame_consulta_cocheras, bg=grisfondo)
    rb_torre_a = tk.Radiobutton(torre_frame, text="A", variable=consulta_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_b = tk.Radiobutton(torre_frame, text="B", variable=consulta_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_c = tk.Radiobutton(torre_frame, text="C", variable=consulta_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    torre_frame.pack(pady=2)
    rb_torre_a.pack(side=tk.LEFT, padx=10)
    rb_torre_b.pack(side=tk.LEFT, padx=10)
    rb_torre_c.pack(side=tk.LEFT, padx=10)
    tk.Label(frame_consulta_cocheras, text="Piso:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    consulta_entry2.pack()
    tk.Label(frame_consulta_cocheras, text="Número:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    consulta_entry3.pack()

    def consultar():
        filtro = consulta_var.get()
        torre = consulta_torre.get().upper()
        piso = consulta_entry2.get()
        ndpto = consulta_entry3.get()
        resultados = []
        if filtro == "torre":
            resultados = [f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Cochera: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}" for h in range(len(torresc)) if torresc[h] == torre]
        elif filtro == "torre_piso":
            resultados = [f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Cochera: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}" for h in range(len(torresc)) if torresc[h] == torre and pisosc[h] == piso]
        elif filtro == "torre_piso_num":
            resultados = [f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Cochera: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}" for h in range(len(torresc)) if torresc[h] == torre and pisosc[h] == piso and dptosc[h] == ndpto]
        else:
            resultados = ["Seleccione un filtro."]
        messagebox.showinfo("Consulta", "\n".join(resultados) if resultados else "Sin resultados.")

    tk.Button(frame_consulta_cocheras, text="Consultar", command=consultar, bg=griscuadros, fg=colortexto, font=("Arial", 12)).pack(pady=10)
    tk.Button(frame_consulta_cocheras, text="Volver", command=lambda: mostrar_frame(frame_cocheras), bg=colorvolver, fg="white", font=("Arial", 12)).pack(pady=10)

def listado_cochera():
    for widget in frame_listado_cocheras.winfo_children():
        widget.destroy()

    listado_var = tk.StringVar()
    listado_torre = tk.StringVar()
    listado_entry2 = tk.Entry(frame_listado_cocheras, font=("Arial", 12))
    listado_entry3 = tk.Entry(frame_listado_cocheras, font=("Arial", 12))

    crear_titulo(frame_listado_cocheras, "Listado Cocheras")
    tk.Label(frame_listado_cocheras, text="Filtrar por:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    tk.Radiobutton(frame_listado_cocheras, text="Torre", variable=listado_var, value="torre", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Radiobutton(frame_listado_cocheras, text="Torre y Piso", variable=listado_var, value="torre_piso", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Radiobutton(frame_listado_cocheras, text="Torre, Piso y Número", variable=listado_var, value="torre_piso_num", bg=grisfondo, fg=colortexto).pack(anchor="w")
    tk.Label(frame_listado_cocheras, text="Torre:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    torre_frame = tk.Frame(frame_listado_cocheras, bg=grisfondo)
    rb_torre_a = tk.Radiobutton(torre_frame, text="A", variable=listado_torre, value="A", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_b = tk.Radiobutton(torre_frame, text="B", variable=listado_torre, value="B", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_c = tk.Radiobutton(torre_frame, text="C", variable=listado_torre, value="C", bg=grisfondo, fg=colortexto, selectcolor=colorvolver, font=("Arial", 12))
    rb_torre_a.pack(side=tk.LEFT, padx=10)
    rb_torre_b.pack(side=tk.LEFT, padx=10)
    rb_torre_c.pack(side=tk.LEFT, padx=10)
    torre_frame.pack(pady=2)
    tk.Label(frame_listado_cocheras, text="Piso:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    listado_entry2.pack()
    tk.Label(frame_listado_cocheras, text="Número:", bg=grisfondo, fg=colortexto, font=("Arial", 12)).pack()
    listado_entry3.pack()

    def listar():
        filtro = listado_var.get()
        torre = listado_torre.get().upper()
        piso = listado_entry2.get()
        ndpto = listado_entry3.get()
        resultados = []
        if filtro == "torre":
            resultados = [f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Cochera: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}" for h in range(len(torresc)) if torresc[h] == torre]
        elif filtro == "torre_piso":
            resultados = [f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Cochera: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}" for h in range(len(torresc)) if torresc[h] == torre and pisos[h] == piso]
        elif filtro == "torre_piso_num":
            resultados = [f"Torre: {torresc[h]}, Piso: {pisosc[h]}, Cochera: {dptosc[h]}, Metros cubiertos: {mtcubiertossc[h]}, Libre: {libres[h]}" for h in range(len(torresc)) if torresc[h] == torre and pisos[h] == piso and dptosc[h] == ndpto]
        else:
            resultados = ["Seleccione un filtro."]
        with open("listado_coch.txt", "a") as archivo:
            for r in resultados:
                archivo.write(r + '\n')
        messagebox.showinfo("Listado", "\n".join(resultados) if resultados else "Sin resultados.")

    tk.Button(frame_listado_cocheras, text="Listar", command=listar, bg=griscuadros, fg=colortexto, font=("Arial", 12)).pack(pady=10)
    tk.Button(frame_listado_cocheras, text="Volver", command=lambda: mostrar_frame(frame_cocheras), bg=colorvolver, fg="white", font=("Arial", 12)).pack(pady=10)
    
def liquidacion():
    pagaeldobleA = 0
    pagaeldobleB = 0
    pagaeldobleC = 0

    luzzconsumida = []
    aguasconsumida = []
    gassconsumida = []
    dsumsconsumo = []
    impuestopcialdepas = []
    impuestopcialcochs = []
    pagannormaldepa = []
    pagandobledepa = []
    pagannormalcoch = []
    paga20pcientomascoch = []

    # Punto 1: Seguridad
    cantidaDeptosA = torres.count("A")
    cantidaDeptosB = torres.count("B")
    cantidaDeptosC = torres.count("C")
    seguridadA = 150000 / cantidaDeptosA if cantidaDeptosA else 0
    seguridadB = 150000 / cantidaDeptosB if cantidaDeptosB else 0
    seguridadC = 150000 / cantidaDeptosC if cantidaDeptosC else 0
    seguridadCocheraA = seguridadA / 2
    seguridadCocheraB = seguridadB / 2
    seguridadCocheraC = seguridadC / 2

    for i in range(len(mtcubiertoss)):
        if int(mtcubiertoss[i]) >= 100:
            torre = torres[i]
            if torre == "A":
                pagaeldobleA += seguridadA
            elif torre == "B":
                pagaeldobleB += seguridadB
            elif torre == "C":
                pagaeldobleC += seguridadC

    # Punto 2: Luz
    for i in luzz:
        kwconsumido = int(i) * 15000
        luzzconsumida.append(kwconsumido)

    # Punto 3: Agua
    for i in aguas:
        m3aguaconsumido = int(i) * 1000
        aguasconsumida.append(m3aguaconsumido)

    # Punto 4: Gas
    for i in gass:
        m3gasconsumido = int(i) * 5000
        gassconsumida.append(m3gasconsumido)

    # Punto 5: SUM
    sumtotal = sums.count("s") if sums.count("s") else 1
    sumconsumo = 80000 / sumtotal

    # Punto 6: Días de SUM
    for i in dsums:
        ddsumconsumo = int(i) * 40000
        dsumsconsumo.append(ddsumconsumo)

    # Punto 7: Impuesto especial
    for i in mtcubiertoss:
        impuestopcialdepa = int(i) * 400
        impuestopcialdepas.append(impuestopcialdepa)
    for i in mtcubiertossc:
        impuestopcialcoch = int(i) * 200
        impuestopcialcochs.append(impuestopcialcoch)

    # Punto 8: Pisos y cocheras
    for i in range(len(pisos)):
        if int(pisos[i]) < 5:
            pagannormaldepa.append(i)
        if int(pisos[i]) > 5:
            pagandobledepa.append(i)
    for h in range(len(torresc)):
        if h < len(torresp) and (torresc[h] != torresp[h] or pisosc[h] != pisosp[h] or dptosc[h] != dptosp[h]):
            pagannormalcoch.append(h)
        else:
            paga20pcientomascoch.append(h)

    # Punto 9: Agua común
    aguacomun = len(torresc) * 2000

    # Construcción del mensaje
    msg = ""
    msg += "\n--- Liquidación por Torre ---\n"
    msg += f"Torre A paga por seguridad:\n - Por departamento: {int(seguridadA)}\n - Por cochera: {int(seguridadCocheraA)}\n"
    msg += f"Torre B paga por seguridad:\n - Por departamento: {int(seguridadB)}\n - Por cochera: {int(seguridadCocheraB)}\n"
    msg += f"Torre C paga por seguridad (doble):\n - Por departamento: {int(seguridadC * 2)}\n - Por cochera: {int(seguridadCocheraC * 2)}\n"
    msg += "Departamentos mayores a 100m2 pagan el doble:\n"
    msg += f" - Torre A: {int(pagaeldobleA)}\n - Torre B: {int(pagaeldobleB)}\n - Torre C: {int(pagaeldobleC)}\n\n"

    msg += "--- Liquidación por Departamento ---\n"
    for i in range(len(torres)):
        msg += f"Depto {torres[i]} - {pisos[i]} - {dptos[i]}\n"
        agua = aguasconsumida[i]
        gas = gassconsumida[i]
        luz = luzzconsumida[i]
        impuesto = impuestopcialdepas[i]
        dias_sum = dsumsconsumo[i]
        uso_sum = int(sumconsumo) if sums[i] == "s" else 0
        if torres[i] == "A":
            luz_comun = seguridadA
        elif torres[i] == "B":
            luz_comun = seguridadB
        else:
            luz_comun = seguridadC * 2
            uso_sum = uso_sum * 2
        total = agua + gas + luz + impuesto + uso_sum + dias_sum + luz_comun
        msg += f"  Agua: {agua}\n  Gas: {gas}\n  Luz: {luz}\n  Impuesto especial: {impuesto}\n  SUM: {uso_sum}\n  Días de SUM: {dias_sum}\n  Luz común: {int(luz_comun)}\n  Total a pagar: {int(total)}\n\n"

    msg += "--- Liquidación por Cochera ---\n"
    for i in range(len(torresc)):
        msg += f"Cochera {torresc[i]} - {pisosc[i]} - {dptosc[i]}\n"
        impuesto = impuestopcialcochs[i]
        if torresc[i] == "A":
            seguridad = seguridadCocheraA
        elif torresc[i] == "B":
            seguridad = seguridadCocheraB
        else:
            seguridad = seguridadCocheraC * 2
        total = impuesto + seguridad
        msg += f"  Impuesto especial: {impuesto}\n  Seguridad: {int(seguridad)}\n  Total a pagar: {int(total)}\n\n"

    msg += "Agua común: " + str(aguacomun) + "\n"

    messagebox.showinfo("Liquidación", msg)

root.mainloop()