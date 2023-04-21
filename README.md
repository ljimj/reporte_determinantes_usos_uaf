# __REPORTES AUTOMÁTICOS - Determinantes - Usos - UAF__
Generación de reportes automáticos de predios que cruzan espacialmente con Determinantes - Usos - UAF del Plan de Ordenamiento Social de la Propiedad Rural - POSPR.

### __Instalación__

Instalar python
`Python`

En consola ubicarse en la dirección donde se descargo este repositorio y ejecutar:
```
pip install -r requirements.txt
```
para instalar los paquetes requeridos
### __Crear estructura de carpetas y archivos de insumo__

![Estructura Carpetas](/assets/Estructura_Carpetas.jpg)

- Capa Terreno (.shp o .gpkg)
    - Campos necesarios | `etiqueta` |
- Capa áreas mínimas (Carpeta)
    - AREAS_MINIMAS_ADJUDICABLES_SIN_UAF (.shp o .gpkg)
        - Campos necesarios | `AREAS DE A` |
- Determinantes (Carpeta)
    - Capa Restricciones (.shp o .gpkg) 
        - Campos necesarios |`CAPA_GEO` | `AREA_CRUCE` | `PORCENTAJE` |
    - Capa Condicionantes (.shp o .gpkg)
        - Campos necesarios |`CAPA_GEO` | `AREA_CRUCE` | `PORCENTAJE` |
    - Capa Otros cruces (.shp o .gpkg)
        - Campos necesarios |`CAPA_GEO` | `AREA_CRUCE` | `PORCENTAJE` |
- UAF (Carpeta)
    - Capa UAF (.shp o .gpkg)
        - Campos necesarios |`ZONA_HOMOGENEA` | `NOMBRE_ZONA_HOMOGENEA` | `UNIDAD_AGRICOLA_FAMILIAR_MINIMA` | `UNIDAD_AGRICOLA_FAMILIAR_MAXIMA` | `UNIDAD_AGRICOLA_FAMILIAR` |
- Usos (Carpeta)
    - Capa Área actividad (.shp o .gpkg)
        - Campos necesarios | `AREAS DE A` |
    - Capa Uso actual (.shp o .gpkg)
        - Campos necesarios | `USO` |
    - Capa Uso potencial (.shp o .gpkg)
        - Campos necesarios | `USO` |

### __Editar archivo Variables.xlsx__
Editar columna <`Nombre`> con la ruta de la carpeta y nombres de los archivos descritos en el anterior paso

### __Ejecutar la aplicación con:__
En consola ubicarse en la dirección donde se descargo este repositorio y ejecutar:
``` 
python reportes.py 
```
### __Resultado__
El reporte resultado (.xlsx) se guarda en la `carpeta estructurada` de los archivos insumo

###### *`geopandas`* - *`pandas`*

*`by: Leonardo Jimenez Joven`*
