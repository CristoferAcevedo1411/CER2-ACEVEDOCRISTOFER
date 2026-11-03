# CER2-ACEVEDOCRISTOFER

Catálogo digital de lugares patrimoniales (Fundación Patrimonio Vivo) hecho
con Django. Incluye zona pública y una zona de gestión con autenticación y permisos.

## Requisitos

Python 3.12 o superior
pip
Conexión a internet (Bootstrap, fuentes e imágenes se cargan desde la web)

## Instalación y ejecución

```
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_datos
python manage.py createsuperuser
python manage.py runserver
```

Abrir http://127.0.0.1:8000/

## Usuarios y permisos de prueba

Las contraseñas no se incluyen en el repositorio; se definen al crear los usuarios.

1. Entrar a http://127.0.0.1:8000/admin/ con el superusuario creado arriba.
2. En **Usuarios**, crear `gestor` y asignarlo al grupo **Gestores**
   (puede agregar y editar lugares). El grupo lo crea `cargar_datos`.
3. Crear `lector` sin grupo (entra a `/gestion/`, pero no puede agregar ni editar).

Para probar los permisos usar `gestor` y `lector`, no el superusuario, porque
este tiene todos los permisos.