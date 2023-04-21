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

def text_uaf_predio (gdf_inter_uaf):
    """
        Función para contruir los textos de UAF
        por predio.
    """
    text_total_uaf = ""
    len_gdf = len(gdf_inter_uaf)
    if len_gdf > 0:
        i = 1
        text_uaf = ""
        for row in gdf_inter_uaf.itertuples():
            area_terreno = row.area_terreno
            zonah = row.ZONA_HOMOGENEA
            name_zonah = row.NOMBRE_ZONA_HOMOGENEA.lower()
            uaf_min = row.UNIDAD_AGRICOLA_FAMILIAR_MINIMA
            uaf_max = row.UNIDAD_AGRICOLA_FAMILIAR_MAXIMA
            range_uaf = row.UNIDAD_AGRICOLA_FAMILIAR
            area = row.area_intercept
            Ha = int(area/10000) #Hectareas sin decimales
            m2 = round(area - Ha*10000,2) # metros cuadrados
            if(round(row.porcentaje,2) > 99.9):
                percent = 100.00
            else:
                percent = row.porcentaje
            area_Tha = area_terreno/10000
            if area_Tha < uaf_min:
                analisis_uaf = ", por lo que el predio es inferior a la UAF"
            elif area_Tha > uaf_max:
                analisis_uaf = ", por lo que el predio es superior a la UAF"
            elif area_Tha > uaf_min and area_Tha < uaf_max:
                analisis_uaf = ", por lo que el predio esta dentro del rango UAF"
            if (len_gdf > 1):
                if percent >= 90:
                    if i == 1:
                        if range_uaf == 'UAF NO DEFINIDA':
                            text_uaf = " con {} Ha {} m2 en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle con UAF no determinada".format(Ha, m2, zonah, name_zonah)
                        else:
                            text_uaf = " con {} Ha {} m2 en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle correspondiente al rango entre {}{}".format(Ha, m2, zonah, name_zonah, range_uaf, analisis_uaf)
                    elif i == len_gdf:
                        if range_uaf == 'UAF NO DEFINIDA':
                            text_uaf = " y con {} Ha {} m2 en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle con UAF no determinada.".format(Ha, m2, zonah, name_zonah)
                        else:
                            text_uaf = " y con {} Ha {} m2 en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle correspondiente al rango entre {}{}.".format(Ha, m2, zonah, name_zonah, range_uaf, analisis_uaf)
                    else:
                        if range_uaf == 'UAF NO DEFINIDA':
                            text_uaf = ", con {} Ha {} m2 en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle con UAF no determinada".format(Ha, m2, zonah, name_zonah)
                        else:
                            text_uaf = ", con {} Ha {} m2 en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle correspondiente al rango entre {}{}".format(Ha, m2, zonah, name_zonah, range_uaf, analisis_uaf)
                else:
                    if i == 1:
                        if range_uaf == 'UAF NO DEFINIDA':
                            text_uaf += " con {} Ha {} m2 en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle con UAF no determinada".format(Ha, m2, zonah, name_zonah)
                        else:
                            text_uaf += " con {} Ha {} m2 en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle correspondiente al rango entre {}{}".format(Ha, m2, zonah, name_zonah, range_uaf, analisis_uaf)
                    elif i == len_gdf:
                        if range_uaf == 'UAF NO DEFINIDA':
                            text_uaf += " y con {} Ha {} m2 en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle con UAF no determinada.".format(Ha, m2, zonah, name_zonah)
                        else:
                            text_uaf += " y con {} Ha {} m2 en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle correspondiente al rango entre {}{}.".format(Ha, m2, zonah, name_zonah, range_uaf, analisis_uaf)
                    else:
                        if range_uaf == 'UAF NO DEFINIDA':
                            text_uaf += ", con {} Ha {} m2 en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle con UAF no determinada".format(Ha, m2, zonah, name_zonah)
                        else:
                            text_uaf += ", con {} Ha {} m2 en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle correspondiente al rango entre {}{}".format(Ha, m2, zonah, name_zonah, range_uaf, analisis_uaf)
            else:
                if range_uaf == 'UAF NO DEFINIDA':
                    text_uaf += " en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle con UAF no determinada.".format(zonah, name_zonah)
                else:
                    text_uaf += " en la Zona Relativamente Homogénea No.{} denominada {} de la Regional Valle correspondiente al rango entre {}{}.".format(zonah,name_zonah, range_uaf, analisis_uaf)
            i+=1
        text_complement_uaf = 'El análisis UAF es realizado por medio de una capa geográfica elaborada a partir de las curvas de nivel del IGAC, modelo digital de elevaciones y conforme a las características establecidas en la Resolución No. 041 del 24/09/1996 del INCORA, encontrando que el predio se ubica'

        text_total_uaf = text_complement_uaf + text_uaf

    return text_total_uaf


