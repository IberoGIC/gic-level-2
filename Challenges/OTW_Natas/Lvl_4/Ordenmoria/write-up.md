Al acceder desde el nivel anterior obtenemos el siguiente mensaje:
`Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"`

Cuando actualizamos la página desde el enlace _Refresh page_, el mensaje se actualiza:
`Access disallowed. You are visiting from "http://natas4.natas.labs.overthewire.org/index.php" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"`

Abrimos el inspector con `Ctrl + Shift + I` para analizar los encabezados HTTP, en la sección de *Red* vemos el encabezado de la solicitud:
```
GET /js/wechall.js HTTP/1.1 
Accept: */* 
Accept-Encoding: gzip, deflate 
Accept-Language: es-US,es-419;q=0.9,es;q=0.8,en;q=0.7 
Cache-Control: no-cache 
Connection: keep-alive 
Cookie: _ga=GA1.1.391681670.1734315220; _ga_RD0K2239G0=GS1.1.1734653824.5.0.1734653824.0.0.0 
Host: natas.labs.overthewire.org 
Pragma: no-cache 
Referer: http://natas4.natas.labs.overthewire.org/ User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36
```

Aquí `Referer` es la *key* que contiene la página desde dónde hacemos la solicitud:
`Referer: http://natas4.natas.labs.overthewire.org/`

La modificamos usando [Postman](https://www.postman.com/).

Ingresamos el URL del nivel http://natas4.natas.labs.overthewire.org/ con el método **GET**, en la sección de autenticación seleccionamos *Basic Auth* e ingresamos el usuario y contraseña para el nivel 4.

Al mandar la solicitud recibimos la página con el mensaje `Access disallowed`, lo que indica que las credenciales son correctas. 

Ahora vamos a la sección *Headers* y agregamos el *key* `Referer` con el valor `http://natas5.natas.labs.overthewire.org/`, al enviar la solicitud con el campo nuevo recibimos la página con el mensaje:
```
Access granted. The password for natas5 is passwordPlaceHolder 
```

---
## **Conclusión**

El nivel demuestra la importancia de los encabezados HTTP, en particular el uso del *key* `Referer` para validar la procedencia de las solicitudes. Aunque este encabezado puede ayudar a restringir el acceso, su manipulación es sencilla con herramientas como Postman o mediante scripts personalizados, resaltando que confiar únicamente en los encabezados HTTP para la autenticación o control de acceso es insuficiente y fácilmente evadible. 

---
-,"  
[_P