import structlog
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rest_api.api import routers
from rest_api.config import EnvironmentEnum, config
from rest_api.types import StrDict

logger = structlog.get_logger(__name__)


def configure_cors(app: FastAPI):
    cors_origin = config.CORS_ORIGIN

    if config.ENV == EnvironmentEnum.PRODUCTION and cors_origin == "*":
        logger.warn("Pls change `CORE_ORIGIN` for production setting")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origin,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def configure_routers(app: FastAPI):
    for router in routers:
        app.include_router(router)


def create_app() -> FastAPI:
    kwargs: StrDict = {}

    if not config.DOCS_UI_ALLOW:
        kwargs["docs_url"] = None
        kwargs["redoc_url"] = None

    app = FastAPI(**kwargs)

    configure_cors(app)
    configure_routers(app)

    return app