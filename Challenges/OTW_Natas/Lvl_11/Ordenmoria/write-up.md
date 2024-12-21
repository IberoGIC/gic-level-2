El nivel nos presenta el mensaje `Cookies are protected with XOR encryption` y un formulario de campo `bgcolor`.

Al inspeccionar las cookies identificamos una de nombre `data` con el valor `HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=`, analizando el código notamos que se trata de `$defaultdata`, que contiene los valores de `showpassword` y `bgcolor`, a través de una cadena de cifrado:
```
$defaultdata -> json encode -> xor -> base64 encode -> data (Cookie)
```
```php
<?
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");  

function saveData($d) {    
	setcookie("data", base64_encode(xor_encrypt(json_encode($d))));  
}  
  
$data = loadData($defaultdata);  
  
saveData($data);  
?>  
```

*Si modificamos el valor de `showpassword` almacenado en la cookie se mostrará la contraseña.*

Sabiendo el valor original de `$defaultdata` y su valor después del cifrado XOR (`data`), podemos aprovechar las propiedades de la operación para recuperar la `key` usada.
$$ \begin{align} defaultdata \oplus key = cookie\\ defaultdata \oplus cookie = key \end{align} $$

Recordando que debemos decodificar en Base64 la cookie, y convertir `$defaultdata` a JSON, dada la cadena de cifrado inversa:
```
data (Cookie) -> base64 decode -> xor -> json decode -> $defaultdata
```

Haciendo esta operación a través  de [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)XOR(%7B'option':'UTF8','string':'%7B%22showpassword%22:%22no%22,%22bgcolor%22:%22%23ffffff%22%7D'%7D,'Standard',false)&input=SG1Za0J3b3pKdzRXTnlBQUZ5QjFWVWNxT0UxSlpqVUlCaXM3QUJkbWJVMUdJakVKQXlJeFRSZz0) obtenemos la siguiente salida:
```
eDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoe
```
Se trata de la `key` (`eDWo`), repetida varias veces debido a su largo menor, a comparación de `$defaultdata`.

Ahora podemos cifrar con XOR la cookie modificando el valor de `showpassword`, nuevamente usamos [CyberChef](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'UTF8','string':'eDWo'%7D,'Standard',false)To_Base64('A-Za-z0-9%2B/%3D')&input=eyJzaG93cGFzc3dvcmQiOiJ5ZXMiLCJiZ2NvbG9yIjoiI2ZmZmZmZiJ9) y obtenemos la siguiente cadena:
```
HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc5
```

Reemplazando el valor de la cookie (`data`) con esta cadena se muestra la contraseña del siguiente nivel.

---
## **Conclusión**

En este nivel se destaca que aunque los métodos de cifrado simples pueden ser útiles en situaciones no críticas, no son adecuados para proteger información sensible en aplicaciones reales.  El uso de XOR en este contexto es riesgoso porque es un algoritmo simétrico, y si no se implementa correctamente con una clave única y suficientemente larga, puede ser fácilmente reversible. Además, al depender de cookies, el sistema no ofrece protección contra modificaciones externas, lo que facilita la alteración de los datos.

---
-,"  
[_P