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

import geopandas as gpd
import pandas as pd
from get_variables_xls import get_variables_xls
from textos.textos_determinantes import text_determinantes_predio
from textos.textos_uaf import text_uaf_predio, texto_area_minima
from textos.textos_usos import text_usos_predio
from time import localtime, strftime
from datetime import datetime

def read_capa_geo (path_insumos, name_capa):
    """
        Función para leer capas geográficas
    """

    path_capa = "/".join([path_insumos, name_capa])
    gdf = gpd.read_file(path_capa)

    return gdf

def get_capas_geo (path_insumos, name_areas_min, name_restri, name_condi, name_otros, name_uaf, name_area_act, name_uso_act, name_uso_poten, name_lc_terreno, porcen_intercept, fuente):
    """
        Función obtener las capas geograficas
        que se necesitan para los reportes
    """

    # LC_TERRENO
    print(" -   1. Leyendo LC_TERRENO")
    
    gdf_lc_terreno = read_capa_geo (path_insumos, name_lc_terreno)
    gdf_lc_terreno["area_terreno"] = gdf_lc_terreno.area
    #gdf_lc_terreno = gdf_lc_terreno["etiqueta"]
    #print(gdf_lc_terreno.head())

    # DETERMINANTES
    print(" -   2. Leyendo determinantes ")
    print(" - -   2.1 Restricciones")
    
    name_restri = f"Determinantes/{name_restri}"
    gdf_resti = read_capa_geo (path_insumos, name_restri)
    gdf_resti = gdf_resti.to_crs(gdf_lc_terreno.crs) # reproyectando
    
    print(" - -   2.2 Condicionantes")
    
    name_condi = f"Determinantes/{name_condi}"
    gdf_condi = read_capa_geo (path_insumos, name_condi)
    gdf_condi = gdf_condi.to_crs(gdf_lc_terreno.crs) # reproyectando
    
    print(" - -   2.3 Otros erosion PBOT")
    
    name_otros = f"Determinantes/{name_otros}"
    gdf_otros = read_capa_geo (path_insumos, name_otros)
    gdf_otros = gdf_otros.to_crs(gdf_lc_terreno.crs) # reproyectando

    # USOS   
    print(" -   3. Leyendo USOS")
    print(" - -  3.1. Areas actividad")
    
    name_area_activ = f"Usos/{name_area_act}"
    gdf_area_activ = read_capa_geo (path_insumos, name_area_activ)
    gdf_area_activ = gdf_area_activ.to_crs(gdf_lc_terreno.crs) # reproyectando

    print(" - -  3.2. Uso actual")
    
    name_uso_actual = f"Usos/{name_uso_act}"
    gdf_uso_actual = read_capa_geo (path_insumos, name_uso_actual)
    gdf_uso_actual = gdf_uso_actual.to_crs(gdf_lc_terreno.crs) # reproyectando

    print(" - -  3.3. Uso potencial")

    name_uso_potencial = f"Usos/{name_uso_poten}"
    gdf_uso_potencial = read_capa_geo (path_insumos, name_uso_potencial)
    gdf_uso_potencial = gdf_uso_potencial.to_crs(gdf_lc_terreno.crs) # reproyectando

    # UAF
    print(" -   4. Leyendo UAF")
    
    name_uaf = f"UAF/{name_uaf}"
    gdf_uaf = read_capa_geo (path_insumos, name_uaf)
    gdf_uaf = gdf_uaf.to_crs(gdf_lc_terreno.crs) # reproyectando

    # ÁREAS MINIMAS
    print(" -   5. Leyendo áreas mínimas\n\n")
    
    name_area_minima = f"Areas_minimas/{name_areas_min}"
    gdf_area_minima = read_capa_geo (path_insumos, name_area_minima)
    gdf_area_minima = gdf_area_minima.to_crs(gdf_lc_terreno.crs) # reproyectando
    
    # INTERCEPTS 
    print(" - 6. Realizando intercepts")
    print(" - - 6.1. lc_terreno y áreas de actividad")
    gdf_inter_area_activ = gdf_lc_terreno.overlay(gdf_area_activ, how='intersection', keep_geom_type=True)
    gdf_inter_area_activ.dissolve(by=["etiqueta", "AREAS DE A"])
    gdf_inter_area_activ["area_actividad"] = gdf_inter_area_activ["AREAS DE A"]
    gdf_inter_area_activ["area_intercept"] = gdf_inter_area_activ.area
    gdf_inter_area_activ["porcentaje"] = gdf_inter_area_activ["area_intercept"]*100/gdf_inter_area_activ["area_terreno"]

    print(" - - 6.2. lc_terreno y uso actual")
    gdf_inter_uso_actual = gdf_lc_terreno.overlay(gdf_uso_actual, how='intersection', keep_geom_type=True)
    gdf_inter_uso_actual.dissolve(by=["etiqueta", "USO"])
    gdf_inter_uso_actual["area_intercept"] = gdf_inter_uso_actual.area
    gdf_inter_uso_actual["porcentaje"] = gdf_inter_uso_actual["area_intercept"]*100/gdf_inter_uso_actual["area_terreno"]

    print(" - - 6.3. lc_terreno y uso potencial")
    gdf_inter_uso_potencial = gdf_lc_terreno.overlay(gdf_uso_potencial, how='intersection', keep_geom_type=True)
    gdf_inter_uso_potencial.dissolve(by=["etiqueta", "USO"])
    gdf_inter_uso_potencial["area_intercept"] = gdf_inter_uso_potencial.area
    gdf_inter_uso_potencial["porcentaje"] = gdf_inter_uso_potencial["area_intercept"]*100/gdf_inter_uso_potencial["area_terreno"]

    print(" - - 6.4. lc_terreno y UAF")
    gdf_inter_uaf = gdf_lc_terreno.overlay(gdf_uaf, how='intersection', keep_geom_type=True)
    gdf_inter_uaf.dissolve(by=["etiqueta", "ZONA_HOMOGENEA"])
    gdf_inter_uaf["area_intercept"] = gdf_inter_uaf.area
    gdf_inter_uaf["porcentaje"] = gdf_inter_uaf["area_intercept"]*100/gdf_inter_uaf["area_terreno"]

    print(" - - 6.5. lc_terreno y áreas mímimas")
    gdf_inter_area_minima = gdf_lc_terreno.overlay(gdf_area_minima, how='intersection', keep_geom_type=True)
    gdf_inter_area_minima.dissolve(by=["etiqueta", "AREAS DE A"])
    gdf_inter_area_minima["area_actividad"] = gdf_inter_area_minima["AREAS DE A"]
    gdf_inter_area_minima["area_intercept"] = gdf_inter_area_minima.area
    gdf_inter_area_minima["porcentaje"] = gdf_inter_area_minima["area_intercept"]*100/gdf_inter_area_minima["area_terreno"]

    print("\n\n - 7. Construyendo reporte.xlsx")
    gdf_lc_terreno[["Resumen_Determinantes",	
                   "Reporte_USOS",	
                   "Reporte_UAF"]] = gdf_lc_terreno.apply(
                                    lambda x: ejecutar_funciones(x['etiqueta'], 
                                     gdf_resti, gdf_condi, 
                                     gdf_otros, gdf_inter_area_activ,
                                     gdf_inter_uso_actual, gdf_inter_uso_potencial,
                                     gdf_inter_uaf, gdf_inter_area_minima, fuente, porcen_intercept), axis=1)
    
    gdf_lc_terreno = gdf_lc_terreno[["etiqueta","Resumen_Determinantes",	
                                    "Reporte_USOS",	"Reporte_UAF", "area_terreno"]]
    
    name_output = "Determinantes_Usos_UAF_{}.xlsx".format(strftime('%d%m%Y_%H%M%Sh', localtime()))
    output = "/".join([path_insumos, name_output])
    gdf_lc_terreno.to_excel(output)


