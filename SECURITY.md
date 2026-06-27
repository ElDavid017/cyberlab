# SECURITY.md - Práctica de Laboratorio No. 4
**Estudiante:** David Guerrero
**Materia:** Ethical Hacking - Octavo Semestre
**Universidad:** ULEAM, Extensión El Carmen

---

## Q0: ¿Por qué un rastreador de incidentes sin autenticación es un problema de seguridad?

Si cualquier persona puede abrir /incidents/ sin iniciar sesión, un atacante que encuentre la URL puede ver todos los reportes de vulnerabilidades de la organización. Básicamente le damos un mapa de qué sistemas están fallando. Es una de las peores cosas que se pueden exponer públicamente porque le facilita al atacante saber exactamente por dónde entrar.

## Q1: Modelo User vs UserProfile — ¿por qué OneToOneField?

El modelo `User` de Django maneja todo lo relacionado con autenticación (usuario, contraseña, sesiones). `UserProfile` es donde guardamos datos adicionales que Django no conoce por defecto, como el campo `role`. Usamos `OneToOneField` porque cada usuario debe tener exactamente un perfil y viceversa. Si modificáramos directamente el modelo `User` de Django tendríamos que reemplazar todo el sistema de autenticación, lo cual es mucho más complicado y propenso a errores.

## Q2: Propósito del parámetro ?next= y riesgo de redirección abierta

Cuando Django te manda al login porque intentaste acceder a una ruta protegida, guarda a dónde ibas en el parámetro `?next=`. Después de iniciar sesión te lleva ahí. El problema de seguridad es que si Django no verifica que la URL de `next` pertenece al mismo sitio, un atacante podría crear un enlace como `/accounts/login/?next=http://sitio-malicioso.com` y después del login el usuario es redirigido al sitio del atacante. Eso se llama Open Redirect y se usa mucho en ataques de phishing.

## Q3: Autenticación vs Autorización — ejemplos concretos del laboratorio

La **autenticación** es verificar quién eres. En este lab es el formulario de login que comprueba usuario y contraseña.

La **autorización** es verificar qué tienes permitido hacer una vez que ya iniciaste sesión. En este lab las vistas de editar y eliminar verifican si tu perfil tiene `role='admin'` antes de dejarte continuar.

Si omites la autorización, cualquier usuario autenticado (incluyendo analistas) podría ir directamente a `/incidents/1/edit/` y modificar o borrar lo que quiera.

## Q4: commit=False y riesgo de asignación masiva

Usamos `commit=False` para pausar el guardado en la base de datos y asignar `reported_by = request.user` desde el servidor antes de guardar. Si en cambio hubiera un campo oculto en el formulario HTML para `reported_by`, cualquiera podría abrir las herramientas de desarrollador, cambiar el valor y enviar el formulario haciéndose pasar por otro usuario. Eso es un ataque de asignación masiva (Mass Assignment). Con `commit=False` el usuario nunca controla ese campo.

## Q5: ¿Por qué ocultar botones en la plantilla NO es suficiente seguridad?

Ocultar los botones de Editar y Eliminar en el HTML solo cambia lo que se muestra en el navegador. Alguien puede escribir directamente `/incidents/1/edit/` en la barra de direcciones y acceder a la vista sin problema. Esto se llama navegación forzada (Forced Browsing) y está relacionado con IDOR. La protección real tiene que estar en la vista con la verificación del rol, no en el HTML.

## Q6 (Bonus): Ataques de fuerza bruta y django-axes

Un ataque de fuerza bruta es cuando alguien crea un script que prueba miles de combinaciones de usuario/contraseña contra el formulario de login hasta que una funciona. `django-axes` lo mitiga rastreando cuántos intentos fallidos vienen de una IP y bloqueándola después de `AXES_FAILURE_LIMIT` fallos. Si el límite se pone muy bajo (como 2 o 3) los usuarios reales que simplemente se equivoquen al escribir su contraseña quedan bloqueados. Otro método para proteger el login es agregar un CAPTCHA para que los scripts automatizados no puedan enviar el formulario.
