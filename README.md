# Ren'Py Toolkit

**Ren'Py Toolkit** es una herramienta de escritorio para Windows que reúne pequeñas utilidades para facilitar la organización de proyectos desarrollados con [Ren'Py](https://www.renpy.org/).

Está pensada especialmente para creadores que están empezando a desarrollar novelas visuales y quieren evitar tareas repetitivas de organización y definición de recursos.

> **No necesitas saber programar para utilizar Ren'Py Toolkit.**

## Características

### 1. Crear estructura de carpetas

La herramienta puede crear automáticamente, dentro de la carpeta `game` de un proyecto Ren'Py, la siguiente estructura:

```text
game/
├── images/
│   ├── bg/
│   └── cg/
└── audio/
    ├── sfx/
    └── bgm/
```

Estas carpetas están pensadas para organizar:

- `images/bg` — fondos.
- `images/cg` — ilustraciones y CGs.
- `audio/sfx` — efectos de sonido.
- `audio/bgm` — música de fondo.

Si una carpeta ya existe, la herramienta no la elimina ni modifica su contenido.

### 2. Generar definiciones de imágenes

Ren'Py Toolkit puede recorrer `game/images`, incluyendo sus subcarpetas, y detectar automáticamente archivos:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`

A partir de ellos genera automáticamente las declaraciones de imagen de Ren'Py:

```renpy
image nombre = "ruta"
```

Estas definiciones se guardan en:

```text
game/images/definitions.rpy
```

El bloque generado está delimitado por:

```renpy
# AUTO START
# AUTO END
```

Esto permite actualizar las definiciones cuando se agregan o eliminan imágenes sin tener que escribir cada declaración manualmente.

Si `definitions.rpy` todavía no existe, Ren'Py Toolkit lo crea automáticamente con las marcas necesarias.

## Uso

1. Abre **Ren'Py Toolkit**.
2. Selecciona la carpeta `game` de tu proyecto de Ren'Py.
3. Utiliza una de las herramientas disponibles:
   - **Crear estructura de carpetas**
   - **Generar definiciones de imágenes**
4. Consulta el registro de actividad de la aplicación para comprobar las operaciones realizadas.

La aplicación valida que la carpeta seleccionada se llame `game` antes de realizar cambios.

## Requisitos

- Windows.
- Un proyecto creado con Ren'Py.
- No es necesario instalar Python para utilizar la versión ejecutable distribuida en Releases.

## Descarga

Las versiones compiladas para Windows se publican en la sección **Releases** de este repositorio.

Descarga siempre la versión correspondiente a la Release que quieras utilizar.

## Advertencia de seguridad de Windows

Las primeras versiones distribuidas de Ren'Py Toolkit pueden mostrar una advertencia de **Microsoft Defender SmartScreen** al ejecutar el archivo `.exe`.

Esto puede ocurrir porque el ejecutable todavía no dispone de una firma digital reconocida y Windows puede no tener suficiente reputación asociada al archivo o al editor. Una advertencia de SmartScreen no constituye por sí sola una determinación de que el programa contenga malware.

Mientras las versiones no estén firmadas, descarga el ejecutable únicamente desde las **Releases oficiales de este repositorio** y, si tienes dudas, puedes inspeccionar el código fuente antes de ejecutarlo.

El proyecto está solicitando actualmente el programa de **code signing de SignPath Foundation** para proporcionar a los usuarios una identidad de editor verificable y una procedencia verificable de las versiones distribuidas. La aceptación en el programa depende de la revisión de SignPath Foundation.

## Código abierto y transparencia

Ren'Py Toolkit es un proyecto de código abierto. El código fuente utilizado para construir las versiones distribuidas se encuentra disponible públicamente en este repositorio.

El objetivo es que los usuarios puedan inspeccionar el código y comprobar qué operaciones realiza la aplicación sobre sus proyectos.

La aplicación trabaja localmente con los archivos del proyecto que el usuario selecciona. No necesita enviar los archivos del proyecto a un servidor para crear las carpetas o generar las definiciones.

## Code signing policy

**Free code signing provided by SignPath.io, certificate by SignPath Foundation.**

Este proyecto está solicitando acceso al programa de firma de código de SignPath Foundation. Esta política se incluye para documentar el proceso de firma y cumplir con los requisitos del programa en caso de aprobación.

### Equipo del proyecto

**Committers and reviewers:** GabffeeDev

**Approvers:** GabffeeDev

GabffeeDev es el responsable del desarrollo, mantenimiento y control del repositorio de código fuente del proyecto.

Los cambios realizados por el mantenedor se publican en el repositorio oficial. Si el proyecto incorpora colaboradores externos en el futuro, los cambios propuestos por personas que no sean committers deberán ser revisados por un miembro autorizado del equipo antes de incorporarse al código que pueda ser firmado.

### Privacidad

> This program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it.

Ren'Py Toolkit no necesita transmitir a servidores externos los archivos del proyecto Ren'Py para realizar sus funciones principales.

### Proceso de publicación y firma

Las versiones oficiales se publican mediante **GitHub Releases**.

Los binarios distribuidos como Releases deben corresponder al código fuente y a los scripts de compilación publicados en este repositorio.

Si el proyecto es aceptado por SignPath Foundation, las versiones destinadas a firma se someterán al proceso de compilación, verificación y aprobación requerido por SignPath. Cada Release deberá recibir la aprobación necesaria antes de ser firmada.

Los binarios firmados deberán ser construidos de forma verificable a partir del código fuente correspondiente del repositorio.

## Seguridad

Ren'Py Toolkit no está diseñado para modificar la configuración de seguridad de Windows, evadir mecanismos de seguridad ni identificar o explotar vulnerabilidades.

La herramienta únicamente realiza las operaciones necesarias para organizar la estructura de archivos de un proyecto Ren'Py y generar definiciones de imágenes.

Si encuentras un comportamiento inesperado o un posible problema de seguridad, abre un Issue en este repositorio.

## Desarrollo

El proyecto está desarrollado en Python y utiliza principalmente la biblioteca estándar para su interfaz gráfica y operaciones de archivos.

La interfaz utiliza Tkinter.

## Licencia

Ren'Py Toolkit se distribuye bajo la **Licencia MIT**. Consulta el archivo [`LICENSE`](LICENSE) para conocer los términos completos.

La licencia permite utilizar, copiar, modificar y redistribuir el software de acuerdo con sus condiciones.

## Ren'Py

Ren'Py es un motor de código abierto para crear novelas visuales y otras experiencias narrativas interactivas.

Ren'Py Toolkit es una herramienta independiente de la organización Ren'Py y no forma parte oficialmente de Ren'Py.

## Estado del proyecto

Ren'Py Toolkit se encuentra en desarrollo y se encuentra en sus primeras versiones públicas. Las herramientas actuales se centran en tareas sencillas de organización de proyectos y generación automática de definiciones de imágenes.

El proyecto se mantiene públicamente en GitHub y las versiones compiladas se distribuyen mediante GitHub Releases. La adopción del proyecto todavía está creciendo, por lo que no se presentan cifras de usuarios o descargas que no puedan verificarse públicamente.

Se planean futuras herramientas para facilitar otros aspectos del desarrollo de novelas visuales con Ren'Py.

---

## Información para mantenedores

Para mantener la elegibilidad para el programa de firma de SignPath Foundation, el proyecto debe continuar cumpliendo las condiciones aplicables al programa, incluyendo el uso de una licencia open source aprobada por OSI, mantenimiento activo, publicación de versiones, documentación, control del código fuente y buenas prácticas de seguridad.

Los miembros del equipo que tengan acceso al repositorio y a los sistemas de firma deben utilizar autenticación multifactor (MFA/2FA), según las condiciones del programa.

Consulta las condiciones actuales de SignPath Foundation antes de realizar cambios en el proceso de compilación o publicación.
