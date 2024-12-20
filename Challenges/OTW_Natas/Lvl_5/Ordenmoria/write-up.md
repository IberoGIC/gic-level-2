Al acceder al nivel obtenemos el siguiente mensaje:
`Access disallowed. You are not logged in`

Abrimos el inspector con `Ctrl + Shift + I` para analizar los encabezados HTTP, pero no identificamos nada relevante.

Nos dirigimos a la sección de *Aplicación* para revisar las **Cookies**, aquí vemos un campo sospechoso `loggedin` con valor `0`, modificamos el valor del campo a `1` y forzamos a recargar la página  con `Ctrl + F5`.

Ahora obtenemos el mensaje con la contraseña:
```
Access granted. The password for natas6 is passwordPlaceHolder
```

---
## **Conclusión**

Este nivel resalta la importancia de las cookies para control de sesión y autenticación en aplicaciones web.

La solución demuestra que confiar únicamente en el lado del cliente para gestionar la autenticación es inseguro, ya que valores como las cookies pueden ser fácilmente modificados.

---
-,"  
[_P