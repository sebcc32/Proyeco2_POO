# Proyecto Actas de Grado

Sistema de información de la dirección de los posgrados en ingeniería de software de la Pontificia Universidad Javeriana Cali
que facilita la calificación de las actas de grado de maestría cuando los estudiantes realizan 
su sustentación pública. El sistema da la posibilidad de crear un archivo en formato PDF con los resultados de la 
calificación obtenida por el estudiante y los comentarios relacionados con la evaluación. Esta evaluación se registra
en un acta de evaluación que es diligenciada luego de la sustentación por los dos jurados participantes y está 
compuesta por:

* ID, fecha, autor, nombre del trabajo, tipo de trabajo (Aplicado o Investigación), director, 
co-director (si aplica), jurado uno y jurado dos. 
* Criterios de evaluación. Actualmente, son 8 criterios de evaluación, pero podrían extenderse en el futuro. 
Cada criterio tiene una descripción y un porcentaje de ponderación. El porcentaje de ponderación está definido por la dirección de los posgrados. 
Eventualmente, podría ser ajustados por el director. 
* En el acta para cada criterio de evaluación se incluye la calificación de acuerdo a la nota del jurado número uno y el 
jurado número dos, junto con las observaciones para el criterio. 
* El acta permite incluir observaciones adicionales y comentarios específicos sobre las condiciones para la 
aprobación del trabajo final.
* Al final de cada acta se incluye un espacio en el que los jurados ponen sus firmas. Además, de la calificación final de todos los criterios.
___
# Manual técnico
[![LINK](Imagenes/Imagen_UML.png)](https://drive.google.com/file/d/1MK1o4HypcTjOP_YV2KTAQA6Ou0AZGJEj/view?usp=sharing)

> **Class** `Acta`\
> Clase encargada de definir los valores que contiene cada una de las actas, recibe 
> del asistente el ID, fecha, autor, nombre del trabajo, tipo de trabajo (Aplicado o Investigación), director, codirector
> jurado 1 y 2, además de crear automáticamente la nota final y el diccionario de criterios con valores vacíos.
> Retornando al final un acta.

> **Class** `Criterio`\
> Clase encargada de definir uno de los criterios que contendrá un acta, recibe de uno de los jurados, la observación
 nota uno y nota dos, recibe automáticamente la descripción del criterio a evaluar y el ponderado del mismo. Esto se
> repite para cada uno de los criterios y como salida da un criterio calificado, cada uno se almacena y se envian en conjunto al
> acta que se está calificando.

> **Class** `EvaluadorController`\
> Clase encarga de almacenar las todas las actas dentro del sistema dentro de un diccionario,
> facilitando así el manejo de esta usando como Key el ID del acta.

> **Class** `MainView`\
> Clase en la cual se encuentra la vista del sistema. En este, se puede encontrar
> la división de los roles (Asistente, Jurado y Director). Cada uno de ellos tiene un menú único con los cargos específicos de su rol.
> \
> \
![](Imagenes/ImagenAsistente.png)
![](Imagenes/ImagenDirector.png)
![](Imagenes/ImagenJurados.png)
___
