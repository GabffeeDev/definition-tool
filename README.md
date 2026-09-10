# Ren'Py Toolkit

**Ren'Py Toolkit** es una herramienta de escritorio para Windows que
reúne pequeñas utilidades para facilitar la organización de proyectos
desarrollados con [Ren'Py](https://www.renpy.org/).

Está pensada especialmente para creadores que están empezando a
desarrollar novelas visuales y no quieren realizar manualmente tareas
repetitivas de organización y definición de recursos.

> **No necesitas saber programar para utilizar Ren'Py Toolkit.**

## Características

### 1. Crear estructura de carpetas

La herramienta puede crear automáticamente, dentro de la carpeta `game`
de un proyecto Ren'Py, la siguiente estructura:

``` text
game/
├── images/
│   ├── bg/
│   └── cg/
└── audio/
    ├── sfx/
    └── bgm/
```

Estas carpetas están pensadas para organizar:

-   `images/bg` --- fondos.
-   `images/cg` --- ilustraciones y CGs.
-   `audio/sfx` --- efectos de sonido.
-   `audio/bgm` --- música de fondo.

Si una carpeta ya existe, la herramienta no la elimina ni modifica su
contenido.

### 2. Generar definiciones de imágenes

Ren'Py Toolkit puede recorrer `game/images`, incluyendo sus subcarpetas,
y detectar automáticamente archivos:

-   `.png`
-   `.jpg`
-   `.jpeg`
-   `.webp`

A partir de ellos genera automáticamente las declaraciones de imagen de
Ren'Py:

``` renpy
image nombre = "ruta"
```

Estas definiciones se guardan en:

``` text
game/images/definitions.rpy
```

El bloque generado está delimitado por:

``` renpy
# AUTO START
# AUTO END
```

Esto permite actualizar las definiciones cuando se agregan o eliminan
imágenes sin tener que escribir cada declaración manualmente.

Si `definitions.rpy` todavía no existe, Ren'Py Toolkit lo crea
automáticamente con las marcas necesarias.

## Uso

1.  Abre **Ren'Py Toolkit**.
2.  Selecciona la carpeta `game` de tu proyecto de Ren'Py.
3.  Utiliza una de las herramientas disponibles:
    -   **Crear estructura de carpetas**
    -   **Generar definiciones de imágenes**
4.  Consulta el registro de actividad de la aplicación para comprobar
    las operaciones realizadas.

La aplicación valida que la carpeta seleccionada se llame `game` antes
de realizar cambios.

## Requisitos

-   Windows.
-   Un proyecto creado con Ren'Py.
-   No es necesario instalar Python para utilizar la versión ejecutable
    distribuida en Releases.

## Descarga

Las versiones compiladas para Windows se publican en la sección
**Releases** de este repositorio.

Descarga siempre la versión correspondiente a la Release que quieras
utilizar.

## Advertencia de seguridad de Windows

Las primeras versiones distribuidas de Ren'Py Toolkit pueden mostrar una
advertencia de **Microsoft Defender SmartScreen** al ejecutar el archivo
`.exe`.

Esto puede ocurrir porque el ejecutable todavía no dispone de una firma
digital reconocida y, por tanto, Windows no puede establecer una
reputación suficiente para el archivo o su editor.

La advertencia no significa por sí misma que el programa contenga
malware.

Para aumentar la confianza y verificar la procedencia de las versiones
distribuidas, el proyecto está preparado para utilizar **code signing**
mediante SignPath Foundation cuando sea aprobado.

Una vez que una Release esté firmada, descarga siempre el ejecutable
desde la Release oficial de este repositorio y verifica que corresponde
a la versión publicada.

## Código abierto y transparencia

Ren'Py Toolkit es un proyecto de código abierto. El código fuente
utilizado para construir las versiones distribuidas se encuentra
disponible públicamente en este repositorio.

El objetivo es que los usuarios puedan inspeccionar el código y
comprobar qué operaciones realiza la aplicación sobre sus proyectos.

La aplicación trabaja localmente con los archivos del proyecto que el
usuario selecciona. No necesita enviar los archivos del proyecto a un
servidor para crear las carpetas o generar las definiciones.

## Code signing policy

**Free code signing provided by SignPath.io, certificate by SignPath
Foundation.**

### Equipo del proyecto

**Committers / Authors:**\
GabffeeDev

**Reviewers:**\
GabffeeDev

**Approvers:**\
GabffeeDev

El responsable del proyecto mantiene el código fuente y el repositorio
oficial del proyecto.

Las versiones firmadas se construyen a partir del código fuente y de los
archivos de compilación disponibles en este repositorio.

### Privacidad

This program will not transfer any information to other networked
systems unless specifically requested by the user or the person
installing or operating it.

Ren'Py Toolkit no necesita transmitir a servidores externos los archivos
del proyecto Ren'Py para realizar sus funciones principales.

### Proceso de publicación

Las versiones oficiales se publican mediante GitHub Releases.

Los binarios distribuidos como Releases deben corresponder al código
fuente publicado en este repositorio.

Las versiones que utilicen la firma de SignPath Foundation se someterán
al proceso de firma y aprobación requerido por SignPath.

## Seguridad

Ren'Py Toolkit no está diseñado para modificar la configuración de
seguridad de Windows, evadir mecanismos de seguridad ni identificar o
explotar vulnerabilidades.

La herramienta únicamente realiza las operaciones necesarias para
organizar la estructura de archivos de un proyecto Ren'Py y generar
definiciones de imágenes.

Si encuentras un comportamiento inesperado o un posible problema de
seguridad, abre un Issue en este repositorio.

## Desarrollo

El proyecto está desarrollado en Python y utiliza principalmente la
biblioteca estándar para su interfaz gráfica y operaciones de archivos.

La interfaz utiliza Tkinter.

## Licencia

Este proyecto debe distribuirse bajo una licencia de código abierto
aprobada por la Open Source Initiative (OSI).

Consulta el archivo `LICENSE` incluido en este repositorio para conocer
los términos exactos de distribución y uso.

> **Nota para los mantenedores:** antes de solicitar la firma gratuita
> de SignPath Foundation, asegúrate de que el repositorio incluya una
> licencia OSI-approved aplicable a todos los componentes del proyecto y
> que no exista una doble licencia comercial.

## Ren'Py

Ren'Py es un motor de código abierto para crear novelas visuales y otras
experiencias narrativas interactivas.

Ren'Py Toolkit es una herramienta independiente de la organización
Ren'Py y no forma parte oficialmente de Ren'Py.

------------------------------------------------------------------------

### Estado del proyecto

Ren'Py Toolkit se encuentra en desarrollo. Las herramientas actuales se
centran en tareas sencillas de organización de proyectos y generación
automática de definiciones de imágenes.

Se planean futuras herramientas para facilitar otros aspectos del
desarrollo de novelas visuales con Ren'Py.
