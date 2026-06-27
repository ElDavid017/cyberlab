# CyberLab — Rastreador de Incidentes Cibernéticos

Aplicación web desarrollada con Django y PostgreSQL para gestionar incidentes de seguridad. Incluye autenticación completa, control de acceso por roles y medidas de endurecimiento de seguridad.

## Tecnologías

- Python 3 / Django
- PostgreSQL
- django-axes (protección contra fuerza bruta)

## Funcionalidades

- Registro e inicio de sesión de usuarios
- Roles: Administrador y Analista
- Los analistas pueden crear y ver incidentes
- Solo los administradores pueden editar y eliminar
- Registro de quién reportó cada incidente
- Cabeceras de seguridad configuradas
- Protección contra ataques de fuerza bruta

## Rutas principales

| URL | Método | Descripción |
|-----|--------|-------------|
| /accounts/login/ | GET, POST | Iniciar sesión |
| /accounts/register/ | GET, POST | Registro de usuario |
| /accounts/logout/ | POST | Cerrar sesión |
| /accounts/dashboard/ | GET | Panel del usuario |
| /incidents/ | GET | Lista de incidentes |
| /incidents/new/ | GET, POST | Crear incidente |
| /incidents/\<pk\>/ | GET | Ver detalle |
| /incidents/\<pk\>/edit/ | GET, POST | Editar (solo admin) |
| /incidents/\<pk\>/delete/ | GET, POST | Eliminar (solo admin) |

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/ElDavid017/cyberlab.git
cd cyberlab

# Instalar dependencias
pip install django psycopg2-binary django-axes

# Configurar base de datos en cyberlab/settings.py

# Aplicar migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

## Materia

Ethical Hacking — Octavo Semestre  
ULEAM, Extensión El Carmen
