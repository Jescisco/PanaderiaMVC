from model.modelo import lol

class ControladorG(lol):

    #tabla insumos 
    def insertar_insumos(self, des_ins, id_uni, exi_min, exi_max, can_disp):
        respuesta = self.insert_insumos(des_ins, id_uni, exi_min, exi_max, can_disp)
        return respuesta

    def ver_insumos(self):
        respuesta = self.view_insumo()
        return respuesta

    def actualizar_insumos(self, id_ins, u_des_ins, u_id_uni, u_exi_min, u_exi_max, u_can_disp):
        respuesta = self.update_insumo(id_ins, u_des_ins, u_id_uni, u_exi_min, u_exi_max, u_can_disp)
        return respuesta
    
    def eliminar_insumos(self, id):
        respuesta = self.delete_insumo(id)
        return respuesta
    
    def buscar_insumos(self, desc):
        respuesta = self.search_insumo(desc)
        return respuesta

    #tabla panes
    def insertar_panes(self, des_pan):
        respuesta = self.insert_panes(des_pan)
        return respuesta
    
    def buscar_panes(self, desc):
        respuesta = self.search_panes(desc)
        return respuesta

    def ver_panes(self):
        respuesta = self.view_panes()
        return respuesta

    def actualizar_panes(self, id_pan, u_des_pan):
        respuesta = self.update_panes(id_pan, u_des_pan)

    def eliminar_panes(self, id_pan):
        respuesta = self.delete_panes(id_pan)
        return respuesta

    #tabla panes_insumos 
    def insertar_pan_insumo(self, id_pan, id_ins, can_ins, id_uni):
        resultado = self.insert_pan_insumo(id_pan, id_ins, can_ins, id_uni) 
        return resultado
    
    def buscar_pan_insumo(self, desc):
        respuesta = self.search_pan_insumos(desc)
        return respuesta
    
    def ver_pan_insumo(self):
        respuesta = self.view_pan_insumo()
        return respuesta
    
    def actualizar_pan_insumo(self, id_panins, u_id_pan, u_id_ins, u_can_ins, u_id_uni):
        respuesta = self.update_pan_insumo(id_panins, u_id_pan, u_id_ins, u_can_ins, u_id_uni)
        return respuesta
    
    def eliminar_pan_insumo(self, id_panins):
        respuesta = self.delete_pan_insumo(id_panins)
        return respuesta
    
    #tabla unidades
    def insertar_unidades(self, des_uni):
        resultado = self.insert_unidades(des_uni) 
        return resultado
    
    def ver_unidades(self):
        respuesta = self.view_unidades()
        return respuesta
    
    def actualizar_unidades(self, id_uni, u_des_uni):
        respuesta = self.update_unidades(id_uni, u_des_uni)
        return respuesta
    
    def buscar_unidades(self, desc):
        respuesta = self.search_unidades(desc)
        return respuesta
    
    def eliminar_unidades(self, id_uni):
        respuesta = self.delete_unidades(id_uni)
        return respuesta   