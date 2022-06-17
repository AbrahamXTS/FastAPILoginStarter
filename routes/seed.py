from fastapi import APIRouter, Depends
from routes.login import oauth2_scheme
from auth.jwt import JSONWebToken

seedRoute = APIRouter()
jsonwebtoken = JSONWebToken()

@seedRoute.get("/", response_model = dict, tags = ["Seed"])
def say_hello():
    return {"Hola": "Bienvenido a mi API"}

@seedRoute.get("/token", response_model = str, tags = ["Seed"])
def verify_token(token: str = Depends(oauth2_scheme)):
    # Todas las rutas deben validar el JWT.
    return jsonwebtoken.validate_access_token(token)