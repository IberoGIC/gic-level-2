Al comenzar el nivel nos recibe el texto `There is nothing on this page`. Comenzamos inspeccionando el código fuente y notamos que la contraseña no se encuentra a simple vista como en los niveles anteriores:

```html
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas2", "pass": "thisLevelPassword" };</script></head>
<body>
<h1>natas2</h1>
<div id="content">
There is nothing on this page
<img src="files/pixel.png">
</div>
</body></html>
```

Analizando el contenido de la página encontramos referencia a un archivo `pixel.png`

```html
<img src="files/pixel.png">
```

Cuando damos clic al enlace de la imagen nos lleva a la URL: http://natas2.natas.labs.overthewire.org/files/pixel.png

Aquí inferimos la siguiente distribución del directorio:
```
☁ natas2.natas.labs.overthewire.org/
├── 📂 files/ 
|	├── pixel.png # La imagen que se referencia
|	|...
|
└── index.html # La página del nivel
```

Modificamos el URL para ingresar al directorio `files/` en búsqueda de la contraseña: http://natas2.natas.labs.overthewire.org/files

Se nos muestra el contenido del directorio:
```
↩ Parent Directory
	pixel.png
	users.txt
```

Damos clic en el archivo `users.txt` y observamos el siguiente contenido:

```
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3: passwordPlaceHolder
eve:zo4mJWyNj2
mallory:9urtcpzBmH
```

La contraseña del siguiente nivel se encuentra junto al usuario `natas3`:

```
natas3: passwordPlaceHolder
```

---
## **Conclusión**

Una mala configuración en una página web puede llevar a que archivos sensibles queden disponibles para todo el mundo sin que lo queramos. Debemos cuidar dónde y cómo almacenamos la información sensible (*como contraseñas y usuarios*) dentro de un sitio web.

---
-,"  
[_P