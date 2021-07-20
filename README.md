# Proyectos_Web_Scrapping
En este repositorio muestro los proyectos de Web Scrapping aplicados a diferentes objetivos y mediante diferentes técnicas.

# **PROYECTO 1**:newspaper:
## Extraccion de datos desde el diario ámbito financiero:

El proyecto busca poder obtener mediante el lenguaje de Python y Xpath la información del reconocido diario de noticias Ámbito Financiero. Básicamente, mediante la utilizacion combinada de Python y Xpath se extrae el título, el copete y el desarrollo de cada una de las noticias que se encuentran en el momento en la web del diario. Y una vez obtenida dicha informacion, se crea una carpeta con el nombre de la fecha de hoy (DD-MM-AAAA) dentro de la cúal se guardan en diferentes archivos .txt toda la informacion citada anteriormente (título, copete y desarrollo de la noticia), con lo cual esto resulta útil para poder realzar diferentes análisis de esa información y tomar decisiones en base a ello. 
En segunda instancia se genera mediante la libreria WordCloud una nube de palabras eliminando mediante la libreria ntkl ( que corresponde al procesamiento del lenguaje natural) las palabras que hacen ruido y que no aportan al analisis. Finalmente con la nube de palabras que se observa se puede analizar cuales son las que mas aparecen en las noticias, siendo las mas grandes las que se observan con mayor frecuencia.
