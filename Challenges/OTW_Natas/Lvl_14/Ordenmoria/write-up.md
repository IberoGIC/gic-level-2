El nivel nos presenta un registro de usuario, en el código vemos que se implementa a través de un *query* en MYSQL:
```php
 $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";  
    if(array_key_exists("debug", $_GET)) {  
        echo "Executing query: $query<br>";  
    }  
  
    if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {  
            echo "Successful login! The password for natas15 is <censored><br>";  
    } else {  
            echo "Access denied!<br>";  
    }
```

Si la consulta devuelve al menos un resultado, se permite el acceso.

Nota:
	Analizando el código, vemos que es posible mostrar en la página el *query* que se ejecuta, en lugar de solo suponerlo. Para ello modificamos la URL agregando la opción de `debug` y enviando a través de `GET` los datos de ingreso:
	`http://natas14.natas.labs.overthewire.org/index.php?debug=true&username=user&password=pass`
	Esto no es estrictamente necesario para completar el nivel, y de hecho resulta un poco molesto completarlo de esta forma, pero puede ser útil para visualizar mejor la consulta en la base de datos.

El método estrella para resolver este nivel es [SQL Injection](https://learn.microsoft.com/es-es/sql/relational-databases/security/sql-injection?view=sql-server-ver16) , y existen muchas consultas que se pueden construir para este propósito, la elegida aquí es:
```sql
 SELECT * from users where username="" or 1# and password=""
```
Donde:
* username toma el valor `" or 1#` 
* password se deja en blanco

`1` es tomado como `TRUE` dentro de SQL, esto provoca que la condición se cumpla para todos los registros de la tabla, ya que independientemente del usuario o contraseña, verdadero siempre será verdadero. Al realizar la consulta se seleccionan todos los registros de la tabla, dado que la condición era tener al menos una selección, esta se cumple y el registro se completa.


---
## **Conclusión**

Siempre debemos dudar del usuario, la falta de validación de entradas es la puerta para múltiples ataques.

Además, el dejar herramientas del desarrollo en el producto final, como uso del parámetro `debug`, facilita la identificación de vulnerabilidades.

---
-,"  
[_P




