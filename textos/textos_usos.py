"""
/***************************************************************************
                    Script para generar reportes automáticos
                        Determinantes - Usos - UAF
                                Pradera POSPR
                             --------------------
                                Abril 2023
                        by: Leonardo Jimenez Joven             
                                    ljimj
 ***************************************************************************/
"""

def text_usos_predio(gdf_inter_area_activ, gdf_inter_uso_actual, gdf_inter_uso_potencial):
    """
        Función para contruir los textos de usos
        por predio.
    """
    text_uso = "De acuerdo a la información entregada por la secretaría de planeación de Pradera, especialmente los planos de Áreas de Actividad, Uso Actual del Suelo y Uso Potencial del Suelo, el predio objeto de estudio se encuentra "

    if len(gdf_inter_area_activ) > 0:
        text_uso += texto_area_actividad(gdf_inter_area_activ)
    if len(gdf_inter_uso_actual) > 0:
        text_uso += texto_uso_actual(gdf_inter_uso_actual)
    if len(gdf_inter_uso_potencial) > 0:
        text_uso += texto_uso_potencial(gdf_inter_uso_potencial)
    
    return text_uso


def texto_area_actividad(gdf_inter_area_activ):
    """
        Función para construir el texto de 
        area de actividad
    """

    i=1
    text_uso = 'en un área de actividad de'
    len_gdf = len(gdf_inter_area_activ)
    for row in gdf_inter_area_activ.itertuples():
        
        areaAct = row.area_actividad.lower()
        if(round(row.porcentaje,2) >= 99.5):
            percent = 100.00
        else:
            percent = round(row.porcentaje,2)

        area = row.area_intercept
        Ha = str(int(area/10000)) #Hectareas sin decimales
        m2 = str(round(area - Ha*10000,2)) # metros cuadrados
        if(i != len_gdf and i != 1):
            #Proyectos Productivos en XX Ha (XX%) y XXXX en XX Ha y XX M2 (XX%),
            text_uso += ", {} en {} Ha {} m2 ({}%)".format(areaAct, Ha, m2, percent)
        elif(i == 1):
            text_uso += " {} en {} Ha {} m2 ({}%)".format(areaAct, Ha, m2, percent)
        else:
            text_uso += ", {} en {} Ha {} m2 ({}%)".format(areaAct, Ha, m2, percent)
        i+=1

    return text_uso

def texto_uso_actual(gdf_inter_uso_actual):
    """
        Función para construir el texto de 
        uso actual
    """
    # Diccionario de usos actuales
    usos_actuales_pradera = {'RA': 'Rastrojo', 'PN-E': 'Pasto natural enmalezado', 
                             'PN': 'Pasto Natural', 'PM': 'Vegetación de paramo', 
                             'CÑ': 'Caña', 'CC': 'Café', 'BN': 'Bosque natural', 
                             'BA': 'Bosque plantado', 'AV': 'Avicola'}
    
    i=1
    text_uso = ', con un uso actual de'
    #accediendo a registros de Uso actual segun el campo especificado
    len_gdf = len(gdf_inter_uso_actual)
    for row in gdf_inter_uso_actual.itertuples():
        uso = usos_actuales_pradera[row.USO].lower()
        if(round(row.porcentaje,2) >= 99.5):
            percent = 100.00
        else:
            percent = round(row.porcentaje,2)
        area = row.area_intercept
        Ha = str(int(area/10000)) #Hectareas sin decimales
        m2 = str(round(area - Ha*10000,2)) # metros cuadrados
        if(i != len_gdf and i != 1):
            #con un uso actual de Rastrojo en XX Ha y XX M2 (XX%) y de Café en XX Ha y XX M2 (XX%)
            text_uso += ", ({}) {} en {} Ha {} m2 ({}%)".format(row.USO, uso, Ha, m2, percent)
        elif(i == 1):
            text_uso += " ({}) {} en {} Ha {} m2 ({}%)".format(row.USO, uso, Ha, m2, percent)
        else:
            text_uso += ", ({}) {} en {} Ha {} m2 ({}%)".format(row.USO, uso, Ha, m2, percent)
        i+=1
    
    return text_uso

def texto_uso_potencial(gdf_inter_uso_potencial):
    """
        Función para construir el texto de 
        uso potencial
    """
    # Diccionario de usos potenciales
    usos_potenciales_pradera = {'F2': 'Tierras forestales', 'R': 'Tierras para reservas naturales', 
                                'F1': 'Tierras forestales', 'C3': 'Tierras cultivables', 
                                'C4': 'Tierras cultivables', 'F2/P': 'Tierras para bosques protectores', 
                                'F3': 'Tierras forestales', 'P': 'Tierras para praderas', 
                                'AF': 'Tierras para arboles frutales', 'C1': 'Tierras cultivables'}

    i=1
    text_uso = ' y un uso potencial de'
    #accediendo a registros de uso potencial segun el campo especificado
    len_gdf = len(gdf_inter_uso_potencial)
    for row in gdf_inter_uso_potencial.itertuples():
        uso = usos_potenciales_pradera[row.USO].lower()
        if(round(row.porcentaje,2) >= 99.5):
            percent = 100.00
        else:
            percent = round(row.porcentaje,2)
        area = row.area_intercept
        Ha = str(int(area/10000)) #Hectareas sin decimales
        m2 = str(round(area - Ha*10000,2)) # metros cuadrados
        if(i != len_gdf and i != 1):
            #un uso potencial de tierras forestales en XX Ha y XX M2 y de Tierras Cultivables en XX Ha y XX M2 (XX%)
            text_uso += ", ({}) {} en {} Ha {} m2 ({}%)".format(row.USO, uso, Ha, m2, percent)
        elif(i == 1):
            text_uso += " ({}) {} en {} Ha {} m2 ({}%)".format(row.USO, uso, Ha, m2, percent)
        else:
            text_uso += " y ({}) {} en {} Ha {} m2 ({}%)".format(row.USO, uso, Ha, m2, percent)
        i+=1
    
    return text_uso


    
    


