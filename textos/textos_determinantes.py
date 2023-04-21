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

def text_determinantes_tipo(gdf, tipo):
    """
        Función para generar texto por tipo
        de determinante
    """

    text = str()
    if len(gdf) > 0:
        for row in gdf.itertuples():
            capa = row.CAPA_GEO
            area = row.AREA_CRUCE
            percent = row.PORCENTAJE
            area = round(area,2) # area intercept
            percent = round(percent,2)
            ha = int(area) #Hectareas sin decimales
            m2 = round(area - ha*10000,2) # metros cuadrados
            text += f"- {tipo}: {capa} en {ha} Ha {m2} m2 ({percent}%)\n"

    return text

def text_determinantes_predio(gdf_resti, gdf_condi, gdf_otros, fuente):
    """
        Función para generar textos a partir del 
        geoproceso de determinantes por qr
    """
    text_determinantes = ""

    if (len(gdf_resti) > 0 or len(gdf_condi) > 0 or len(gdf_otros) > 0):

        text_determinantes += """La información que se relaciona a continuación corresponde a cruces meramente cartográficos entre la información de restricciones y condicionantes entregada por la ANT y la obtenida durante la operación del BPM. Por tal razón, se aclara que es meramente informativa y en ningún momento sustituye los conceptos que deben emitir las entidades competentes según el caso.\n""" 
        
        # Restricciones
        text_determinantes += text_determinantes_tipo(gdf_resti, "Restricción")

        # Condicionantes 
        text_determinantes += text_determinantes_tipo(gdf_condi, "Condicionante")

        # Otros Erosion
        text_determinantes += text_determinantes_tipo(gdf_otros, "Otros cruces")

        if ('EROSIÓN MUY SEVERA - PBOT' in text_determinantes) or ('EROSIÓN SEVERA - PBOT' in text_determinantes):
            text_determinantes += "\nAunque el plano de “Erosión” del Plan Básico de Ordenamiento Territorial vigente aprobado mediante Acuerdo 019 del 31 de diciembre de 2002, suministrado por la oficina de planeación municipal de Pradera (Valle), advierte categorización del suelo en erosión SEVERA o MUY SEVERA, es importante anotar que el mismo plano no manifiesta si corresponde a un riesgo de carácter mitigable o no mitigable, elemento a tener en cuenta en el curso de atención OSPR con sujeción a la normatividad vigente, en este sentido y en virtud de la indeterminación, se solicitó  a la oficina de planeación municipal nos certifique el plan de mitigación, tal que, la actividad de procesamiento de información y análisis jurídico/técnico del predio objeto de intervención en el BPM continuará en su trámite a fin de que en sede de ejecución de la respectiva ruta de atención se dilucide la categoría del riesgo existente.\n"
        elif ('EROSIÓN MODERADA - PBOT' in text_determinantes):
            text_determinantes += "\nEl predio objeto de estudio, se encuentra en una zona que presenta EROSIÓN MODERADA, según fuente Plan básico de Ordenamiento Territorial de Pradera Acuerdo No. 019 (31 diciembre del 2002). Mapa: Erosión Fuente Temática: PBOT Pradera 2002.\n"
        elif ('EROSIÓN LIGERA - PBOT' in text_determinantes):
            text_determinantes += "\nEl predio objeto de estudio, se encuentra en una zona que presenta EROSIÓN LIGERA, según fuente Plan básico de Ordenamiento Territorial de Pradera Acuerdo No. 019 (31 diciembre del 2002). Mapa: Erosión Fuente Temática: PBOT Pradera 2002.\n"

        # Fuente versión de la capas geoproceso
        text_determinantes += f"\nFuente: Capa Cruces Geoproceso entregado por SSIT {fuente}"

    return text_determinantes