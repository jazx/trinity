# trinity
Pequeño y liviano asistente para linux escrito en python.
Esta basado en markopolo, pero ha sido modificado para mejorar su eficacia en el procesamiento de las ordenes recibidas.

### Descripcion:
Se trata de una version un poco mas elaborada que su predecesor markopolo, al menos en lo referido al analisis de sintaxis. Pues esta version realiza dos analisis de texto.
- El primero detecta elementos generales. Normalmente OBJETOS sobre los que recae la accion (ej: MUSICA, VIDEO, IMAGENES). Y dirige el procesamiento al "SECTOR" de ese objeto.
- El segundo analisis de sintaxis, con un segundo diccionario especifico del sector, realiza una segunda clasificación de terminos. Pudiendo, de esta manera, generar una interpretacion mas eficiente de la accion solicitada.


### Dependencias del servidor:
- python3

Cada cliente tiene su propio README.

