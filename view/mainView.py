from controller.controlador import *
from tkinter import *
from customtkinter import *
from PIL import Image
from tkinter import messagebox
from tkinter import ttk


ce = "#00790B" #color para buscar o enviar
cd = "#790000" #color delete
cp = "#efcead" #color primario
cs = "#744c24" #color secundario

class Menu():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.pantalla.config(bg=cp)
        self.pantalla.geometry("300x500")
        self.controlador = ControladorG()

        img = CTkImage(light_image=Image.open("view/img/fondo.jpg"), size=(300, 500))
        lbl_img = CTkLabel(pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        menuTitle = Label(self.pantalla, text="Panaderia SUS", bg=cs, fg="white", width="40", height="3", font="1")
        menuTitle.pack(pady=15, padx=10)

        #Botones

        btn1 = CTkButton(self.pantalla, text="Insumos", fg_color=cs,command=self.insu, height=35)
        btn1.place(x=79, y=300)
        btn2 = CTkButton(self.pantalla, text="Panes", fg_color=cs,command=self.pan, height=35)
        btn2.place(x=79, y=345)
        btn3 = CTkButton(self.pantalla, text="Insumos de Panes", fg_color=cs,command=self.insu_pan, height=35)
        btn3.place(x=79, y=390)
        btn3 = CTkButton(self.pantalla, text="Unidades", fg_color=cs,command=self.uni, height=35)
        btn3.place(x=79, y=435)

        btn_exit= CTkButton(self.pantalla, text="Salir", command=self.salir, height=25, width=20, fg_color=cs)
        btn_exit.place(x= 258, y= 472)


    def insu(self):
        self.limpiar_ventana()
        Insumos(self.pantalla)

    def pan(self):
        self.limpiar_ventana()
        Panes(self.pantalla)

    def insu_pan(self):
        self.limpiar_ventana()
        InsuPanes(self.pantalla)

    def uni(self):
        self.limpiar_ventana()
        Unidades(self.pantalla)

    def limpiar_ventana(self):
        for widget in self.pantalla.winfo_children():
            widget.destroy()

    def volver_menu(self):
        self.limpiar_ventana()
        Menu(self.pantalla)
    
    def volverTpl(self):
        self.pantalla.deiconify()
        self.toplevel.destroy()

    def salir(self):
        respuesta = messagebox.askquestion("Salir", "¿Estás seguro que quieres salir?")
        if respuesta == "yes":
            self.pantalla.destroy()


class Insumos(Menu):
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.pantalla.title("Insumos")
        self.pantalla.geometry("800x400")
        self.pantalla.resizable(width=False, height=False)
        self.controlador = ControladorG()
        img = CTkImage(light_image=Image.open("view/img/fondo3.jpg"), size=(800, 400))
        lbl_img = CTkLabel(pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        menuTitle = Label(self.pantalla, text="Insumos", bg=cs, fg="white", width="85", height="3", font="1")
        menuTitle.pack(pady=15, padx=5)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background=cs, relief="flat")
        style.map("Treeview.Heading", background=[('active',cs)])

        self.grid = ttk.Treeview( columns=("#1","#2","#3","#4","#5"), show="headings")
        self.grid.place(x=175, y=100, width=600, height=240)

        self.grid.column("#0", width=0, anchor=CENTER)
        self.grid.column("#1",width=30, anchor=CENTER)
        self.grid.column("#2",width=45, anchor=CENTER)
        self.grid.column("#3",width=35, anchor=CENTER)
        self.grid.column("#4",width=35, anchor=CENTER)
        self.grid.column("#5",width=45, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("#1", text="Descripcion", anchor=CENTER)
        self.grid.heading("#2", text="Unidad de medida", anchor=CENTER)
        self.grid.heading("#3", text="Existencia min", anchor=CENTER)
        self.grid.heading("#4", text="Existencia max", anchor=CENTER)
        self.grid.heading("#5", text="Cantidad disponible", anchor=CENTER)

        sano= self.grid.get_children()
        for element in sano:
            self.grid.delete(element)

        data,i=self.controlador.ver_insumos(),-1
        for loca in data:
            self.grid.insert('',i, text=loca[0], values=(loca[1], loca[2], loca[3], loca[4], loca[5]))
    
        self.txtHar = CTkEntry(self.pantalla, placeholder_text="Buscar")
        self.txtHar.place(x=25, y=105)
        self.btnBuscar = CTkButton(self.pantalla, text="Buscar", command=self.busquelo, height=30, fg_color=ce)
        self.btnBuscar.place(x=25, y=145)

        btn_agregar= CTkButton(self.pantalla, text="Agregar", command=self.nuevoInsumo, fg_color=cs,height=40)
        btn_agregar.place(x=25, y=188)
        btn_actualizar= CTkButton(self.pantalla, text="Actualizar",command=self.actualizarInsumo, fg_color=cs,height=40)
        btn_actualizar.place(x=25, y=243)
        btn_eliminar= CTkButton(self.pantalla, text="Eliminar", command=self.delete, fg_color=cd,height=40)
        btn_eliminar.place(x=25, y=298)
        btn_volver= CTkButton(self.pantalla, text="Volver", command=self.volver_menu, fg_color=cs ,height=25, width=20)
        btn_volver.place(x=740, y=365)

    def busquelo(self):
        if self.txtHar.get() == "":
            messagebox.showerror(message=f"Campo vacio, Ingrese un dato", title="Error")
        else:
            if self.controlador.buscar_insumos(self.txtHar.get())!=[]:
                data=self.controlador.buscar_insumos(self.txtHar.get())
                sano= self.grid.get_children()
                for element in sano:
                    self.grid.delete(element)
                i=-1
                for loca in data:
                    self.grid.insert('',i, text=loca[0], values=(loca[1], loca[2], loca[3], loca[4], loca[5]))
            else:
                messagebox.showerror(message=f"No se encuentra '{self.txtHar.get()}' ", title="Error")
                
    def delete(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Debe seleccionar un campo", title="Error")
        else:
            respuesta = messagebox.askquestion("Eliminar", "¿Estás seguro que deseas eliminar este campo?")
            if respuesta == "yes":
                if self.controlador.eliminar_insumos(self.sisas)=="Eliminado":
                    messagebox.showinfo(message="Eliminado con exito", title="Info")
                    self.limpiar_ventana()
                    Insumos(self.pantalla)
                else:
                    messagebox.showerror(message="Error al eliminar", title="Error")


    def actualizarInsumo(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas== "":
            messagebox.showerror(message=f"Campo vacio, Ingrese un dato", title="Error")
        else:
            self.pantalla.withdraw()
            self.toplevel = CTkToplevel(self.pantalla)
            self.toplevel.geometry("300x400")
            self.toplevel.resizable(False, False)
            self.toplevel.config(background=cp)

            menuTitle = Label(self.toplevel, text="Agregar Insumo", bg=cs, fg="white", width="30", height="3", font="1")
            menuTitle.pack(padx=3, pady=5)

            CTkLabel(self.toplevel, text="", bg_color=cp).pack(pady=5)

            self.entryDescripcion = CTkEntry(self.toplevel, placeholder_text="Descripcion")
            self.entryDescripcion.pack(padx=1, pady=5)  
            self.entryUnidadMedida = CTkComboBox(self.toplevel, values=self.llenar_combo_insumos(), state="readonly")
            self.entryUnidadMedida.set("Unidad De Medida")
            self.entryUnidadMedida.pack(padx=1, pady=5)
            self.entryExistenciaMinima = CTkEntry(self.toplevel, placeholder_text="Existencia minima")
            self.entryExistenciaMinima.pack(padx=1, pady=5)  
            self.entryExistenciaMaxima = CTkEntry(self.toplevel, placeholder_text="Existencia Maxima")
            self.entryExistenciaMaxima.pack(padx=1, pady=5) 
            self.entryCantidad = CTkEntry(self.toplevel, placeholder_text="Cantidad")
            self.entryCantidad.pack(padx=1, pady=5) 

            btnSend = CTkButton(self.toplevel, text="Enviar", command=self.actulInsumo, fg_color=cs,height=40)
            btnSend.pack(padx=1, pady=5)

            btn_volver= CTkButton(self.toplevel, text="Volver", command=self.volverTpl, fg_color=cs ,height=25, width=20)
            btn_volver.place(x=245, y=370)
    
    def actulInsumo(self):
        if self.controlador.actualizar_insumos(self.sisas, self.entryDescripcion.get(),self.entryUnidadMedida.get(),self.entryExistenciaMinima.get(),self.entryExistenciaMaxima.get(),self.entryCantidad.get()):
            messagebox.showinfo(message="Actualizado con exito")
            self.pantalla.deiconify()
            self.limpiar_ventana()
            Insumos(self.pantalla)
            self.toplevel.destroy()
        else:
            messagebox.showerror(message="Error al actualizar")
            


    def nuevoInsumo(self):
        self.pantalla.withdraw()
        self.toplevel = CTkToplevel(self.pantalla)
        self.toplevel.geometry("300x400")
        self.toplevel.resizable(False, False)
        self.toplevel.config(background=cp)

        menuTitle = Label(self.toplevel, text="Agregar Insumo", bg=cs, fg="white", width="30", height="3", font="1")
        menuTitle.pack(padx=3, pady=5)

        CTkLabel(self.toplevel, text="", bg_color=cp).pack(pady=5)

        self.entryDescripcion = CTkEntry(self.toplevel, placeholder_text="Descripcion")
        self.entryDescripcion.pack(padx=1, pady=5)  
        self.entryUnidadMedida = CTkComboBox(self.toplevel, values=self.llenar_combo_insumos(), state="readonly")
        self.entryUnidadMedida.set("Unidad De Medida")
        self.entryUnidadMedida.pack(padx=1, pady=5)
        self.entryExistenciaMinima = CTkEntry(self.toplevel, placeholder_text="Existencia minima")
        self.entryExistenciaMinima.pack(padx=1, pady=5)  
        self.entryExistenciaMaxima = CTkEntry(self.toplevel, placeholder_text="Existencia Maxima")
        self.entryExistenciaMaxima.pack(padx=1, pady=5) 
        self.entryCantidad = CTkEntry(self.toplevel, placeholder_text="Cantidad")
        self.entryCantidad.pack(padx=1, pady=5) 

        btnSend = CTkButton(self.toplevel, text="Enviar", command=self.enviarInsumo, fg_color=cs,height=40)
        btnSend.pack(padx=1, pady=5)

        btn_volver= CTkButton(self.toplevel, text="Volver", command=self.volverTpl, fg_color=cs ,height=25, width=20)
        btn_volver.place(x=245, y=370)

    def enviarInsumo(self):
        validacion = self.controlador.insertar_insumos(self.entryDescripcion.get(),self.entryUnidadMedida.get(),self.entryExistenciaMinima.get(),self.entryExistenciaMaxima.get(),self.entryCantidad.get())
        if validacion == "Insertado":
            messagebox.showinfo(message="Registro con exito")
            self.pantalla.deiconify()
            self.limpiar_ventana()
            Insumos(self.pantalla)
            self.toplevel.destroy()
        else:
            messagebox.showerror(message="Error al regisrar el insumo", title="Error")

    def llenar_combo_insumos(self):
        #Invoca en el controlador el método de consultar todos los clientes
        valores = self.controlador.ver_unidades()
        #Crea la lista de valores a partir del juego de registros devuelto
        valores_combo = [str(result[0])+'-'+result[1] for result in valores]
        return valores_combo      

    def volverTpl(self):
        self.pantalla.deiconify()
        self.toplevel.destroy()

class Panes(Menu):
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.pantalla.title("Panes")
        self.pantalla.geometry("600x400")
        self.pantalla.resizable(width=False, height=False)
        self.controlador = ControladorG()
        img = CTkImage(light_image=Image.open("view/img/fondo2.jpg"), size=(600, 400))
        lbl_img = CTkLabel(pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        menuTitle = Label(self.pantalla, text="Agregar Pan", bg=cs, fg="white", width="62", height="3", font="1")
        menuTitle.place(x=25, y=20)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background=cs, relief="flat")
        style.map("Treeview.Heading", background=[('active',cs)])

        self.grid = ttk.Treeview( columns=("#1"), show="headings")
        self.grid.column("#0", width=5, anchor=CENTER)
        self.grid.column("#1",width=90, anchor=CENTER)
        
        self.grid.heading("#0", text="ID",anchor=CENTER)
        self.grid.heading("#1", text="Panes", anchor=CENTER)
        self.grid.place(x=250, y=100, width=200, height=250)

        sano= self.grid.get_children()
        for element in sano:
            self.grid.delete(element)

        data,i=self.controlador.ver_panes(),-1
        for loca in data:
            self.grid.insert('',i, text=loca[0], values=(loca[1]))

        self.txtHar = CTkEntry(self.pantalla, placeholder_text="Buscar")
        self.txtHar.place(x=50, y=100)
        self.btnBuscar = CTkButton(self.pantalla, text="Buscar", command=self.buscarPan, height=30, fg_color=ce)
        self.btnBuscar.place(x=50, y=145)
        btn_agregar= CTkButton(self.pantalla, text="Agregar", command=self.nuevoPan, fg_color=cs,height=40)
        btn_agregar.place(x=50, y=190)
        btn_actualizar= CTkButton(self.pantalla, text="Actualizar", command=self.editarPan, fg_color=cs,height=40)
        btn_actualizar.place(x=50, y=250)
        btn_eliminar= CTkButton(self.pantalla, text="Eliminar", command=self.eliminarPan, fg_color=cd,height=40)
        btn_eliminar.place(x=50, y=310)
        btn_volver= CTkButton(self.pantalla, text="Volver", command=self.volver_menu, fg_color=cs ,height=25, width=20)
        btn_volver.place(x=540, y=360)

    def buscarPan(self):
        if self.txtHar.get() == "":
            messagebox.showerror(message=f"Campo vacio, Ingrese un dato", title="Error")
        else:
            if self.controlador.buscar_panes(self.txtHar.get())!=[]:
                data=self.controlador.buscar_panes(self.txtHar.get())
                sano= self.grid.get_children()
                for element in sano:
                    self.grid.delete(element)

                i=-1
                for loca in data:
                    self.grid.insert('',i, text=loca[0], values=(loca[1]))
            else:
                messagebox.showerror(message=f"No se encuentra '{self.txtHar.get()}' ", title="Error")
        

    def editarPan(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Debe seleccionar un campo", title="Error")
        else:
            self.pantalla.withdraw()
            self.toplevel = CTkToplevel(self.pantalla)
            self.toplevel.geometry("300x200")
            self.toplevel.resizable(False, False)
            self.toplevel.config(background=cp)

            menuTitle = Label(self.toplevel, text="Editar Pan", bg=cs, fg="white", width="30", height="3", font="1")
            menuTitle.pack(padx=3, pady=5)

            self.entryDescripcion = CTkEntry(self.toplevel, placeholder_text="Descripcion")
            self.entryDescripcion.pack(padx=1, pady=10) 
            
            btnSend = CTkButton(self.toplevel, text="Actualizar", command=self.editPan, fg_color=ce,height=40)
            btnSend.pack(padx=1, pady=10)

            btn_volver= CTkButton(self.toplevel, text="Volver", command=self.volverTpl, fg_color=cs ,height=25, width=20)
            btn_volver.place(x=245, y=170)
    
    def editPan(self):
        if self.controlador.actualizar_panes(self.sisas, self.entryDescripcion.get())=="Actualizado":
            messagebox.showerror(message="Error al actualizar", title="Error")
            self.pantalla.deiconify()
            self.limpiar_ventana()
            Panes(self.pantalla)
            self.toplevel.destroy()
        else:
            messagebox.showinfo(message="Actualizado con exito")
            self.pantalla.deiconify()
            self.limpiar_ventana()
            Panes(self.pantalla)
            self.toplevel.destroy()


            
    def eliminarPan(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Debe seleccionar un campo", title="Error")
        else:
            respuesta = messagebox.askquestion("Eliminar", "¿Estás seguro que deseas eliminar este campo?")
            if respuesta == "yes":
                if self.controlador.eliminar_panes(self.sisas):
                    messagebox.showerror(message="Error al eliminar", title="Error")
                else:
                    messagebox.showinfo(message="Eliminado con exito")
                    self.limpiar_ventana()
                    Panes(self.pantalla)


    def nuevoPan(self):
        self.pantalla.withdraw()
        self.toplevel = CTkToplevel(self.pantalla)
        self.toplevel.geometry("300x200")
        self.toplevel.resizable(False, False)
        self.toplevel.config(background=cp)

        menuTitle = Label(self.toplevel, text="Agregar Pan", bg=cs, fg="white", width="30", height="3", font="1")
        menuTitle.pack(padx=3, pady=5)

        self.entryDescripcion = CTkEntry(self.toplevel, placeholder_text="Descripcion")
        self.entryDescripcion.pack(padx=1, pady=10) 
        
        btnSend = CTkButton(self.toplevel, text="Enviar", command=self.enviarPan, fg_color=ce,height=40)
        btnSend.pack(padx=1, pady=10)

        btn_volver= CTkButton(self.toplevel, text="Volver", command=self.volverTpl, fg_color=cs ,height=25, width=20)
        btn_volver.place(x=245, y=170)

    def enviarPan(self):
        if self.controlador.insertar_panes(self.entryDescripcion.get())=="Insertado":
            messagebox.showinfo(message=f"'{self.entryDescripcion.get()}' agregado con exito")
            self.pantalla.deiconify()
            self.limpiar_ventana()
            Panes(self.pantalla)
            self.toplevel.destroy()
        else:
            messagebox.showerror(message=f"No se pudo agregar '{self.entryDescripcion.get()}' al inventario")

class InsuPanes(Menu):
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.pantalla.title("insumo de Panes")
        self.pantalla.geometry("600x400")
        self.pantalla.resizable(width=False, height=False)
        self.controlador = ControladorG()
        img = CTkImage(light_image=Image.open("view/img/fondo2.jpg"), size=(600, 400))
        lbl_img = CTkLabel(pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        menuTitle = Label(self.pantalla, text="Agregar Insumos", bg=cs, fg="white", width="62", height="3", font="1")
        menuTitle.place(x=25, y=20)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background=cs, relief="flat")
        style.map("Treeview.Heading", background=[('active',cs)])

        self.grid = ttk.Treeview( columns=("#1","#2","#3","#4"), show="headings")
        self.grid.column("#0", width=5, anchor=CENTER)
        self.grid.column("#1",width=10, anchor=CENTER)
        self.grid.column("#2",width=10, anchor=CENTER)
        self.grid.column("#3",width=10, anchor=CENTER)
        self.grid.column("#4",width=10, anchor=CENTER)
        self.grid.heading("#0", text="ID",anchor=CENTER)
        self.grid.heading("#1", text="ID Pan", anchor=CENTER)
        self.grid.heading("#2", text="ID Insumo", anchor=CENTER)
        self.grid.heading("#3", text="Cantidad", anchor=CENTER)
        self.grid.heading("#4", text="Medida", anchor=CENTER)
        self.grid.place(x=250, y=100, width=270, height=250)

        sano= self.grid.get_children()
        for element in sano:
            self.grid.delete(element)

        data,i=self.controlador.ver_pan_insumo(),-1
        for loca in data:
            self.grid.insert('',i, text=loca[0], values=(loca[1], loca[2], loca[3], loca[4]))

        self.txtHar = CTkEntry(self.pantalla, placeholder_text="Buscar")
        self.txtHar.place(x=50, y=100)
        self.btnBuscar = CTkButton(self.pantalla, text="Buscar", command=self.buscarinsuPan, height=30, fg_color=ce)
        self.btnBuscar.place(x=50, y=145)
        btn_agregar= CTkButton(self.pantalla, text="Agregar", command=self.nuevoInsuPan, fg_color=cs,height=40)
        btn_agregar.place(x=50, y=190)
        btn_actualizar= CTkButton(self.pantalla, text="Actualizar", command=self.actualizarInsuPan, fg_color=cs,height=40)
        btn_actualizar.place(x=50, y=250)
        btn_eliminar= CTkButton(self.pantalla, text="Eliminar", command=self.eliminarInsuPan, fg_color=cd,height=40)
        btn_eliminar.place(x=50, y=310)
        btn_volver= CTkButton(self.pantalla, text="Volver", command=self.volver_menu, fg_color=cs ,height=25, width=20)
        btn_volver.place(x=545, y=370)

    def buscarinsuPan(self):
        if self.txtHar.get() == "":
            messagebox.showerror(message=f"Campo vacio, Ingrese un dato", title="Error")
        else:
            if self.controlador.buscar_pan_insumo(self.txtHar.get())!=[]:
                data=self.controlador.buscar_pan_insumo(self.txtHar.get())
                sano= self.grid.get_children()
                for element in sano:
                    self.grid.delete(element)

                i=-1
                for loca in data:
                    self.grid.insert('',i, text=loca[0], values=(loca[1], loca[2], loca[3], loca[4]))
            else:
                messagebox.showerror(message=f"No se encuentra '{self.txtHar.get()}' ", title="Error")

    def actualizarInsuPan(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Debe seleccionar un campo", title="Error")
        else:
            self.pantalla.withdraw()
            self.toplevel = CTkToplevel(self.pantalla)
            self.toplevel.geometry("300x400")
            self.toplevel.resizable(False, False)
            self.toplevel.config(background=cp)

            menuTitle = Label(self.toplevel, text="Actualizar InsuPan", bg=cs, fg="white", width="30", height="3", font="1")
            menuTitle.pack(padx=3, pady=5)

            CTkLabel(self.toplevel, text="", bg_color=cp).pack(pady=5)
    
            self.entryIDpan = CTkComboBox(self.toplevel, values=self.llenar_combo_idpan(), state="readonly")
            self.entryIDpan.set("ID Pan")
            self.entryIDpan.pack(padx=1, pady=5)

            self.entryIDinsumo = CTkComboBox(self.toplevel, values=self.llenar_combo_idinsumo(), state="readonly")
            self.entryIDinsumo.set("ID Insumo")
            self.entryIDinsumo.pack(padx=1, pady=5)

            self.entryCantidad = CTkEntry(self.toplevel, placeholder_text="Cantidad")
            self.entryCantidad.pack(padx=1, pady=5)

            self.entryIDmedida = CTkComboBox(self.toplevel, values=self.llenar_combo_idmedida(), state="readonly")
            self.entryIDmedida.set("ID Medida")
            self.entryIDmedida.pack(padx=1, pady=5)

            btnSend = CTkButton(self.toplevel, text="Actualizar", command=self.editInsuPan, fg_color=cs,height=40)
            btnSend.pack(padx=1, pady=5)

            btn_volver= CTkButton(self.toplevel, text="Volver", command=self.volverTpl, fg_color=cs ,height=25, width=20)
            btn_volver.place(x=245, y=370)

    def editInsuPan(self):
        if self.controlador.actualizar_pan_insumo(self.sisas, self.entryIDpan.get(), self.entryIDinsumo.get(), self.entryCantidad.get(), self.entryIDmedida.get()) == "Actualizado":
            messagebox.showinfo(message="Actualizado con exito")
            self.pantalla.deiconify()
            self.limpiar_ventana()
            InsuPanes(self.pantalla)
            self.toplevel.destroy()
        else:
            messagebox.showerror(message="Error al Actualizar el InsuPan", title="Error")

    
    def eliminarInsuPan(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas== "":
            messagebox.showerror(message="Debe seleccionar un campo", title="Error")
        else:
            respuesta = messagebox.askquestion("Eliminar", "¿Estás seguro que deseas eliminar este campo?")
            if respuesta == "yes":
                if self.controlador.eliminar_pan_insumo(self.sisas):
                    messagebox.showerror(message="Error al eliminar el InsuPan", title="Error")
                    self.limpiar_ventana()
                    InsuPanes(self.pantalla)
                else:
                    messagebox.showinfo(message="Eliminado con exito")
                    self.limpiar_ventana()
                    InsuPanes(self.pantalla)




    def nuevoInsuPan(self):
        self.pantalla.withdraw()
        self.toplevel = CTkToplevel(self.pantalla)
        self.toplevel.geometry("300x400")
        self.toplevel.resizable(False, False)
        self.toplevel.config(background=cp)

        menuTitle = Label(self.toplevel, text="Agregar InsuPan", bg=cs, fg="white", width="30", height="3", font="1")
        menuTitle.pack(padx=3, pady=5)

        CTkLabel(self.toplevel, text="", bg_color=cp).pack(pady=5)
 
        self.entryIDpan = CTkComboBox(self.toplevel, values=self.llenar_combo_idpan(), state="readonly")
        self.entryIDpan.set("ID Pan")
        self.entryIDpan.pack(padx=1, pady=5)

        self.entryIDinsumo = CTkComboBox(self.toplevel, values=self.llenar_combo_idinsumo(), state="readonly")
        self.entryIDinsumo.set("ID Insumo")
        self.entryIDinsumo.pack(padx=1, pady=5)

        self.entryCantidad = CTkEntry(self.toplevel, placeholder_text="Cantidad")
        self.entryCantidad.pack(padx=1, pady=5)

        self.entryIDmedida = CTkComboBox(self.toplevel, values=self.llenar_combo_idmedida(), state="readonly")
        self.entryIDmedida.set("ID Medida")
        self.entryIDmedida.pack(padx=1, pady=5)

        btnSend = CTkButton(self.toplevel, text="Enviar", command=self.enviarInsuPan, fg_color=cs,height=40)
        btnSend.pack(padx=1, pady=5)

        btn_volver= CTkButton(self.toplevel, text="Volver", command=self.volverTpl, fg_color=cs ,height=25, width=20)
        btn_volver.place(x=245, y=370)

    def enviarInsuPan(self):
        if self.controlador.insertar_pan_insumo(self.entryIDpan.get(), self.entryIDinsumo.get(), self.entryCantidad.get(), self.entryIDmedida.get()):
            messagebox.showinfo(message="Registrado con exito")
            self.pantalla.deiconify()
            self.limpiar_ventana()
            InsuPanes(self.pantalla)
            self.toplevel.destroy()
        else:
            messagebox.showerror(message="Error al regisrar el InsuPan", title="Error")


    def llenar_combo_idpan(self):
        valores = self.controlador.ver_panes()
        valores_combo = [str(result[0])+'-'+result[1] for result in valores]
        return valores_combo  
    
    def llenar_combo_idinsumo(self):
        valores = self.controlador.ver_insumos()
        valores_combo = [str(result[0])+'-'+result[1] for result in valores]
        return valores_combo 
    def llenar_combo_idmedida(self):
        valores = self.controlador.ver_unidades()
        valores_combo = [str(result[0])+'-'+result[1] for result in valores]
        return valores_combo 


class Unidades(Menu):
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.pantalla.title("Unidades")
        self.pantalla.geometry("600x400")
        self.pantalla.resizable(width=False, height=False)
        self.controlador = ControladorG()
        img = CTkImage(light_image=Image.open("view/img/fondo2.jpg"), size=(600, 400))
        lbl_img = CTkLabel(pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        menuTitle = Label(self.pantalla, text="Agregar Unidades", bg=cs, fg="white", width="62", height="3", font="1")
        menuTitle.place(x=25, y=20)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background=cs, relief="flat")
        style.map("Treeview.Heading", background=[('active',cs)])

        self.grid = ttk.Treeview( columns=("#1"), show="headings")
        self.grid.column("#0", width=5, anchor=CENTER)
        self.grid.column("#1",width=10, anchor=CENTER)

        self.grid.heading("#0", text="ID",anchor=CENTER)
        self.grid.heading("#1", text="Unidad", anchor=CENTER)
        self.grid.place(x=250, y=100, width=250, height=250)

        data,i=self.controlador.ver_unidades(),-1
        for loca in data:
            self.grid.insert('',i, text=loca[0], values=(loca[1]))

        self.txtHar = CTkEntry(self.pantalla, placeholder_text="Buscar")
        self.txtHar.place(x=50, y=100)
        self.btnBuscar = CTkButton(self.pantalla, text="Buscar", command=self.buscaruni, height=30, fg_color=ce)
        self.btnBuscar.place(x=50, y=145)
        btn_agregar= CTkButton(self.pantalla, text="Agregar", command=self.insertaruni, fg_color=cs,height=40)
        btn_agregar.place(x=50, y=190)
        btn_actualizar= CTkButton(self.pantalla, text="Actualizar", command=self.actualizaruni, fg_color=cs,height=40)
        btn_actualizar.place(x=50, y=250)
        btn_eliminar= CTkButton(self.pantalla, text="Eliminar", command=self.eliminaruni, fg_color=cd,height=40)
        btn_eliminar.place(x=50, y=310)
        btn_volver= CTkButton(self.pantalla, text="Volver", command=self.volver_menu, fg_color=cs ,height=25, width=20)
        btn_volver.place(x=540, y=360)

    def buscaruni(self):
        if self.txtHar.get() == "":
            messagebox.showerror(message=f"Campo vacio, Ingrese un dato", title="Error")
        else:
            if self.controlador.buscar_unidades(self.txtHar.get())!=[]:
                data=self.controlador.buscar_unidades(self.txtHar.get())
                sano= self.grid.get_children()
                for element in sano:
                    self.grid.delete(element)

                i=-1
                for loca in data:
                    self.grid.insert('',i, text=loca[0], values=(loca[1]))
            else:
                messagebox.showerror(message=f"No se encuentra '{self.txtHar.get()}' ", title="Error")
        
    def actualizaruni(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Debe seleccionar un campo", title="Error")
        else:
            self.pantalla.withdraw()
            self.toplevel = CTkToplevel(self.pantalla)
            self.toplevel.geometry("300x200")
            self.toplevel.resizable(False, False)
            self.toplevel.config(background=cp)

            menuTitle = Label(self.toplevel, text="Editar Unidades", bg=cs, fg="white", width="30", height="3", font="1")
            menuTitle.pack(padx=3, pady=5)

            self.entryDescripcion = CTkEntry(self.toplevel, placeholder_text="Descripcion")
            self.entryDescripcion.pack(padx=1, pady=10) 
            
            btnSend = CTkButton(self.toplevel, text="Actualizar", command=self.editunidades, fg_color=ce,height=40)
            btnSend.pack(padx=1, pady=10)

            btn_volver= CTkButton(self.toplevel, text="Volver", command=self.volverTpl, fg_color=cs ,height=25, width=20)
            btn_volver.place(x=245, y=170)
    
    def editunidades(self):
        if self.controlador.actualizar_unidades(self.sisas, self.entryDescripcion.get())=="Actualizado":
            messagebox.showerror(message="Error al actualizar", title="Error")
            self.pantalla.deiconify()
            self.limpiar_ventana()
            Unidades(self.pantalla)
            self.toplevel.destroy()
        else:
            messagebox.showinfo(message="Actualizado con exito")
            self.pantalla.deiconify()
            self.limpiar_ventana()
            Unidades(self.pantalla)
            self.toplevel.destroy()

    def eliminaruni(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Debe seleccionar un campo", title="Error")
        else:
            respuesta = messagebox.askquestion("Eliminar", "¿Estás seguro que deseas eliminar este campo?")
            if respuesta == "yes":
                if self.controlador.eliminar_unidades(self.sisas):
                   messagebox.showinfo(message="Eliminado con exito")
                   self.limpiar_ventana()
                   Unidades(self.pantalla)
                else:
                   messagebox.showerror(message="Error al eliminar", title="Error")
                    
    def insertaruni(self):
        self.pantalla.withdraw()
        self.toplevel = CTkToplevel(self.pantalla)
        self.toplevel.geometry("300x200")
        self.toplevel.resizable(False, False)
        self.toplevel.config(background=cp)

        menuTitle = Label(self.toplevel, text="Agregar Unidades", bg=cs, fg="white", width="30", height="3", font="1")
        menuTitle.pack(padx=3, pady=5)

        self.entryDescripcion = CTkEntry(self.toplevel, placeholder_text="Descripcion")
        self.entryDescripcion.pack(padx=1, pady=10) 
        
        btnSend = CTkButton(self.toplevel, text="Enviar", command=self.enviarUni, fg_color=ce,height=40)
        btnSend.pack(padx=1, pady=10)

        btn_volver= CTkButton(self.toplevel, text="Volver", command=self.volverTpl, fg_color=cs ,height=25, width=20)
        btn_volver.place(x=245, y=170)

    def enviarUni(self):
        if self.controlador.insertar_unidades(self.entryDescripcion.get())=="Insertado":
            messagebox.showerror(message=f"No se pudo agregar '{self.entryDescripcion.get()}' al inventario")
            self.pantalla.deiconify()
            self.limpiar_ventana()
            Unidades(self.pantalla)
            self.toplevel.destroy()
        else:
            messagebox.showinfo(message=f"'{self.entryDescripcion.get()}' agregado con exito")
            self.pantalla.deiconify()
            self.limpiar_ventana()
            Unidades(self.pantalla)
            self.toplevel.destroy()
