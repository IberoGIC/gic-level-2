Este nivel contiene únicamente un enlace para ver el código fuente. Al revisarlo, notamos que, al enviar el campo `revelio`, la página verifica el valor de `admin` en la sesión. Si no se cumple este requisito, nos redirige a la página principal; en caso de ser administradores, la página muestra la contraseña del siguiente nivel.
```php
<?php
session_start();

if(array_key_exists("revelio", $_GET)) {
    // only admins can reveal the password
    if(!($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1)) {
    header("Location: /");
    }
}
?>

...

<?php
    if(array_key_exists("revelio", $_GET)) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas23\n";
    print "Password: <censored></pre>";
    }
?>
```

Por la forma en que está implementada la página, la contraseña aparece en la respuesta de la solicitud, pero la redirección es tan rápida que no se muestra en el navegador. Esto se puede solucionar fácilmente con el comando  `curl` en Linux.

`curl` es una herramienta de línea de comandos que permite realizar solicitudes HTTP/HTTPS directamente desde la terminal. En este caso, podemos usar `curl` para capturar la respuesta de la solicitud antes de la redirección. Para usarlo debemos configurar la autenticación básica (*Basic Auth*) mediante el argumento `-u`, seguido del nombre de usuario y la contraseña en el formato `usuario:contraseña`.
```bash
curl -u natas22:contraseña http://natas22.natas.labs.overthewire.org?revelio
```

- **`-u`** Credenciales de autenticación básica
- **`http://`** URL del nivel
- **`?revelio`**: Parámetro enviado en la solicitud

Este comando mostrará en la terminal la respuesta completa de la solicitud, incluyendo la contraseña del siguiente nivel antes de que ocurra la redirección.

---
## **Conclusión**
 
Este nivel demuestra cómo las redirecciones rápidas pueden ocultar información importante de la vista del usuario en el navegador, pero no de las respuestas completas del servidor, por eso no debemos confiar únicamente en redirecciones como medida de seguridad y hay que asegurarse de que la información sensible no sea enviada en las respuestas.

---
-,"  
[_P