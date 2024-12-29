En este nivel, tenemos un registro de usuario en el cual, al iniciar sesión, se muestra un mensaje que indica si somos usuarios regulares o administradores.
```
You are logged in as a regular user. Login as an admin to retrieve credentials for natas19.
```
 
Al revisar el código, observamos que la diferenciación se realiza a través de un valor `admin` almacenado para cada sesión del lado del servidor.
```php
function print_credentials() { /* {{{ */
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas19\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas19.";
    }
}
```

Se muestra una función capaz de cambiar este valor, pero se encuentra desactivada.
```php
function isValidAdminLogin() { /* {{{ */
    if($_REQUEST["username"] == "admin") {
    /* This method of authentication appears to be unsafe and has been disabled for now. */
        //return 1;
    }
    
    return 0;
}
```

El ID de la sesión se almacena como una cookie en el navegador.
```php
function my_session_start() { /* {{{ */
    if(array_key_exists("PHPSESSID", $_COOKIE) and isValidID($_COOKIE["PHPSESSID"])) {
    if(!session_start()) {
        debug("Session start failed");
        return false;
    } else {
        debug("Session start ok");
        if(!array_key_exists("admin", $_SESSION)) {
        debug("Session was old: admin flag set");
        $_SESSION["admin"] = 0; // backwards compatible, secure
        }
        return true;
    }
    }
    
    return false;
}
```

Y vemos que existe un número máximo de ID para las sesiones generadas.
```php
$maxid = 640; // 640 should be enough for everyone
```

Con esta información, podemos deducir que, dentro del número limitado de sesiones, debe existir alguna que tenga el valor `admin = 1`. Dado que el ID de sesión se almacena en la cookie `PHPSESSID`, podemos crear un [script](https://github.com/IberoGIC/gic-level-2/blob/main/Challenges/OTW_Natas/Lvl_18/Ordenmoria/script.py) que pruebe cada ID hasta encontrar uno que corresponda a una sesión de administrador.

---
## **Conclusión**
 
 Incluso las configuraciones aparentemente inofensivas, como limitar el rango de IDs de sesión, pueden ser explotadas. Al identificar un rango limitado de IDs de sesión y con fuerza bruta, logramos encontrar una sesión activa con privilegios de administrador.

Es necesario generar IDs de sesión no predecibles y establecer límites de intentos o implementar CAPTCHA para prevenir ataques de fuerza bruta.

---
-,"  
[_P