Se nos muestra una página idéntica en apariencia al nivel anterior. 
En comparación el código fuente no contiene el enlace a la imagen del nivel anterior, sino que contiene un comentario:

`<!-- No more information leaks!! Not even Google will find it this time... -->`

Recordando la distribución anterior, modificamos el URL para intentar acceder al directorio `files/`:  http://natas3.natas.labs.overthewire.org/files

Pero nos encontramos con un *error 404*:
```html
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
<hr>
<address>Apache/2.4.58 (Ubuntu) Server at natas3.natas.labs.overthewire.org Port 80</address>
</body></html>

```

Analizamos la pista que nos dan y  realizando la búsqueda: `which pages can not be indexed by google?` obtenemos la siguiente información:

> Google doesn't index **pages that are blocked by a robots.txt** rule or noindex tag, or pages that are duplicates of other pages on your site, or pages that are inappropriate to index them (for example, variations of a page with different filters applied).

>  [Page Indexing report - Search Console Help](https://support.google.com/webmasters/answer/7440203?hl=en#zippy=%2Cnon-experts-usage-guide%2Cis-it-ok-if-a-page-isnt-indexed)

Deducimos que la página web contiene un archivo `robots.txt` y modificamos el URL para acceder a él: http://natas3.natas.labs.overthewire.org/robots.txt

Se nos muestra el siguiente contenido:
```
User-agent: *
Disallow: /s3cr3t/
```

Aquí inferimos la siguiente distribución del directorio:
```
☁ natas3.natas.labs.overthewire.org/
├── 📂 s3cr3t/ 
|	|...
|
└── index.html # La página del nivel
```

Modificamos el URL para ingresar al directorio `s3cr3t/`: https://natas3.natas.labs.overthewire.org/s3cr3t y se nos muestra el contenido del directorio:
```
↩ Parent Directory
	users.txt
```

La contraseña del siguiente nivel se muestra al abrir el archivo `users.txt`:

```
natas4: passwordPlaceHolder
```

---
## **Conclusión**

Aunque la configuración adecuada del archivo `robots.txt` ayuda a evitar que ciertos directorios aparezcan en los resultados de búsqueda web, no impide el acceso directo a archivos. Esto demuestra que no es una medida de seguridad suficiente y que se deben implementar protecciones adicionales, especialmente cuando se manejan contraseñas u otra información sensible.

---
-,"  
[_P