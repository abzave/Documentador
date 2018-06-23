# Documentador

Funcionalidades implementadas:
Crea la documentación interna de cualquier programa escrito en Python. El archivo a documentar puede encontrarse en la misma dirección que el procente programa o también podrá especificarsele una ruta en la que buscar.

Explicación paso a paso:
Una vez abierto el programa este mostrará un listado con todos los archivos con extensión .py en la carpeta actual. Aquí hay dos posibilidades, si el archivo a documentar se encuentra en la misma carpeta que el programa deberá ingresar el número en el que esté listado el archivo. También, si el archivo está en otro lugar, puede ingresar la ruta en que se desea buscar, esto volverá a listar todos los archivos .py que haya en la nueva ruta.

Cuando ya esté seleccionado el archivo el archivo, este preguntará si desea documentar cada función o método encontrada. Para afirmar que se desea documentar dicha función o método puede ingresar cualquier cosa, para negarlo ingrese -1, lo que hará que se pase a la siguiente función. Cabe destacar que si la función ya se encuentra documentada o es un __init__ o un getter o setter no se le preguntará sobre esta.

Al aceptar que se desea documentar una función se le preguntará por el tipo de dato de cada parametro, siempre cunado estos existan o el parametro no sea un self. Luego, se prosigue consultado por las salidas de la función o método y por último sobre el funcionamiento de este. El proceso se repite hasta que ya no haya más funciones o métodos en el archivo.

Una vez termidas las funciones y/o métodos el archivo ya se encontrará totalmente documentado y se le consultará si desea continuar. Al ingresar S el programa se reiniciará, y al ingresar N saldrá del programa
