Este nivel consiste en un formulario con el campo `passwd`. Al analizar el código, vemos que la contraseña debe cumplir con dos condiciones:
```php
<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas24 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>
```

1.  `strstr($_REQUEST["passwd"],"iloveyou"`: La contraseña debe contener la cadena `"iloveyou"`
2. `$_REQUEST["passwd"] > 10 `: La contraseña debe ser mayor a 10

Podríamos pensar que no es posible que **la contraseña sea mayor a 10** debido a que es una cadena, pero en PHP esto es posible gracias a la coerción de tipos (*Type coercion*), que es la habilidad de un lenguaje de programación para convertir automáticamente un tipo de dato en otro para realizar una operación. PHP es un lenguaje de tipado débil, lo que significa que las variables no tienen un tipo fijo y PHP determina dinámicamente el tipo según el contexto.

Cuando realizamos una comparación numérica (`<`, `>`, `==`, etc.) sobre una cadena, PHP intenta interpretar la cadena como un número siguiendo estas reglas:
1. Si la cadena comienza con caracteres numéricos, PHP usa esos caracteres como el número.
* `"123abc"` se convierte en `123`
* `"10.5hola"` se convierte en `10.5`
2. Si la cadena no comienza con un número, se trata como `0`
* `"abc123"` se convierte en `0`
- `"hola"` se convierte en `0`
3. Las cadenas que son **estrictamente numéricas** (por ejemplo, `"42"`, `"3.14"`) se convierten directamente en sus equivalentes numéricos.

Conociendo el comportamiento de PHP en estas condiciones, podemos construir una contraseña que cumpla ambas reglas:
```
11iloveyou
```
* `strstr($_REQUEST["passwd"], "iloveyou")` devuelve `"iloveyou"` (Verdadero)
* `$_REQUEST["passwd"] > 10` interpreta `11iloveyou` como `11` y devuelve Verdadero


---
## **Conclusión**
 
Para evitar problemas relacionados con la comparación y coerción de tipos en PHP y otros lenguajes de tipado débil, es fundamental seguir buenas prácticas. Usar comparaciones estrictas (`===`) garantiza que tanto el valor como el tipo sean correctos, evitando comportamientos inesperados. También es importante realizar conversiones explícitas de tipos y limpiar las entradas para validar las cadenas antes de procesarlas, reduciendo así el riesgo de errores y vulnerabilidades.

---
-,"  
[_P