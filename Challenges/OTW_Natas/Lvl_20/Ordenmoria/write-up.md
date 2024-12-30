La página consiste en un formulario para cambiar el nombre de usuario. Después de usarla un par de veces, notamos que no ofrece ningún tipo de feedback sobre nuestras acciones. Revisando el código, observamos que existe un modo de [debug](http://natas20.natas.labs.overthewire.org/index.php?debug=true). Al usarlo y compararlo con el código fuente, notamos el siguiente flujo del programa:

* `myread()` verifica que el ID de sesión sea válido
```php
if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
    debug("Invalid SID");
        return "";
    }
```

* Si `SID` es válido, revisa si existe un archivo para la sesión
```php
$filename = session_save_path() . "/" . "mysess_" . $sid;
    if(!file_exists($filename)) {
        debug("Session file doesn't exist");
        return "";
    }
```

* Si no existe un archivo de sesión, `mywrite()` verifica que el ID de sesión sea válido, crea el archivo y guarda el nombre de usuario
```php
    $filename = session_save_path() . "/" . "mysess_" . $sid;
    $data = "";
    debug("Saving in ". $filename);
    ksort($_SESSION);
    foreach($_SESSION as $key => $value) {
        debug("$key => $value");
        $data .= "$key $value\n";
    }
    file_put_contents($filename, $data);
```

* Si existe un archivo de sesión, `myread()` lee el contenido del archivo y lo descompone en pares de valores `key value`, para guardarlos en la sesión
```php
    debug("Reading from ". $filename);
    $data = file_get_contents($filename);
    $_SESSION = array();
    foreach(explode("\n", $data) as $line) {
        debug("Read [$line]");
    $parts = explode(" ", $line, 2);
    if($parts[0] != "") $_SESSION[$parts[0]] = $parts[1];
    }
    return session_encode() ?: "";
```

* Si la sesión tiene almacenado el valor `admin 1` se muestran las credenciales del siguiente nivel.
```php
function print_credentials() { /* {{{ */
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas21\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.";
    }
}
```

Al analizar la manera en que se almacenan y leen los valores de la sesión, llegamos a la conclusión de que, simulando el formato del archivo de sesión, podemos agregar la clave `admin` con el valor `1` a nuestra sesión para obtener privilegios de administrador

* Archivo de sesión con usuario `realAdmin`
```
name realAdmin
```
* Archivo de sesión con usuario `realAdmin\nadmin 1`
```
name realAdmin
admin 1
```

Esto podemos lograrlo usando la codificación de URL, donde:
* `%0A` Representa un salto de línea.
* `%20` Representa un espacio

```
http://natas20.natas.labs.overthewire.org/index.php?debug=true&name=realAdmin%0Aadmin%201
```

Al cargar la [URL](http://natas20.natas.labs.overthewire.org/index.php?debug=true&name=realAdmin%0Aadmin%201) por primera vez, se modificará el nombre de usuario, cuando recargamos la página, al leer el archivo de sesión, el valor de `admin` se modificará, dándonos la contraseña del siguiente nivel.

---
## **Conclusión**
 
No validar adecuadamente el contenido de los archivos, especialmente los de sesión, es una vulnerabilidad que puede ser explotada fácilmente. Para prevenir este tipo de ataques, es necesario implementar no solo la validación de los datos, sino también técnicas de almacenamiento seguro, como el cifrado de los archivos de sesión.

---
-,"  
[_P
