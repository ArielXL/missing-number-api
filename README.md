# Missing Number API

API construida con **FastAPI** que trabaja con el conjunto de los primeros 100 números naturales \(\[1, 100\]\).  
Permite extraer un número del conjunto y calcular cuál es el número faltante, ofreciendo dos enfoques:

- **Stateless**: el estado del conjunto se calcula a partir del número enviado en cada petición.
- **Stateful**: el estado se mantiene en memoria entre peticiones (útil para demostrar manejo de estado en APIs).

## Tecnologías y dependencias principales

- **Python** 3.10+ (asumido)
- **FastAPI**
- **Uvicorn** (servidor ASGI)
- **pytest** y **fastapi.testclient** para pruebas

Todas las dependencias se encuentran en `requirements.txt`.

## Estructura básica del proyecto

- `app/main.py`: crea la aplicación FastAPI y registra los routers.
- `app/solution_stateless/routes.py`: endpoints que calculan el número faltante sin mantener estado.
- `app/solution_stateful/routes.py`: endpoints que mantienen el estado del conjunto en memoria.
- `app/utils/set100.py`: lógica de negocio para el conjunto \[1, 100\] y el cálculo del número faltante.
- `app/utils/schemas.py`: modelos Pydantic para requests y responses.
- `tests/test_api.py`: pruebas automatizadas sobre el endpoint stateless.

## Puesta en marcha

1. **Crear y activar un entorno virtual** (opcional pero recomendado):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # linux / macOS
   # .venv\Scripts\activate   # windows
   ```

2. **Instalar dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Levantar la API** (asumiendo `app.main:app` como entrypoint):

   ```bash
   uvicorn app.main:app --reload
   ```

4. La documentación interactiva de la API estará disponible en:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints principales

Todos los endpoints están expuestos bajo el prefijo `/api`.

### 1. Enfoque Stateless

- **POST** `/api/missing`

  Calcula el número faltante del conjunto \[1, 100\] a partir del número extraído enviado en el cuerpo.

  **Request body** (`application/json`):

  ```json
  {
    "number": 57
  }
  ```

  - `number`: entero entre 1 y 100.

  **Response 200 OK** (modelo `MissingResponse`):

  ```json
  {
    "extracted": 57,
    "missing": 57,
    "message": "The extracted number was 57 and the calculated missing number is 57."
  }
  ```

  **Códigos de error esperados**:

  - `422 Unprocessable Entity`: validación fallida (por ejemplo, `number` fuera de rango).
  - `400 Bad Request`: error de negocio (valor no válido).
  - `500 Internal Server Error`: error no controlado al calcular el número faltante.

### 2. Enfoque Stateful

Los siguientes endpoints comparten un estado en memoria (`First100NaturalNumbers`) que se actualiza con cada operación:

- **POST** `/api/extract`

  Extrae un número del conjunto y actualiza el estado interno.

  **Request body**:

  ```json
  {
    "number": 42
  }
  ```

  **Response 200 OK**:

  ```json
  {
    "message": "Number 42 extracted successfully."
  }
  ```

- **GET** `/api/missing`

  Obtiene el número faltante en el conjunto actual (después de alguna extracción previa).

  **Response 200 OK**:

  ```json
  {
    "extracted": 42,
    "missing": 42
  }
  ```

  **Posibles errores**:

  - `400 Bad Request`: si aún no se ha extraído ningún número.

- **POST** `/api/reset`

  Restaura el conjunto de números \[1, 100\] a su estado original.

  **Response 200 OK**:

  ```json
  {
    "message": "The set has been reset."
  }
  ```

## Ejecución de pruebas

Las pruebas automatizadas usan `pytest` y el `TestClient` de FastAPI.

Para ejecutarlas:

```bash
pytest
```

Esto validará, entre otras cosas, el comportamiento del endpoint stateless `/api/missing` y la validación de entrada.
