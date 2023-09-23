sobre los archivos excel con nombres "Ingresos y gastoa municipales XXXX.xls

estos archivos tienen alguna incompatibilidad para su lectura con python, la solución fue abrirlos con excel y guardarlos como .xlsx
les cambié el nombre para evitar usar espacios y mayusculas, pero su contenido está intacto
se revisó que todos tuvieran el mismo "offset" de filas respecto al inicio para indicar este parámetro en la función de pandas que lee archivos excel


--------------------------------
sobre archivos de detalle cat y rol cobro

quedarán en una carpeta aparte
se incluyen los glosarios de cada uno de tipo de datos, que se usan para la lectura y estructuración de los datos en dataframes de pandas