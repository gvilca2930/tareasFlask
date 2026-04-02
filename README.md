# API de tareas con Flask

API REST desarrollada en Python con Flask para la gestion de tareas (To-Do) con autenticacion mediante JWT y control de acceso por usuario.

---

## Caracteristicas

- Autenticacion con JWT
- Registro y login de usuarios
- Hashing de passwords
- Cambio de passwords validando la anterior
- CRUD de tareas
- Multiusuario (Cada usuario solo ve sus tareas)
- Arquitectura modular (Rutas y servicios separados)

---

## Tecnologias

- Python
- Flask
- SQLite
- JWT

---

## Autenticacion

### Login
POST /api/users/login

Body:

{
    "username" : "usuario",
    "password" : "password"
}

Respuesta:

{
    "access_token" : "TOKEN"
}

### Uso del Token

Authorization : Bearer TOKEN

## EndPoints

### Obtener Tareas
GET /tasks -> Requiere autenticacion

Respuesta:

[
    {
        "id" : 1,
        "title" : "Tarea 1",
        "done" : False
    }
]

### Crear Tareas
POST /tasks -> Requiere autenticacion

Body:
{
    "title" : "Nueva Tarea"
}

### Actualizar Tarea
PUT /tasks/<id> -> Requiere autenticacion

Body:
{
    "title" : "Actualizacion nombre de la tarea",
    "done" : True
}

### Eliminar Tarea
DELETE /tasks/<id> -> Requiere autenticacion

## Servicios Users

### Registro de Usuarios
POST /api/users/register

Body:
{
    "username" : "usuario",
    "password" : "password"
}

### Actualizacion de Password
    -Agregar autorizacion en la ruta-
POST /api/users/update

Body:
{
    "username" : "usuario",
    "current_password" : "password_actual",
    "new_password" : "nuevo_password"
}