def ejecutar_funciones(etiqueta, gdf_resti, gdf_condi, 
                        gdf_otros, gdf_inter_area_activ,
                        gdf_inter_uso_actual, gdf_inter_uso_potencial,
                        gdf_inter_uaf, gdf_inter_area_minima, fuente, porcen_intercept):
    """
        Función general para ejecutar otras funciones
    """
    gdf_resti_filter = gdf_resti.loc[gdf_resti["QR"] == etiqueta]
    gdf_condi_filter = gdf_condi.loc[gdf_condi["QR"] == etiqueta]
    gdf_otros_filter = gdf_otros.loc[gdf_otros["QR"] == etiqueta]
    gdf_inter_uaf_filter = gdf_inter_uaf.loc[gdf_inter_uaf["etiqueta"] == etiqueta]
    gdf_inter_area_activ_filter = gdf_inter_area_activ.loc[gdf_inter_area_activ["etiqueta"] == etiqueta]
    gdf_inter_uso_actual_filter = gdf_inter_uso_actual.loc[gdf_inter_uso_actual["etiqueta"] == etiqueta]
    gdf_inter_uso_potencial_filter = gdf_inter_uso_potencial.loc[gdf_inter_uso_potencial["etiqueta"] == etiqueta]
    gdf_inter_area_minima_filter = gdf_inter_area_minima.loc[gdf_inter_area_minima["etiqueta"] == etiqueta]

    text_determinante = text_determinantes_predio(gdf_resti_filter, gdf_condi_filter, gdf_otros_filter,fuente)
    text_uaf = text_uaf_predio(gdf_inter_uaf_filter)
    text_uaf += texto_area_minima(gdf_inter_area_minima_filter, porcen_intercept)
    text_uso = text_usos_predio(gdf_inter_area_activ_filter, gdf_inter_uso_actual_filter, gdf_inter_uso_potencial_filter)

    return pd.Series([text_determinante, text_uso, text_uaf])



start = datetime.now()
start_timef = start.strftime("%Hh %Mm %Ss")
print(f"\n\n#### ---  Inicio: {start_timef} ---")

path_insumos, name_areas_min, name_restri, name_condi, name_otros, name_uaf, name_area_act, name_uso_act, name_uso_poten, name_lc_terreno, porcen_intercept, fuente = get_variables_xls()

get_capas_geo (path_insumos, name_areas_min, name_restri, name_condi, name_otros, name_uaf, name_area_act, name_uso_act, name_uso_poten, name_lc_terreno, porcen_intercept, fuente)

print("\n#### ------  Textos Automáticos Determinantes - Usos - UAF ------ ####")    
        
exec_time = datetime.now() - start
exec_time = str(exec_time).split(":")     
print('\n## -->  <--##')
print(f'## --> FINALIZADO: Tiempo de ejecución: {exec_time[0]}h {exec_time[1]}m {int(float(exec_time[2]))}s')
print("\n      ---------------------")
print("      |-    By: ljimj    -|")
print("      ---------------------")