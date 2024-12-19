Bienvenido al directorio de **OverTheWire: Natas**, una serie de retos diseñados para aprender y desarrollar habilidades en vulnerabilidades web. Estos desafíos forman parte del **Nivel 2** y tienen como objetivo fortalecer tu comprensión de la seguridad en aplicaciones web.

---
## 🔍 **¿Qué es OverTheWire?**

OverTheWire es una plataforma educativa que ofrece una variedad de retos CTF (Capture The Flag) enfocados en conceptos fundamentales de seguridad informática. Cada serie de retos está orientada a un tema específico como Linux, redes, criptografía y vulnerabilidades web.
* Página oficial: [https://overthewire.org/](https://overthewire.org/)

---
## 👁‍🗨 **¿Qué es Natas?**

Natas es un *wargame* sobre conceptos básicos de seguridad web. Cada nivel presenta un sitio web **vulnerable**, y tu objetivo es descubrir la contraseña (flag) que te permite avanzar al siguiente nivel.

Cada nivel de Natas consiste en su propio sitio web localizado en:

```
http://natasX.natas.labs.overthewire.org
```

Donde **X** es el número del nivel correspondiente. No existe acceso mediante **SSH**.

- Para acceder a un nivel, introduce el **nombre de usuario** correspondiente (por ejemplo, `natas0` para el nivel 0) y su **contraseña**.
    
- Cada nivel tiene acceso a la **contraseña del siguiente nivel**.
    
- Tu trabajo es obtener de alguna manera esa contraseña y avanzar al siguiente nivel.

### **Ubicación de las Contraseñas**

Todas las contraseñas también están almacenadas en la ruta:

```
/etc/natas_webpass/
```

Por ejemplo, la contraseña de **natas5** se encuentra en el archivo:

```
/etc/natas_webpass/natas5
```

Este archivo solo puede ser leído por los usuarios **natas4** y **natas5**.

**Requisitos:**

* Conocimientos básicos de HTML, HTTP y herramientas de navegación web.
* Familiaridad con comandos básicos de Linux y scripts simples.

---
## **📝 Cómo Resolver los Retos**

Sigue estos pasos generales para abordar cada nivel:

1. **Lee el enunciado**: Analiza la descripción del nivel y el objetivo.
    
2. **Inspecciona la página**:
    
    - Revisa el **código fuente** con DevTools (clic derecho → Ver código fuente).
        
    - Analiza los **elementos y las cookies**.
    
3. **Prueba entradas y parámetros**:
    
    - Manipula formularios, parámetros en la URL y solicitudes HTTP.
	
4. **Encuentra la flag**: La solución será una contraseña oculta.
    
5. **Documenta tu proceso**:
    
    - Guarda comandos, herramientas y pasos utilizados en un **write-up**.

---
## **🚀 Buenas Prácticas**

- Lee y comprende el **objetivo de cada nivel** antes de probar soluciones.
	
- Discute ideas y comparte herramientas con otros miembros *(no spoilers)*. 
    
- Usa herramientas éticamente y **no ataques sitios externos**.
    
- Documenta tu solución siguiendo la plantilla de write-ups.
    
- Colabora y pide ayuda si te atoras. ¡El aprendizaje es grupal!

---
## **📜 Reglas de OverTheWire**

El objetivo de los juegos de OverTheWire es proporcionar recursos educativos gratuitos a quienes deseen aprender sobre ciberseguridad. Al usar estos recursos, es necesario seguir estas reglas básicas:

- **No hagas spoilers**: Evita compartir soluciones en chats públicos. Si necesitas ayuda, menciona el juego y nivel, y busca asistencia mediante mensajes privados.

- **Limpieza**: Si creas archivos o directorios durante los retos, elimínalos al finalizar.

- **Evita nombres obvios**: No uses nombres fáciles de adivinar para tus archivos o directorios.

- **No publiques credenciales**: Evita publicar nombres de usuario o contraseñas de los juegos.

---
## **🔧 Primeros Pasos**

* Accede al primer nivel de Natas [aquí](http://natas0.natas.labs.overthewire.org).
	* Username : natas0
	* Password  : natas0
* Si te atoras consulta [Lvl-0/hint.md]().
- Compara tu solución con las disponibles en [Lvl-0/write-ups.md](), si encuentras una nueva solución y quieres contribuirla, hazlo siguiendo está guía: [contributing.md]().
	*No olvides firmar tu solución.*
- Una vez completes el nivel actualiza tu *xp* en [progress.md]().

---

¡🚀 Completa los retos, documenta tu progreso y prepárate para el siguiente nivel! Si tienes dudas, consulta con el equipo del GIC o abre una [Discussion](https://github.com/IberoGIC/gic-level-2/discussions) en este repositorio.

---
-,"  
[_P