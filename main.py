
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="MLOPs first API",
    description="MLOPs API",
    version="0.0.1"
)

# Cliente envia info de Usuario por medio de JSON.
@app.post("/users", tags=["Users"])
async def create_user(data: dict):
    user = data["user"]
    name = data["name"]
    email = data["email"]

    return {
        "message": f"User {name} Created Successfully. ID {str(uuid.uuid4())}",
    }

# Cliente envia info de Producto.
@app.post("/products", tags=["Products"])
async def create_product(product_name:str, product_price: float):

    try:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": f"Product {product_name} with price {product_price}",
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e))

# Cliente pide información de Usuarios.
@app.get("/get'users/{user_id}", tags=["Users"])
async def get_users(user_id:str):

    # Base de datos simulada. Aquí usaríamos sql alchemy.
    user_db = {
        "70": {
            "name": "Jason",
            "email": "jason@email.com",
        },
        "90": {
            "name": "Jorge",
            "email": "jorge@email.com",
        }
    }

    try:
        user = user_db[user_id]
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": f"User {user} was found",
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e))