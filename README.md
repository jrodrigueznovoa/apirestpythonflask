# apirestpythonflask
Desarrollo apirest python con Flask

1.- Crear un directorio del proyecto, copiar todos los archivos del desarrollo para que funcione correctamente, 
esto se encuentra en la carpeta apirest_haulmer

2.-instalar virtualenv abrir cmd y ejecutar el siguiente comando
#pip install virtualenv 

3.- en la raiz del directorio creado se debe crear un entorno virtual
para crearlo solo debe ejecutar en el terminal cmd 
#virtualenv venv
 
4.- al revisar la carpeta raiz se creara una carpeta venv ingrese 
#cd venv/Scripts y ejecute activate.bat despues vuelva a la raiz de su proyecto

5.ejecutar los siguientes comandos a traves de cmd
#pip install Flask
#pip install Flask-RESTful
#pip install Flask-JWK
#pip install requests

5.-para ejecutar la app debe ingresar a /code y ejecutar

#py app.py

En el caso que tenga el puerto 5000 utilizado, lo puede cambiar a otro en el archivo /code/constantes.py
puerto = <puerto>

Si desea utilizar docker siga los siguientes pasos de todas maneras revisar el archivo DockerFile

1.- en la raiz de la carpta del proyecto
#docker build -t apirestflask .

2.- para revisar imagen creada ejecute el siguiente comando
#docker images

3.-Ejecutar el siguiente comando para ejecutar su proyecto
#docker run -it --publish 7000:5000 apirestflask

en Postaman debera utilizar el nuevo puerto en este caso 7000
