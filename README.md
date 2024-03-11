## En nuestro proyecto, creamos una carpeta que llamamos "python" donde introduciremos la carpeta "lib", que está ubicada en ".venv".
![Adición de la carpeta lib a la carpeta python](/img/Screenshot_20240311_174746.png)

## Una vez hecho esto comprimiremos la carpeta "python" utilizando el siguiente comando.
    zip -r -q discord.zip python/

## Ya comprimida la carpeta nos dirigimos a Lambda y creamos una función en la que añadiremos un programa cuya función es mandar un mensaje a nuestro servidor de discord.
![Compresión de carpeta](/img/Screenshot_20240311_175320.png )

## A continuación creamos una capa, a la que le asignaremos un nombre y cargaremos la carpeta comprimida en pasos anterioires.
![Creación de capa](/img/Screenshot_20240311_175642.png)

## Por último le añadimos la capa creada a nuestra función.
![Adición de capa a nuestra función](/img/Screenshot_20240311_175823.png)

## La comprobación la realizaremos invocando nuestra función y revisando si el mensaje ha sido enviado al Discord.
![Comprobación del funcionamiento](/img/Screenshot_20240311_180024.png)