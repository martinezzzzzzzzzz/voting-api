# 📑 Documentación Interactiva (Swagger UI)

La API cuenta con documentación interactiva generada automáticamente gracias a **FastAPI**.

Puedes probar **todos los endpoints** directamente desde el navegador sin necesidad de herramientas externas como Postman o curl.

---

## 🔗 Cómo acceder a Swagger UI

- **URL:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🚪 Ingreso de credenciales

Nuestra API está protegida con **Autenticación Básica (HTTP Basic Auth)**.

Al abrir Swagger UI:

✅ Se mostrará un cuadro emergente solicitando usuario y contraseña.

- **Usuario:** `admin`
- **Password:** `secret`

> ⚠ **Importante:** Debes ingresar estos datos para poder hacer peticiones desde Swagger UI.

---

## ▶ Cómo probar un endpoint en Swagger

1. Ingresa tus credenciales si te las pide el navegador.
2. Busca el endpoint que quieras probar (por ejemplo, **POST /voters/**).
3. Haz clic en el botón **“Try it out”**.
4. Completa el JSON con los datos necesarios.
5. Haz clic en **“Execute”**.
6. Observa la respuesta del servidor en el mismo Swagger UI.

---

## Ejemplo de petición en Swagger

### **POST /voters/**

```json
{
  "name": "Juan Perez",
  "email": "juan@example.com"
}
```

Si los datos son válidos, recibirás una respuesta como:

```json
{
  "id": 1,
  "name": "Juan Perez",
  "email": "juan@example.com",
  "has_voted": false
}
```

# 📊 Consultar estadísticas
Puedes consultar las estadísticas de votos en:

```pgsql
GET /votes/statistics
```
Muestra un resumen como:

```json
{
  "total_votes": 3,
  "total_voters_voted": 2,
  "candidates": [
    {
      "candidate_id": 1,
      "name": "Pedro Lopez",
      "votes_count": 1,
      "percentage": 50.0
    }
  ]
}
```

# ❗ Problemas comunes

- Error 401 Unauthorized: Verifica usuario y contraseña.
- Error 422 Unprocessable Entity: Revisa el JSON enviado en el body.
- Swagger sigue mostrando ventana emergente aunque ingreses bien las credenciales: prueba borrar caché del navegador o usa incógnito.