def texto_area_minima(gdf_inter_area_minima, porcen_intercept):
    """
        Función para establecer texto para áreas minima de parcelación
    """
    text_minParce = ""
    # área mínima parcelación
    if len(gdf_inter_area_minima) > 0:
        gdf_inter_area_minima = gdf_inter_area_minima.sort_values(by="porcentaje", ascending=False)
        percent_max = gdf_inter_area_minima['porcentaje'].values[0]
        if (percent_max > int(porcen_intercept)):
            area_actividad = gdf_inter_area_minima['area_actividad'].values[0]
            area_terreno = gdf_inter_area_minima['area_terreno'].values[0]
            area_parcela_min = gdf_inter_area_minima["AREA_MIN_M2"].values[0] # area de parcelación minima permitida
            if (area_terreno < area_parcela_min):
                text_minParce = f"\n\nUna vez analizado el Acuerdo No. 019 de 2002, modificado por el Acuerdo No. 005 “Por Medio Del Cual Se Modifica El Plan De Ordenamiento Territorial Incorporando Predios Ubicados En Suelo Rural Y De Expansión Urbana Al Perímetro Urbano Del Municipio, Con El Fin De Garantizar El Desarrollo De Vivienda De Interés Social Vis, Vivienda De Interés Prioritario Vip Y Se Dictan Otras Disposiciones”, que en sus artículos No. 204, 205-Parágrafo 1- 206-Parágrafo 1- y Art. 213 preceptúa los rangos de áreas mínimas para adjudicar y/o formalizar predios en el municipio de Pradera, y en concordancia de la cartografía e insumos catastrales suministrados por la Secretaría de Planeación e Infraestructura de Pradera (Valle), así las cosas el predio se encuentra en un área de {area_actividad}; que presenta un área mínima de subdivisión de {area_parcela_min} m2, por lo cual se evidencia que el predio se encuentra por debajo de este valor."
                text_minParce += "\n\nEs imperativo mencionar que, aunque el inmueble objeto de estudio cuenta con un área inferior a las mínimas adjudicables diseminadas en el Acuerdo 019 de 2002 del municipio de Pradera-Valle del Cauca, ello no es óbice para determinar que la Agencia Nacional de Tierras-ANT-  contraria el derecho que tiene el municipio para ordenar su territorio-concepto analizado en Sentencia C-149 de 2010- ante el reconocimiento de derechos de propiedad a los pobladores rurales que se encuentren ejerciendo una ocupación o posesión dentro de extensiones de terreno que estén por fuera de las que se encuentran erigidas en los PBOT; por el contrario, su fin misional como máxima autoridad de tierras de la Nación al pronunciarse de fondo frente a la formalización de la pequeña y mediana propiedad, es resolver el problema en la tenencia de la tierra  garantizando el acceso progresivo a la misma y dar cumplimiento a la Reforma Rural Integral con el Ordenamiento Social de la Propiedad."
            else:
                text_minParce = f"\n\nUna vez analizado el Acuerdo No. 019 de 2002, modificado por el Acuerdo No. 005 “Por Medio Del Cual Se Modifica El Plan De Ordenamiento Territorial Incorporando Predios Ubicados En Suelo Rural Y De Expansión Urbana Al Perímetro Urbano Del Municipio, Con El Fin De Garantizar El Desarrollo De Vivienda De Interés Social Vis, Vivienda De Interés Prioritario Vip Y Se Dictan Otras Disposiciones”, que en sus artículos No. 204, 205-Parágrafo 1- 206-Parágrafo 1- y Art. 213 preceptúa los rangos de áreas mínimas para adjudicar y/o formalizar predios en el municipio de Pradera, y en concordancia de la cartografía e insumos catastrales suministrados por la Secretaría de Planeación e Infraestructura de Pradera (Valle), así las cosas el predio se encuentra en un área de {area_actividad}; que presenta un área mínima de subdivisión de {area_parcela_min} m2, por lo cual se evidencia que el predio se encuentra por encima de este valor."
               

    return text_minParce