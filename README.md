# 📝 API de Tareas con Flask

API REST desarrollada en Python con Flask para la gestión de tareas
(To-Do), con autenticación mediante JWT y control de acceso por usuario.

------------------------------------------------------------------------

## 🚀 Características

-   Autenticación con JWT
-   Registro y login de usuarios
-   Hashing seguro de contraseñas
-   Cambio de contraseña validando la contraseña actual
-   CRUD de tareas
-   Multiusuario (cada usuario solo puede ver y gestionar sus propias
    tareas)
-   Arquitectura modular (separación de rutas y servicios)

------------------------------------------------------------------------

## 🛠️ Tecnologías

-   Python
-   Flask
-   SQLite
-   JWT (flask-jwt-extended)

------------------------------------------------------------------------

## 🔐 Autenticación

### Login

POST /api/users/login

Body:

``` json
{
  "username": "usuario",
  "password": "password"
}
```

Respuesta:

``` json
{
  "access_token": "TOKEN"
}
```

### Uso del Token

Para acceder a rutas protegidas, enviar el token en el header:

Authorization: Bearer TOKEN

------------------------------------------------------------------------

## 📋 Endpoints de Tareas

### Obtener tareas

GET /tasks\
🔒 Requiere autenticación

Respuesta:

``` json
[
  {
    "id": 1,
    "title": "Tarea 1",
    "done": false
  }
]
```

------------------------------------------------------------------------

### Crear tarea

POST /tasks\
🔒 Requiere autenticación

Body:

``` json
{
  "title": "Nueva tarea"
}
```

------------------------------------------------------------------------

### Actualizar tarea

PUT /tasks/`<id>`{=html}\
🔒 Requiere autenticación

Body:

``` json
{
  "title": "Nuevo título",
  "done": true
}
```

------------------------------------------------------------------------

### Eliminar tarea

DELETE /tasks/`<id>`{=html}\
🔒 Requiere autenticación

------------------------------------------------------------------------

## 👤 Servicios de Usuario

### Registro de usuario

POST /api/users/register

Body:

``` json
{
  "username": "usuario",
  "password": "password"
}
```

Respuesta:

``` json
{
  "message": "Usuario creado correctamente"
}
```

------------------------------------------------------------------------

### Actualización de contraseña

POST /api/users/update\
🔒 Requiere autenticación

⚠️ Es necesario enviar el token JWT en el header Authorization.

Body:

``` json
{
  "username": "usuario",
  "current_password": "password_actual",
  "new_password": "nuevo_password"
}
```

Respuesta:

``` json
{
  "message": "Contraseña actualizada correctamente"
}
```

------------------------------------------------------------------------

## ⚠️ Manejo de errores

La API utiliza códigos HTTP estándar:

-   400 → Datos inválidos\
-   401 → No autenticado\
-   403 → No autorizado\
-   404 → Recurso no encontrado

Ejemplo:

``` json
{
  "message": "Usuario o password incorrectos"
}
```

------------------------------------------------------------------------

## 📁 Estructura del proyecto

tareasFlask/ │ ├── app/ │ ├── routes/ │ ├── services/ │ └── ... │ ├──
run.py\
├── requirements.txt\
└── README.md

------------------------------------------------------------------------

## 🔒 Seguridad

-   Contraseñas almacenadas con hash seguro\
-   Autenticación basada en JWT\
-   Validación de usuario en cada operación\
-   Protección de rutas sensibles

------------------------------------------------------------------------

## 🚀 Próximas mejoras

-   Migración a MySQL / PostgreSQL\
-   Implementación de ORM (SQLAlchemy)\
-   Pruebas automatizadas\
-   Despliegue en la nube\
-   Sistema de roles (admin / user)

------------------------------------------------------------------------

## 👨‍💻 Autor

George Vilca
