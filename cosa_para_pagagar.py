from tkinter import *
from tkinter import messagebox
interfaz=Tk()

def cambio():
    precioaux=precio.get()
    pagoaux=pago.get()
    cambioaux=pagoaux-precioaux
    faltanteaux=precioaux-pagoaux

    if cambioaux<0:
        messagebox.showinfo(title="ejercicio 2", message="falta dinero en el pago... el dinero faltante es:" + str(faltanteaux))
    elif cambioaux==0:
        messagebox.showinfo(title="ejercicio 2", message="se a pagado exacto no es necesario dar cambio"  )
    elif cambioaux>0:
        messagebox.showinfo(title="ejercicio 2", message="el cambio a dar es:" + str(cambioaux))
#creando el tamaño de ña ventana
interfaz.geometry("500x300+100+100")
interfaz.title("programa de cambio XD")#titulo del la ventana XD

titulolbl=Label(text="Cuanto cambio dar en un programa", font=("arial black,",14)).pack()
ingreselbl=Label(text="Ingrese el precio del articulo:", font=("comic sans ms",12)).place(x=10, y=40)
precio=DoubleVar()
ingresar=Entry(interfaz,textvariable=precio).place(x=270, y=48)

ingrese2lbl=Label(text="Cuanto pago el cliente:", font=("comic sans ms",12)).place(x=10, y=70)
pago=DoubleVar()
ingresar2=Entry(interfaz,textvariable=pago).place(x=270, y=78)

btnboton=Button(interfaz,text="calcular",command=cambio, font=("comic sans ms",12)).place(x=10,y=110)


interfaz.mainloop()







"""
pre=float(input("ingrese el precio del articulo:"))
pag=float(input("cuanto a pagado el cliente:"))

cambio=pag-pre
faltante=pre-pag

if cambio<0:
    print("falta dinero en el pago... el dinero faltante es:", faltante)
elif cambio==0:
    print("se a pagado exacto no es necesario dar cambio")
elif cambio>0:
    print("el cambio a dar es:", cambio)
"""