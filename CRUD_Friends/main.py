import tkinter as tk
from tkinter import messagebox
import os

ARCHIVO = "friendsContact.txt"

def crear():

    nombre = txtNombre.get().strip()
    numero = txtNumero.get().strip()

    if nombre == "" or numero == "":
        messagebox.showwarning("Advertencia", "Complete todos los campos.")
        return

    if not os.path.exists(ARCHIVO):
        open(ARCHIVO, "w").close()

    with open(ARCHIVO, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")
            if len(datos) >= 2 and datos[0].lower() == nombre.lower():
                messagebox.showinfo("Mensaje",
                                    f"The friend {nombre} already exists.")
                return

    with open(ARCHIVO, "a") as archivo:
        archivo.write(f"{nombre};{numero}\n")

    messagebox.showinfo("Mensaje",
                        f"The friend {nombre} was added successfully.")

    limpiar()

def leer():

    nombre = txtNombre.get().strip()

    if nombre == "":
        messagebox.showwarning("Advertencia",
                               "Enter the friend's name.")
        return

    if not os.path.exists(ARCHIVO):
        messagebox.showinfo("Mensaje",
                            "No friends have been registered.")
        return

    encontrado = False

    with open(ARCHIVO, "r") as archivo:
        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) >= 2 and datos[0].lower() == nombre.lower():

                txtNumero.delete(0, tk.END)
                txtNumero.insert(0, datos[1])

                encontrado = True
                break

    if not encontrado:
        messagebox.showinfo(
            "Mensaje",
            f"The friend {nombre} does not exists."
        )

def actualizar():

    nombre = txtNombre.get().strip()
    numero = txtNumero.get().strip()

    if nombre == "" or numero == "":
        messagebox.showwarning("Advertencia", "Complete todos los campos.")
        return

    if not os.path.exists(ARCHIVO):
        messagebox.showinfo("Mensaje", "No friends have been registered.")
        return

    actualizado = False
    registros = []

    with open(ARCHIVO, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")

            if len(datos) >= 2:
                if datos[0].lower() == nombre.lower():
                    registros.append(f"{nombre};{numero}\n")
                    actualizado = True
                else:
                    registros.append(linea)

    if actualizado:
        with open(ARCHIVO, "w") as archivo:
            archivo.writelines(registros)

        messagebox.showinfo(
            "Mensaje",
            f"The friend's number of {nombre} was updated successfully."
        )

        limpiar()

    else:
        messagebox.showinfo(
            "Mensaje",
            f"The friend {nombre} does not exist."
        )

def eliminar():

    nombre = txtNombre.get().strip()

    if nombre == "":
        messagebox.showwarning("Advertencia", "Enter the friend's name.")
        return

    if not os.path.exists(ARCHIVO):
        messagebox.showinfo("Mensaje", "No friends have been registered.")
        return

    eliminado = False
    registros = []

    with open(ARCHIVO, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")

            if len(datos) >= 2:
                if datos[0].lower() == nombre.lower():
                    eliminado = True
                else:
                    registros.append(linea)

    if eliminado:
        with open(ARCHIVO, "w") as archivo:
            archivo.writelines(registros)

        messagebox.showinfo(
            "Mensaje",
            f"The friend {nombre} was deleted successfully."
        )

        limpiar()

    else:
        messagebox.showinfo(
            "Mensaje",
            f"The friend {nombre} does not exist."
        )

def limpiar():
    txtNombre.delete(0, tk.END)
    txtNumero.delete(0, tk.END)
    txtNombre.focus()

def salir():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Friends")
ventana.geometry("620x320")
ventana.configure(bg="#d9ecff")
ventana.resizable(False, False)


frame = tk.Frame(ventana, padx=20, pady=20)
frame.pack(fill="both", expand=True)

titulo = tk.Label(
    frame,
    text="FRIENDS CONTACT MANAGER",
    font=("Arial", 16, "bold"),
    fg="navy"
)
titulo.grid(row=0, column=0, columnspan=4, pady=10)



lblNombre = tk.Label(frame, text="Name", font=("Arial",11))
lblNombre.grid(row=1,column=0,pady=10,sticky="w")

txtNombre = tk.Entry(frame,width=40,font=("Arial",11))
txtNombre.grid(row=1,column=1,columnspan=4,padx=10)



lblNumero = tk.Label(frame,text="Number",font=("Arial",11))
lblNumero.grid(row=2,column=0,pady=10,sticky="w")

txtNumero = tk.Entry(frame,width=40,font=("Arial",11))
txtNumero.grid(row=2,column=1,columnspan=4,padx=10)




btnCrear = tk.Button(frame,text="Create",width=10,command=crear)
btnCrear.grid(row=3,column=0,pady=15)

btnLeer = tk.Button(frame,text="Read",width=10,command=leer)
btnLeer.grid(row=3,column=1)

btnActualizar = tk.Button(frame,text="Update",width=10,command=actualizar)
btnActualizar.grid(row=3,column=2)

btnEliminar = tk.Button(frame,text="Delete",width=10,command=eliminar)
btnEliminar.grid(row=3,column=3)




btnLimpiar = tk.Button(frame,text="Clear",width=10,command=limpiar)
btnLimpiar.grid(row=4,column=1,pady=15)

btnSalir = tk.Button(frame,text="Exit",width=10,command=salir)
btnSalir.grid(row=4,column=2)


ventana.mainloop()