# Desarrollo, prueba y publicacion con Azure Functions Core Tools

Azure Functions Core Tools se compone de utilidades de línea de comandos que permiten desarrollar y ejecutar funciones de forma local y publicarlas en Azure. En esta sesión vamos a usar Azure Functions Core Tools desde la CLI de Azure para crear una aplicación de funciones y un proyecto de Functions locales. Vamos a modificar el código de inicio generado por Core Tools para ejecutar un cálculo de interés simple y a ejecutar la función de forma local para probarla. Y para terminar, vamos a usar la CLI de Azure para crear una aplicación de funciones en Azure, publicar la función y luego invocarla a través de Internet.

## Enlaces relevantes para esta sesión

- [Desarrollo, prueba y publicación de funciones de Azure Functions mediante Azure Functions Core Tools](https://aka.ms/AzureFunctionsCoreTools5)


## Objetivos de aprendizaje

Al final de este módulo va a poder usar Azure Functions Core Tools para:

- Crear nuevos proyectos y funciones de Functions
- Ejecutar y probar funciones en un entorno local
- Publicar funciones en Azure

## Requisitos previos

- Experiencia de desarrollo de principiante con Azure Functions
- Familiaridad con el uso básico de la línea de comandos

## Qué es Azure Functions Core Tools

Azure Functions Core Tools es un conjunto de herramientas de línea de comandos que se puede usar para desarrollar y probar funciones de Azure Functions en el equipo local.

Core Tools incluye una serie de funcionalidades relacionadas con las funciones, aunque su finalidad principal es:

1. Generar los archivos y las carpetas necesarios para desarrollar funciones en el equipo local
2. Ejecutar las funciones de forma local para poder probarlas y depurarlas
3. Publicar las funciones en Azure

Core Tools se empaqueta como una utilidad de línea de comandos denominada `func`

Otras herramientas de desarrollo de Functions, como las características relacionadas con Functions de Visual Studio y la extensión Azure Functions para Visual Studio Code, se basan en Core Tools.

## Creación de funciones localmente

Cada función publicada en Azure pertenece a una aplicación de funciones, que es una colección de una o más funciones que se publican juntas en el mismo entorno. Todas las funciones de una aplicación de funciones comparten un conjunto común de valores de configuración y se deben compilar para el mismo entorno de ejecución de lenguaje.

Al desarrollar funciones de forma local, se trabaja en un proyecto de Functions, que es una carpeta que contiene el código y los archivos de configuración que definen las funciones. Un proyecto de Functions en el equipo equivale a una aplicación de funciones en Azure y puede contener varias funciones que usan el mismo runtime de lenguaje.

### `func init`

Para crear un proyecto de Functions, ejecute `func init` en la línea de comandos.

func init le pregunta qué runtime de lenguaje quiere usar para la aplicación y adapta el contenido de la carpeta del proyecto en consecuencia.

Al crear un nuevo proyecto de Functions, los archivos incluidos en la carpeta del proyecto dependen del runtime de lenguaje que se seleccione. Independientemente del runtime seleccionado, los dos archivos de proyecto más importantes siempre están presentes:

host.json almacena valores de configuración del runtime, como opciones de registro, para la aplicación de funciones. La configuración almacenada en este archivo se usa cuando se ejecutan funciones en local y en Azure.
local.settings.json almacena valores de configuración que solo se aplican a la aplicación de funciones cuando se ejecuta localmente con Core Tools. Este archivo contiene dos tipos de configuración: configuración del runtime local, que se usa para configurar el propio runtime de funciones local, y la configuración de la aplicación personalizada, que se puede agregar y configurar en función de las necesidades de la aplicación y a la que todas las funciones de la aplicación pueden acceder y usar.
Los proyectos de Functions que genera func init no tienen ninguna función incluida.

### `func new`

Cada función individual de un proyecto necesita código y configuración para definir su comportamiento. Al ejecutar func new en una carpeta de proyecto de Functions, se crean una nueva función y todos los archivos necesarios para empezar el desarrollo.

### `func start`

Las funciones no son programas que se pueden ejecutar por sí solos: deben hospedarse. El host de Functions es lo que acciona todo fuera del código de la función: carga la configuración, escucha a los desencadenadores y las solicitudes HTTP, inicia el proceso de trabajo del lenguaje en el que se han escrito las funciones, escribe la salida del registro, etc. En Azure, las aplicaciones de funciones ejecutan el host de Functions automáticamente al iniciarse.

Para iniciar el host de Functions en el entorno local, ejecute func start desde una carpeta de proyecto de Functions.

## Publicar una función en Azure con Core Tools

Para usar Core Tools a fin de publicar un proyecto, es necesario crear una aplicación de funciones en Azure. Esta no es una funcionalidad de Core Tools. La creación de aplicaciones de funciones se realiza mediante las herramientas de administración de Azure.

Para publicar un proyecto de Functions en Azure, ejecute `func azure functionapp publish <app_name>` desde la carpeta del proyecto de Functions. `<app_name>` es el nombre de la aplicación de funciones de destino en Azure, no el nombre de la carpeta del proyecto, que puede ser diferente.