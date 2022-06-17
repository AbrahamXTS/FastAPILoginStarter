from fastapi import FastAPI
from docs import tags_metadata
from routes.seed import seedRoute
from routes.login import loginRoute
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    version = 1.0,
    title = "Starter Login",
    openapi_tags = tags_metadata,
    description = "Demostración del uso de OAUTH2 Y JWT para un inicio de sesión en FastAPI.",
)

app.include_router(seedRoute)
app.include_router(loginRoute)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_credentials = True,
)