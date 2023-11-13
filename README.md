# Taller IA guiado por Sainapsis 

En esta actividad, se realizaran preguntas sobre carreras de la Escuela Colombiana de Ingeniería. Se utilizó Pinecone para crear una base de datos de vectores, donde se almacenó la información de las carreras. Los documentos anexos, en este caso, FAQs de universidades, se cargaron utilizando Embeddings de OpenAI y Langchain.

El enfoque principal del taller fue aprender a utilizar Langchain, una herramienta esencial para crear agentes que empleen la técnica de Retrieval Augmented Generation (RAG). Además, se evaluaron buenas prácticas y clean code en Python.

Las tareas del taller incluyeron la configuración de una Tool de Langchain que consultara los documentos almacenados en la base de datos de vectores de Pinecone. La meta final fue la creación de un API REST que, al recibir un mensaje de usuario, lo procesara a través de un orquestador (API de Python ejecutando un agente de Langchain). Este proceso utilizaría la base de datos de vectores y los endpoints de OpenAI para el LLM, generando así una respuesta contextual y relevante.

## Desafio 1
Crear una base de datos de vectores en Pinecone Starter Version (https://www.pinecone.io/) 
usando su correo institucional, cargar los documentos anexos (FAQs de universidades) usando 
Embeddings de OpenAI y Langchain. Configurar una Tool de langchain que consulte los documentos 
y genere una respuesta.

# Pon el Proyecto en tu maquina

Estas instrucciones te ayudarán a tener una copia de este proyecto corriendo en tu máquina local, en donde podrás hacer pruebas o desarrollar sobre él.

## Prerrequisitos

Asegúrate de tener instaladas las siguientes tecnologías:

- Git
- Python
- Pip
-Pinecone (Sitio Web); https://www.pinecone.io/

![image](https://github.com/danielsperezb/Sainapsis_AREP/assets/101849347/88a679c4-c7fd-4773-a3d3-7a26e54099d6)


Te puedes guiar con lo siguiente:

- [Pip Instalación](https://pip.pypa.io/en/stable/installation/)

## Instalando 
Para hacer una copia local del proyecto, luego sigue lossiguientes comandos, para el pip debes estar dentro de el proyecto clonado, otra manera es descargar el .ZIP

```bash
git clone https://github.com/danielsperezb/Sainapsis_AREP.git

pip install -r requirements.txt

```

En Pycharm si creas el requirementes.txt te aparecera una opcion para instalarlos, de igual manera.
## Pruebas

 Se encontraron limitaciones en la realización de pruebas debido a la eliminación de la clave de OpenAI. No hay evidencia de funcionamiento hasta la fecha de este taller y La clave de API de OpenAI fue revocada al finalizar la clase de laboratorio.

## Autores

* **Daniel Esteban Perez** - Conoce mis repositorios visitando mi usuario

## Licencia

Este proyecto tiene la licencia GNU General Public License v3.0; consulte el archivo [LICENSE](LICENSE.txt) para obtener más información.

## Reconocimientos

+ David Esteban Useche – Líder técnico - david.useche@sainapsis.com
+ Santiago Velez – CoFounder – santiago.velez@sainapsis.com
* PurpleBooth - Plantilla para hacer un buen README
* Luis Daniel Benavides
* Monitor 




