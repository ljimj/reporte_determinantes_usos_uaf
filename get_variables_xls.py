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

import pandas as pd
import os

def get_variables_xls():
    """
        Función para extraer las variables
        almacenadas en el archivo xlsx
    """
    current_path = os.path.abspath(os.getcwd())
    path_xlsx = f"{current_path}\Variables.xlsx"
    df_varibles = pd.read_excel(path_xlsx, dtype=str)
    # path insumos
    path_insumos = df_varibles.loc[df_varibles["Variable_Capa"] == 'Ruta Carpeta']['Nombre'].values[0]
    # name capa área mínimas
    name_areas_min = df_varibles.loc[df_varibles["Variable_Capa"] == 'Áreas mínimas']['Nombre'].values[0]
    # name capa restricciones
    name_restri = df_varibles.loc[df_varibles["Variable_Capa"] == 'Restricciones']['Nombre'].values[0]
    # name capa condicionantes
    name_condi = df_varibles.loc[df_varibles["Variable_Capa"] == 'Condicionantes']['Nombre'].values[0]
    # name capa otros cruces
    name_otros = df_varibles.loc[df_varibles["Variable_Capa"] == 'Otros cruces']['Nombre'].values[0]
    # name capa UAF
    name_uaf = df_varibles.loc[df_varibles["Variable_Capa"] == 'UAF']['Nombre'].values[0]
    # name capa area actividad
    name_area_act = df_varibles.loc[df_varibles["Variable_Capa"] == 'Área actividad']['Nombre'].values[0]
    # name capa Uso actual
    name_uso_act = df_varibles.loc[df_varibles["Variable_Capa"] == 'Uso actual']['Nombre'].values[0]
    # name capa Uso potencial
    name_uso_poten = df_varibles.loc[df_varibles["Variable_Capa"] == 'Uso potencial']['Nombre'].values[0]
    # name capa lc_terreno
    name_lc_terreno = df_varibles.loc[df_varibles["Variable_Capa"] == 'Terreno']['Nombre'].values[0]
    # name capa Porcentaje intercept
    porcen_intercept = df_varibles.loc[df_varibles["Variable_Capa"] == 'Porcentaje intercept']['Nombre'].values[0]
    # name capa Uso potencial
    fuente = df_varibles.loc[df_varibles["Variable_Capa"] == 'Fecha Geoproceso ANT']['Nombre'].values[0]

    return path_insumos, name_areas_min, name_restri, name_condi, name_otros, name_uaf, name_area_act, name_uso_act, name_uso_poten, name_lc_terreno, porcen_intercept, fuente
