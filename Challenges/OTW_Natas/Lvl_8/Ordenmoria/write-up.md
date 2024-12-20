La apariencia es la misma del nivel 6, al acceder el código fuente notamos algunas similitudes:

```php
<?  
  
$encodedSecret = "3d3d516343746d4d6d6c315669563362";  
  
function encodeSecret($secret) {  
    return bin2hex(strrev(base64_encode($secret)));  
}  
  
if(array_key_exists("submit", $_POST)) {  
    if(encodeSecret($_POST['secret']) == $encodedSecret) {  
    print "Access granted. The password for natas9 is <censored>";  
    } else {  
    print "Wrong secret";  
    }  
}  
?>
```

Al igual que el otro nivel, este compara el texto que ingresamos en el formulario, aunque ahora encriptado, con una variable `$encodedsecret`, si ambas cadenas son iguales nos muestra la contraseña, en caso contrario nos muestra el mensaje `Wrong secret`.

Aquí  el valor de `$encodedsecret` se encuentra a simple vista:
```php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";  
```

Analizando la función `encodeSecret` identificamos la siguiente cadena de encriptación:
```
$secret -> to base64 -> reverse -> to Hex -> $encodedSecret
```

Sabiendo el valor que debe tener `$encodedSecret` podemos revertir esta cadena capa por capa:
```
$encodedSecret -> from Hex -> reverse -> from base64 -> $secret
```

Usando [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')Reverse('Character')From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=M2QzZDUxNjM0Mzc0NmQ0ZDZkNmMzMTU2Njk1NjMzNjI) obtenemos la siguiente cadena como resultado:
```
oubWYf2kBq
```

Enviando la cadena `oubWYf2kBq` en el formulario de la página, obtenemos la contraseña:
```
Access granted. The password for natas9 is passwordPlaceHolder
```

---
## **Conclusión**

Este nivel resalta lo importante que es evitar exponer datos sensibles, incluso si están cifrados o codificados, ya que con suficiente información, es posible descifrar o revertir estas transformaciones. La seguridad de una aplicación no debe depender solo de ofuscar información, sino de métodos que protejan activamente la información crítica.

---
-,"  
[_P