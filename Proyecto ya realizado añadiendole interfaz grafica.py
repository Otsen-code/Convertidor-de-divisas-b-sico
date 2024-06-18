from customtkinter import *
from tkinter import *

#logo = PhotoImage(file= '')

app = CTk()
app.title("Convertidor de divisas")
app.geometry("500x600")

set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green



def btn_function():
    #label.configure(text="Bienvenido al programa")
    #label.configure(text=f'Bienvenido al programa {Entry.get()} ') 
    Entry.delete(0,END)
    Entry.configure(state="disabled")
                
    if (checkvar.get() == "on") and (checkvar2.get() == "on"):
        label.configure(text="Selecciono ambas opciones")
    
    else: label.configure(text=f'Bienvenido al programa {Entry.get()} ')
    
def clear():
    Entry.configure(state="normal")
    label.configure(text="") 
    mycheck.deselect()
    mycheck2.deselect()
    label2.configure(text="")
    
    
    """
    def btn_function():
    print(label2)
    label2.place(relx= 0.5, rely=0.4, anchor="center")
    label.place_forget()
    """

         
#Entrada del usuario
    
Entry = CTkEntry(app, placeholder_text="Ingrese aqui la cantidad")
Entry.place(relx= 0.5, rely=0.6, anchor="center")

#Botones

btn = CTkButton(master=app, command=btn_function, text="Convertir", corner_radius=32, fg_color="#4158D0", hover_color="#C850C0", border_width=2 ,border_color="black")
btn.place(relx= 0.5, rely=0.5, anchor="center")

btn2 = CTkButton(master=app, command=clear, text="Nueva cantidad", corner_radius=32, fg_color="#4158D0", hover_color="#C850C0", border_width=2 ,border_color="black")
btn2.place(relx= 0.5, rely=0.7, anchor="center")

#Etiquetas

label = CTkLabel (master=app, text="", font=("Arial",20))
label.place(relx= 0.5, rely=0.4, anchor="center")

label2 = CTkLabel(master=app, text="lol", font=("Arial",20))
label2.place(relx= 0.5, rely=0.1, anchor="center")

#Check box botones de validar
checkvar = StringVar(value="off")
mycheck = CTkCheckBox(app, text="De dolares a pesos Dominicanos" , variable=checkvar, onvalue="on", offvalue="off" )
mycheck.place(relx= 0.5, rely=0.3, anchor="center")

checkvar2 = StringVar(value="off")
mycheck2 = CTkCheckBox(app, text="De pesos dominicanos a dolares" , variable=checkvar2, onvalue="on", offvalue="off" )
mycheck2.place(relx= 0.5, rely=0.2, anchor="center")

app.mainloop()