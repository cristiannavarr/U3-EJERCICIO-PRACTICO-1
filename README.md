# Programa para resolver operaciones matemáticas

Programa de python que lee problemas matemáticos (suma, resta, multiplicación, división y potencia) de un csv, los resuelve y modifica el archivo para agregar los resultados.

# Estructura del proyecto

├── data/

│   └── math_operations.csv      # CSV inicial que será modificado

├── data-reference/

│   └── math_operations.csv      # Copia del CSV original antes de ser modificado

├── main.py                      # Archivo para ejecutar el programa

├── math_operations.py           # Funciones para ejecutar las operaciones matemáticas

├── data_processor.py            # Lee el CSV y agregar los resultados

├── requirements.txt             # Dependencias requeridas

└── README.md                    # Información del proyecto


# Como ejecutarlo:

Correr el archivo main.py y revisar los resultados en consola.


# Comentarios adicionales

1. La carpeta data-reference contiene el CSV original que fue obtenido siguiendo los pasos descritos en la guía de la actividad:


    "Clona el repositorio en tu máquina local:
    git clone https://github.com/JhennerTigreros/UNICIENCIA-INTRO-PROGRAMACION
    Navega al directorio del proyecto:
    cd UNICIENCIA-INTRO-PROGRAMACION
    Asegúrate de tener instalado Python 3 y crea el directorio data
    Ejecuta el generador de los datos.
    python mini_proyecto-1.py
    Revisa el archivo CSV en data/math_operations.csv"

    Este archivo no será modificado, se deja solo como referencia para que se pueda revisar el archivo inicial con el que se trabajó.
    
    Este archivo no contiene ninguna columna mostrando los resultados correctos, entonces no hay resultados de referencia para verificar los resultados obtenidos,      así que le verificación se hace visual/manualmente solo con los primeros resultados.

2. Algunas operaciones de potencia generan resultados demasiado grandes, estos resultados serán escritos como "Result too large" ya que calcularlos genera error de overflow en Python.

3. No se requirieron dependencias adicionales.

4. El programa ya fue ejecutado, entonces el archivo data > math_operations.csv ya fue modificado por el programa. Si se quiere volver a ejecutar el programa para verificar su funcionamiento remplazar el archivo data > math_operations.csv por el original que se encuentra en data-reference > math_operations.csv.





