La página web muestra el texto `You can find the password for the next level on this page`. Inspeccionando el código fuente de la página con *clic derecho > Ver código fuente*, vemos el siguiente archivo html:

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
<script>var wechallinfo = { "level": "natas0", "pass": "natas0" };</script></head>
<body>
<h1>natas0</h1>
<div id="content">
You can find the password for the next level on this page.

<!--The password for natas1 is passwordPlaceHolder -->
</div>
</body>
</html>
```

La contraseña del siguiente nivel se encuentra comentada:
`<!--The password for natas1 is passwordPlaceHolder -->`

---
## **Conclusión**

Este nivel introduce conceptos fundamentales sobre la inspección de código fuente. Familiarizarnos con estas capacidades del navegador web es importante, ya que será lo primero que revisemos para próximos niveles.

---
-,"  
[_P