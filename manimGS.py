from manim import *

class GaleShapley(Scene):
    def construct(self):
        solicitantes_pref = {
            "s1": ["d1", "d2", "d3"],
            "s2": ["d2", "d1", "d3"],
            "s3": ["d1", "d2", "d3"]
        }

        destinatarios_pref = {
            "d1": ["s3", "s1", "s2"],
            "d2": ["s1", "s2", "s3"],
            "d3": ["s3", "s2", "s1"]
        }
        emparejamientos = {}

        emps = list(destinatarios_pref)
        print("+=+=+=+=+=+=+=+=+",emps)
        tabSolicitantes = self.crear_tabla(solicitantes_pref).scale(.2)

        tabDestinatario = self.crear_tabla(destinatarios_pref).scale(.2)
        tabEmparejamientos = self.crear_tabla_emparejamiento(emparejamientos).scale(.2)
        
        tabDestinatario.to_edge(UP)
        tabEmparejamientos.to_edge(DOWN)
        self.play(Create(tabDestinatario))
        self.play(Create(tabSolicitantes))
        self.play(Create(tabEmparejamientos))
        
        self.wait(.5)
        #emparejamientos = self.gale_shapley(solicitantes_pref, destinatarios_pref)

        emparejamientos = {}
        solicitantes_libres = list(solicitantes_pref.keys())

        #listas para obtener la posicion de los datos para manipular las tablas

        solicitantesIndex=list(solicitantes_pref)
        destinatariosIndex=list(destinatarios_pref)

        #print(solicitantesIndex)
        #print(destinatariosIndex)
        

        while solicitantes_libres:
            solicitante = solicitantes_libres.pop(0)      
            lista_preferencias = solicitantes_pref[solicitante]
            
            #----------------------------------------------------------------------------------------
            #posicion del solicitante en tab solicitantes 
            cajaSol=solicitantesIndex.index(solicitante)
            #----------------------------------------------------------------------------------------
            for destinatario in lista_preferencias:
                cajaDes=lista_preferencias.index(destinatario)
                caja2Sol=destinatariosIndex.index(destinatario)
            
                #V----------------------------------------------------------------------------------------
                #accesos a lista de solicitantes 
                #todos los accesos
                #color naranja?
                #((((((((((((((((((((((((((((((((((((((((((((((((((((((((propuesta))))))))))))))))))))))))))))))))))))))))))))))))))))))))
                self.remove(tabSolicitantes)
                tabSolicitantes = self.propone(solicitantes_pref,1,cajaSol+2,cajaSol+2,lista_preferencias.index(destinatario)+2)
                self.add(tabSolicitantes)
                self.wait(.5)

                print("=====sol:sol x:",1,"y:",cajaSol+2,"->",solicitantesIndex[cajaSol])
                print("=====sol:des x:",cajaSol+2,"y:",lista_preferencias.index(destinatario)+2,"->", lista_preferencias[cajaDes])
                #----------------------------------------------------------------------------------------
                print(f"{solicitante} propone a {destinatario}")
                
                
                # Si el destinatario aún no está emparejado, forma un par
                if destinatario not in emparejamientos:

                    emparejamientos[destinatario] = solicitante
                    #print(emparejamientos)
                    #((((((((((((((((((((((((((((((((((((((((((((((((((((((((empareja))))))))))))))))))))))))))))))))))))))))))))))))))))))))

                    self.remove(tabSolicitantes)
                    tabSolicitantes = self.empareja(solicitantes_pref,1,cajaSol+2,cajaSol+2,lista_preferencias.index(destinatario)+2)
                    self.add(tabSolicitantes)
                    self.wait(.5)


                    #V----------------------------------------------------------------------------------------
                    #acceso para emparejamiento 
                    print("-----sol:sol x:",1,"y:",cajaSol+2,"->",solicitantesIndex[cajaSol])
                    print("-----sol:des x:",cajaSol+2,"y:",lista_preferencias.index(destinatario)+2,"->", lista_preferencias[cajaDes])

                    #print("des:des x: ",caja2Sol+2," y: ",)

                    #----------------------------------------------------------------------------------------
                    print(f"Emparejamiento formado: {solicitante} y {destinatario}")
                    self.remove(tabEmparejamientos)
                    tabEmparejamientos = self.crear_tabla_emparejamiento(emparejamientos).scale(.2)
                    tabEmparejamientos.to_edge(DOWN)
                    self.add(tabEmparejamientos)
                    self.wait(.5)
                    
                    break
                else:
                    # Si el destinatario prefiere al nuevo solicitante
                    solicitante_actual = emparejamientos[destinatario]
                    desInd=destinatariosIndex.index(destinatario)+2
                    if destinatarios_pref[destinatario].index(solicitante) < destinatarios_pref[destinatario].index(solicitante_actual):
                        #caja2Des=destinatarios_pref.index(solicitante)
                        
                        emparejamientos[destinatario] = solicitante
                        solicitantes_libres.append(solicitante_actual)

                        #((((((((((((((((((((((((((((((((((((((((((((((((((((((((cambio))))))))))))))))))))))))))))))))))))))))))))))))))))))))
                        self.remove(tabDestinatario)
                        tabDestinatario = self.cambia(destinatarios_pref,destinatarios_pref[destinatario].index(solicitante)+2,desInd,destinatarios_pref[destinatario].index(solicitante_actual)+2,desInd)
                        tabDestinatario.to_edge(UP)
                        self.add(tabDestinatario)
                        self.wait(.5)
                        self.remove(tabDestinatario)
                        tabDestinatario = self.crear_tabla(destinatarios_pref).scale(.2)
                        tabDestinatario.to_edge(UP)
                        self.add(tabDestinatario)
                        
                        print("*****des:des x:",1,"y:",desInd,"->",destinatariosIndex[desInd-2])
                        #XYsol----------------------------------------------------------------------------------------
                        print("*****des:sol:actual x:",destinatarios_pref[destinatario].index(solicitante)+2,"y:",desInd,"->",solicitante)
                        #XYsolcambio----------------------------------------------------------------------------------------
                        print("*****des:sol:cambio(ex) x:",destinatarios_pref[destinatario].index(solicitante_actual)+2,"y:",desInd,"->",solicitante_actual)

                        #----------------------------------------------------------------------------------------
                        print(f"{destinatario} cambia a {solicitante} por {solicitante_actual}")
                        break
                    else:
                         #((((((((((((((((((((((((((((((((((((((((((((((((((((((((rechaza))))))))))))))))))))))))))))))))))))))))))))))))))))))))
                        self.remove(tabDestinatario)
                        tabDestinatario = self.rechaza(destinatarios_pref,1,desInd,destinatarios_pref[destinatario].index(solicitante)+2,desInd)
                        tabDestinatario.to_edge(UP)
                        self.add(tabDestinatario)
                        self.wait(.5)
                        self.remove(tabDestinatario)
                        tabDestinatario = self.crear_tabla(destinatarios_pref).scale(.2)
                        tabDestinatario.to_edge(UP)
                        self.add(tabDestinatario)

                        print("+++++des:sol:rechaza x:",1,"y:",desInd,"->",solicitante)
                        print("+++++des:des:rechaza x:",destinatarios_pref[destinatario].index(solicitante)+2,"y:",desInd,"->",destinatariosIndex[desInd-2])
                        print(f"{destinatario} rechaza a {solicitante}")

        self.wait(3)
        return emparejamientos



    def crear_tabla_emparejamiento(self, diccionario):
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",diccionario.type())
        filasGen=[]
        for i in range(1):
            if i == 0:
                filasGen.append("parejas")
            
        filas=[filasGen]
        for destinatario,preferencias in diccionario.items():
            #print("===========================================",destinatario.type())
            #print("===========================================",preferencias.type())
            #if preferencias==None:
                #preferencias=""
            prex=destinatario+":"+preferencias
            fila = [prex]
            filas.append(fila)

        tabla=Table(filas)
        return tabla

    def crear_tabla(self, diccionario):

        # Crear las filas de la tabla a partir del diccionario
        filasGen=[]
        for i in range(len(list(diccionario.values())[0])+1):
            if i == 0:
                filasGen.append("Solicitante")
            else:
                filasGen.append("Preferencia "+str(i))

        filas = [filasGen]
        
        for solicitante, preferencias in diccionario.items():
            fila = [solicitante] + preferencias
            filas.append(fila)

        # Crear y retornar la tabla
        tabla = Table(filas)
        return tabla

    def iluminacionSol(self,solicitantes,x,y):
        nuevaTabla = self.crear_tabla(solicitantes).scale(.2)
        nuevaTabla.add_highlighted_cell((x,y), color=GREEN)
        print(x,y)
        return nuevaTabla
    
    def rechaza(self,destinatarios,x1,y1,x2,y2):
        nuevaTabla = self.crear_tabla(destinatarios).scale(.2)
        nuevaTabla.add_highlighted_cell((y1,x1), color=RED_C)
        nuevaTabla.add_highlighted_cell((y2,x2), color=RED_C)
        return nuevaTabla

    def propone(self,solicitantes,x1,y1,x2,y2):
        nuevaTabla = self.crear_tabla(solicitantes).scale(.2)
        nuevaTabla.add_highlighted_cell((y1,x1), color=GREEN)
        nuevaTabla.add_highlighted_cell((x2,y2), color=GOLD)
        return nuevaTabla
    def empareja(self,solicitantes,x1,y1,x2,y2):
        nuevaTabla = self.crear_tabla(solicitantes).scale(.2)
        nuevaTabla.add_highlighted_cell((y1,x1), color=YELLOW_C)
        nuevaTabla.add_highlighted_cell((x2,y2), color=YELLOW_C)
        return nuevaTabla
    def cambia(self,destinatarios,x1,y1,x2,y2):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>cambio")
        print(destinatarios)
        nuevaTabla = self.crear_tabla(destinatarios).scale(.2)
        nuevaTabla.add_highlighted_cell((y1,x1), color=BLUE_D)
        nuevaTabla.add_highlighted_cell((y2,x2), color=BLUE_D)
        return nuevaTabla

        
    """
    pruebas


    solicitantes_pref = {
        "s1": ["d1", "d2", "d3", "d4"],
        "s2": ["d2", "d1", "d3", "d4"],
        "s3": ["d3", "d2", "d4", "d1"],
        "s4": ["d1", "d2", "d3", "d4"]
    }

    destinatarios_pref = {
        "d1": ["s3", "s1", "s2", "s4"],
        "d2": ["s1", "s2", "s3", "s4"],
        "d3": ["s3", "s2", "s1", "s4"],
        "d4": ["s1", "s2", "s4", "s3"]
    }

    solicitantes_pref = {
        "s1": ["d4", "d3", "d2", "d1"],
        "s2": ["d3", "d2", "d1", "d4"],
        "s3": ["d2", "d1", "d4", "d3"],
        "s4": ["d1", "d2", "d3", "d4"]
        }

        destinatarios_pref = {
            "d1": ["s1", "s2", "s3", "s4"],
            "d2": ["s2", "s3", "s4", "s1"],
            "d3": ["s3", "s4", "s1", "s2"],
            "d4": ["s4", "s1", "s2", "s3"]
        }

    """
    
