# 🗳️ Sistema de Votaciones - FastAPI

Proyecto técnico que implementa un sistema de votaciones con Python, FastAPI y MySQL.

## 🚀 Instrucciones para ejecutar el proyecto localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/martinezzzzzzzzzz/voting-api.git
cd voting-api
```

## 2. Crear un entorno virtual
```bash
python -m venv venv
```

- Windows:
venv\Scripts\activate

- Linux/Mac:
source venv/bin/activate

## 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
## 4. Crear la base de datos
En la carpeta database/ encontrarás el archivo schema.sql para crear la base de datos y tablas necesarias.
Ejecuta el script en tu servidor MySQL:

```bash
mysql -u root -p < database/schema.sql
```

## 5. Levantar el servidor

```bash
uvicorn app.main:app --reload
```
Por defecto se ejecuta en:
```cpp
http://127.0.0.1:8000
```
Para ver la documentación interactiva:
```cpp
http://127.0.0.1:8000/docs
```
# 🔐 Autenticación

La API está protegida con autenticación básica.
Credenciales:

- Usuario: admin
- Contraseña: secret

En Swagger UI, al llamar cualquier endpoint protegido aparecerá una ventana emergente para ingresar usuario y contraseña.

# 🎯 Ejemplos de uso

Crear un votante
Con cURL:

```bash
curl -X POST "http://127.0.0.1:8000/voters/" ^
  -H "Content-Type: application/json" ^
  -u admin:secret ^
  -d "{\"name\":\"Juan Perez\",\"email\":\"juan@example.com\"}"
```

Con Postman:

- Method: POST
- URL: http://127.0.0.1:8000/voters/
- Auth: Basic Auth (usuario admin, password secret)
- Body (JSON)

```json
{
  "name": "Juan Perez",
  "email": "juan@example.com"
}
```

### Emitir un voto

Con cURL:

```bash
curl -X POST "http://127.0.0.1:8000/votes/" ^
  -H "Content-Type: application/json" ^
  -u admin:secret ^
  -d "{\"voter_id\":1,\"candidate_id\":2}"
```

Con Postman: 

- Method: POST
- URL: http://127.0.0.1:8000/votes/
- Auth: Basic Auth
- Body (JSON):

```json
{
  "voter_id": 1,
  "candidate_id": 2
}
```

### Consultar estadísticas

Con cURL:

```bash
curl -X GET "http://127.0.0.1:8000/votes/statistics" ^
  -u admin:secret
```

Con Postman: 

- Method: GET
- URL: http://127.0.0.1:8000/votes/statistics
- Auth: Basic Auth

# 📊 Ejemplo de respuesta de estadísticas

Ejemplo de lo que devuelve el endpoint /votes/statistics:

```json
{
  "total_votes": 3,
  "total_voters_voted": 3,
  "candidates": [
    {
      "candidate_id": 1,
      "name": "Pedro Gómez",
      "votes_count": 2,
      "percentage": 66.67
    },
    {
      "candidate_id": 2,
      "name": "Ana López",
      "votes_count": 1,
      "percentage": 33.33
    }
  ]
}
```

# 📷 Capturas

Swagger UI 

![Estidisticas de votos](images\statics.png)
Esta es una vista de las estidisticas egenades despues de 3 votantes. Solo se ve 1 voto reflejado en los candidatos por que los otos 2 fueron de prueba y no contaon los votos a los candidatos.

# 📂 Estructura del proyecto

```pgsql
|voting-api/
├── app/
│   ├── main.py
│   ├── routers/
│   ├── models.py
│   ├── schemas.py
│   ├── auth/
│   └── database.py
├── sql/
│   └── schema.sql
├── docs/
│   ├── swagger_ui.png
│   └── postman_stats.png
├── requirements.txt
└── README.md
```

# 🤝 Autor

- Emanuel Martínez Valencia
- https://github.com/martinezzzzzzzzzz

