El nivel nos presenta un buscador de palabras similar a los niveles 9 y 10, aunque ahora con un filtrado más extenso:
```php
<?  
$key = "";  
  
if(array_key_exists("needle", $_REQUEST)) {    $key = $_REQUEST["needle"];  
}  
  
if($key != "") {  
    if(preg_match('/[;|&`\'"]/',$key)) {  
        print "Input contains an illegal character!";  
    } else {        passthru("grep -i \"$key\" dictionary.txt");  
    }  
}  
?>
```

Una diferencia importante es que ahora el valor de `$key` se encierra entre comillas dobles, esto complica la solución, porque lo que escribamos dentro del formulario se usará como texto literal, impidiendo que usemos comandos directamente, en contraste con los niveles anteriores.

Podemos evadir esto por medio de sustitución de comandos, donde ejecutamos un comando interior, se captura su salida y se sustituye dentro del comando exterior:

```bash
grep -i "$(grep /etc/natas_webpass/natas17)" dictionary.txt
```

Ahora se presenta un nuevo desafío, aunque podemos ejecutar comandos, estos se sustituyen como una cadena literal dentro del `grep` exterior, lo que causa que se utilicen como patrón de búsqueda en el archivo `dictionary.txt` y al no contener la cadena de la contraseña, este no da ninguna salida.

Una forma de enfrentar esto es simular una salida booleana, utilizamos una palabra que sabemos que existe en el diccionario, por ejemplo *exists* y le concatenamos la salida de un `grep` interno, por medio de sustitución de comandos, si el `grep` interno coincide con la contraseña, esta se concatena a la palabra *exists* y causa que el `grep` exterior no tenga salida, por el contrario, si el `grep` interno no coincide con la contraseña, entonces el `grep` externo nos dará de salida la palabra *exist*.

De esta forma construimos un comando como este:
```bash
grep -i "$(grep ^a.* /etc/natas_webpass/natas17)^exists" dictionary.txt
```

* `^` | Representa el inicio de una línea, evitando una coincidencia a mitad de la contraseña
* `.*` | `.`  representa cualquier carácter y `*` es la repetición de este , juntos sirven de comodín para coincidir cualquier cadena

Cambiando el carácter en la búsqueda eventualmente no aparecerá la palabra *exists*, indicando que encontramos el primer carácter de la contraseña, si agregamos este carácter al inicio podemos seguir la búsqueda con los demás caracteres.

```bash
$(grep ^Ea.* /etc/natas_webpass/natas17)^exists
```

Dado que las contraseñas contienen 32 caracteres que pueden ser mayúsculas, minúsculas o números, es conveniente realizar un [script](https://github.com/IberoGIC/gic-level-2/blob/main/Challenges/OTW_Natas/Lvl_16/Ordenmoria/script.py) que automatize este proceso.

---
## **Conclusión**

 Aunque el filtrado inicial evita inyecciones directas, un conocimiento amplio del shell y su uso estratégico puede evadir las restricciones del código, permitiendo ejecutar comandos indirectamente. 
 
 Es importante ser estrictos con la limpieza de las entradas de usuario y usar herramientas de búsqueda más seguras o consultas parametrizadas.

---
-,"  
[_P
