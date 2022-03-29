# trinity
Pequeño y liviano asistente para linux escrito en python.
Esta basado en markopolo, pero ha sido modificado para mejorar su eficacia.
Tambien corre sin necesidad de google-chrome haciendo uso de algunas minimas dependencias

Incluye
- palabra de activacion (trinity)
- reconocmiento de voz (usando el servicio gratuito de google)
- comandos personalizados configurados mediante scripts de bash


### Funcionamiento:
Se trata de una version un poco mas elaborada que su predecesor markopolo, al menos en lo referido al analisis de sintaxis. Pues esta version realiza dos analisis de texto.
- El *primer analisis de sintaxis* detecta elementos generales. Normalmente OBJETOS sobre los que recae la accion (ej: MUSICA, VIDEO, IMAGENES). Y dirige el procesamiento al **sector** de ese objeto. Esta primera clasificacion se realiza utilizando los filtros del archivo **'server/brain/dictionary1.conf'**
- El *segundo analisis de sintaxis*, con un segundo diccionario especifico del sector, realiza una segunda clasificación de terminos. Pudiendo, de esta manera, generar una interpretacion mas eficiente de la accion solicitada. Esta segunda clasificacion se realiza utilizando los filtros del archivo **'SECTOR/dictionary2.conf'** .

Hay, por lo tanto, un solo archivo *dictionary1.conf* . No obstante, hay tantos archivos *dictionary2.conf* como sectores existan. Cada sector incluye un diccionario. Permitiendo de esa forma especificar menos ambiguamente las acciones de ciertas palabras.
Esto permite lidiar mas efectivamente contra la ambigüedad de muchas expresiones verbales.

Por ejemplo:
Dentro del sector VOLUMEN, la palabra "bajar" equivale normalmente a la accion de "disminuir".
Mientras que dentro del sector INTERNET, la palabra "bajar" suele equivaler a la accion de "descargar/download".
Con el uso de los dos filtros se pueden configurar con presicion el significado de las palabras.

Para el uso de los diccionarios puede ver la documentacion y los videos de markopolo.


Cada cliente tiene su propio README.

### Como ejecutar en Ubuntu y derivados:

- Descargar/clonar este repositorio
- Instalar Dependencias

        sudo apt install python3-pyaudio libatlas-base-dev screen
        
- Ejecutar:

        ./run_trinity.sh                     (para iniciar el asistente)
        ./stop_trinity.sh                    (para detener el asistente)
        

