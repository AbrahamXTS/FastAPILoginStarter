from auth.auth import Auth
from auth.jwt import JSONWebToken
from models.token import TokenModel
from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm, OAuth2PasswordBearer

authorization = Auth()
loginRoute = APIRouter()
jsonwebtoken = JSONWebToken()

# El parametro tokenUrl es la ruta relativa de la que se obtendrá el token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")

@loginRoute.post("/login", response_model = TokenModel, tags = ["Auth"])
async def handle_login(user: OAuth2PasswordRequestForm = Depends()):
    
    # Aquí va la comprobación de credenciales con la BD

    access_token = jsonwebtoken.create_access_token(user.username)

    return {"access_token": access_token, "token_type": "Bearer"}
