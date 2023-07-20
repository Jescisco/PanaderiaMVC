import mariadb

class Connection:

    def connect(self):
        try:
            connection = mariadb.connect(host='localhost',user='root',password='',database='panificadora')
            return connection
        except mariadb.Error as error:
            return error

    def setExecute(self, query):
        conn=self.connect()
        cursor=conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
            row=cursor.rowcount
            return row
        except mariadb.Error as error:
            return error
        finally:
            conn.close()

    def getExecute(self, query):
        conn=self.connect()
        cursor=conn.cursor()
        try:
            cursor.execute(query)
            resultados=cursor.fetchall()
            return resultados
        except mariadb.Error as error:
            return error
        finally:
            conn.close()

class lol(Connection):

#tabla insumos        
    def insert_insumos(self, des_ins, id_uni, exi_min, exi_max, can_disp):
        query = f"INSERT INTO insumos(des_ins, id_uni, exi_min, exi_max, can_disp) VALUES ('{des_ins}', '{id_uni}', '{exi_min}', '{exi_max}', '{can_disp}')"
        resultado=self.setExecute(query)

        if resultado!=0:
            respuesta="No se insertó"
        elif resultado==0:
            respuesta="Insertado"
        else:
            respuesta=resultado
        return respuesta
    
    def view_insumo(self):
        query = f"SELECT * FROM insumos ORDER BY id_ins DESC"
        result =self.getExecute(query)
        return result
    
    def search_insumo(self, desc):
        query = f"SELECT * FROM insumos WHERE des_ins = '{desc}'"
        resultado = self.getExecute(query)
        return resultado
    
    def update_insumo(self, id_ins, u_des_ins, u_id_uni, u_exi_min, u_exi_max, u_can_disp):
        query = f"UPDATE insumos SET des_ins = '{u_des_ins}', id_uni = '{u_id_uni}', exi_min = '{u_exi_min}', exi_max = '{u_exi_max}', can_disp = '{u_can_disp}' WHERE id_ins = '{id_ins}'"
        resultado = self.setExecute(query)
        if resultado != 0:
         respuesta = "No se actualizó"
        elif resultado == 0:
            respuesta = "Actualizado"
        else:
            respuesta = resultado
        return respuesta
    
    def delete_insumo(self, id):
        query = f"DELETE FROM insumos WHERE id_ins = '{id}'"
        result=self.setExecute(query)
        if result!=0:
            respuesta="No se elimino"
        elif result==0:
            respuesta="Eliminado"
        else:
            respuesta=result
        return respuesta

#tabla panes  
    def insert_panes(self, des_pan):
        query = f"INSERT INTO panes(des_pan) VALUES ('{des_pan}')"
        resultado=self.setExecute(query)
        if resultado!=0:
            respuesta="No se insertó"
        elif resultado==0:
            respuesta="Insertado"
        else:
            respuesta=resultado
        return respuesta
    
    def search_panes(self, desc):
        query = f"SELECT * FROM panes WHERE des_pan = '{desc}'"
        resultado = self.getExecute(query)
        return resultado

    def view_panes(self):
        query = f"SELECT * FROM panes ORDER BY id_pan DESC"
        result =self.getExecute(query)
        return result
    
    def update_panes(self, id_pan, u_des_pan):
        query = f"UPDATE panes SET des_pan = '{u_des_pan}' WHERE id_pan = '{id_pan}'"
        resultado = self.setExecute(query)
        if resultado != 0:
            respuesta = "Actualizado"
        elif resultado == 0:
            respuesta = "No se actualizó"
        else:
            respuesta = resultado
        return respuesta
    
    def delete_panes(self, id_pan):
        query = f"DELETE FROM panes WHERE id_pan = '{id_pan}'"
        result=self.setExecute(query)
        return result

#tabla panes_insumos  
    def insert_pan_insumo(self, id_pan, id_ins, can_ins, id_uni):
        query = f"INSERT INTO panes_insumos(id_pan, id_ins, can_ins, id_uni) VALUES ('{id_pan}', '{id_ins}', '{can_ins}', '{id_uni}')"
        resultado=self.setExecute(query)
        if resultado!=0:
            respuesta="Insertado"
        elif resultado==0:
            respuesta="No se insertó"
        else:
            respuesta=resultado
        return respuesta
    
    def view_pan_insumo(self):
        query = f"SELECT * FROM panes_insumos ORDER BY id_panins DESC"
        result =self.getExecute(query)
        return result
    
    def update_pan_insumo(self, id_panins, u_id_pan, u_id_ins, u_can_ins, u_id_uni):
        query = f"UPDATE panes_insumos SET id_pan = '{u_id_pan}', id_ins = '{u_id_ins}', can_ins = '{u_can_ins}', id_uni = '{u_id_uni}' WHERE id_panins = '{id_panins}'"
        resultado = self.setExecute(query)
        if resultado != 0:
         respuesta = "No se actualizó"
        elif resultado == 0:
            respuesta = "Actualizado"
        else:
            respuesta = resultado
        return respuesta
    
    def search_pan_insumos(self, desc):
        query = f"SELECT * FROM panes_insumos WHERE id_pan = '{desc}'"
        resultado = self.getExecute(query)
        return resultado
    
    def delete_pan_insumo(self, id_panins):
        query = f"DELETE FROM panes_insumos WHERE id_panins = '{id_panins}'"
        result=self.setExecute(query)
        return result
    
#tabla unidades    
    def insert_unidades(self, des_uni):
        query = f"INSERT INTO unidades(des_uni) VALUES ('{des_uni}')"
        resultado=self.setExecute(query)
        if resultado!=0:
            respuesta="Insertado"
        elif resultado==0:
            respuesta="No se insertó"
        else:
            respuesta=resultado
        return respuesta
    
    def search_unidades(self, desc):
        query = f"SELECT * FROM unidades WHERE des_uni = '{desc}'"
        resultado = self.getExecute(query)
        return resultado
    
    def view_unidades(self):
        query = f"SELECT * FROM unidades ORDER BY id_uni DESC"
        result =self.getExecute(query)
        return result
    
    def update_unidades(self, id_uni, u_des_uni):
        query = f"UPDATE unidades SET des_uni = '{u_des_uni}' WHERE id_uni = '{id_uni}'"
        resultado = self.setExecute(query)
        if resultado != 0:
            respuesta = "Actualizado"
        elif resultado == 0:
         respuesta = "No se actualizó"
        else:
            respuesta = resultado
        return respuesta
    
    def delete_unidades(self, id_uni):
        query = f"DELETE FROM unidades WHERE id_uni = '{id_uni}'"
        result=self.setExecute(query)
        if result!=0:
            respuesta="No se elimino"
        elif result==0:
            respuesta="Eliminado"
        else:
            respuesta=result
        return respuesta