El nivel nos presenta un formulario con un campo `secret` y un botón de envío, junto con un breve código en PHP:

```php
<?  
  
include "includes/secret.inc";  
  
    if(array_key_exists("submit", $_POST)) {  
        if($secret == $_POST['secret']) {  
        print "Access granted. The password for natas7 is <censored>";  
    } else {  
        print "Wrong secret";  
    }  
    }  
?>
```

Este compara el texto que ingresamos en el formulario con una variable `$secret` contenida en la biblioteca `secret.inc`, si ambas cadenas son iguales nos muestra la contraseña, en caso contrario nos muestra el mensaje `Wrong secret`.

Debido a que `$secret` está siendo llamada a través de una biblioteca no podemos observar su valor en el código ni los recursos de la página web.

Analizando la biblioteca, notamos que se encuentra dentro del directorio `includes/` e inferimos la siguiente distribución del directorio:
```
☁ natas6.natas.labs.overthewire.org/
├── 📂 includes/
|   └── secret.inc # Biblioteca que contiene $secret
|
└── index.php # La página del nivel
```

Modificamos el URL para acceder al archivo:
http://natas6.natas.labs.overthewire.org/includes/secret.inc y se nos muestra el siguiente contenido:
```php
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
```

Enviando la cadena `FOEIUWGHFEEUHOFUOIU` en el formulario de la página, obtenemos la contraseña:
```
Access granted. The password for natas7 is passwordPlaceHolder
```


---
## **Conclusión**

La seguridad no debe depender de ocultar información en el código, sino de implementaciones que impidan su exposición accidental o maliciosa. Al incluir recursos sin asegurar su acceso, se abre una puerta a posibles vulnerabilidades que pueden ser explotadas por atacantes. 

---
-,"  
[_P