La página web muestra el texto `You can find the password for the next level on this page, but rightclicking has been blocked!`. Cuando intentamos dar clic derecho, salta una alerta con el texto `right clicking has been blocked!`.

Podemos ver el código fuente de la página con los siguientes atajos:
* Ver código fuente `Ctrl + U`
* Inspeccionar página `Ctrl + Shift + I`

Y observamos el siguiente archivo html:

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
<script>var wechallinfo = { "level": "natas1", "pass": "0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq" };</script></head>
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">
<h1>natas1</h1>
<div id="content">
You can find the password for the
next level on this page, but rightclicking has been blocked!

<!--The password for natas2 is passwordPlaceHolder -->
</div>
</body>
</html>

```

Nuevamente la contraseña del siguiente nivel se encuentra comentada:
`<!--The password for natas2 is passwordPlaceHolder -->`

---
## **Conclusión**

Este nivel nos obliga a buscar nuevas formas de ver el código fuente, ahora podremos usar estos atajos para analizar los siguientes niveles.

---
-,"  
[_P