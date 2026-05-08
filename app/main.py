from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.models import user, task
from app.api.routes import auth, protected, tasks
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logger import logger

app = FastAPI(title="SmartTask API")

class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        logger.info(
            f"Request: {request.method} {request.url}"
        )

        response = await call_next(request)

        logger.info(
            f"Response Status: {response.status_code}"
        )

        return response

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="SmartTask API",
        version="1.0.0",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer"
        }
    }

    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


# REGISTER MIDDLEWARE
app.add_middleware(LoggingMiddleware)

app.openapi = custom_openapi


app.include_router(auth.router)
app.include_router(protected.router)
app.include_router(tasks.router)