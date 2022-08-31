import json
import os

import click
import structlog
import uvicorn
from fastapi.openapi.utils import get_openapi

from rest_api.app import create_app
from rest_api.constants import API_SPEC_DIR

app = create_app()

__all__ = [
    "app",
]

logger = structlog.get_logger(__name__)


@click.group(chain=True)
def cli():
    pass


@cli.command()
@click.option("-h", "--host", "host", default="localhost")
@click.option("-p", "--port", "port", default=8002, type=click.INT)
def execute(host: str, port: int):
    uvicorn.run(app, host=host, port=port)


@cli.command()
def gen_spec():
    logger.info("Start generate spec")

    openapi = get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
        tags=app.openapi_tags,
        servers=app.servers,
    )

    path = os.path.join(API_SPEC_DIR, "rest-api.json")
    if not os.path.exists(API_SPEC_DIR):
        os.makedirs(API_SPEC_DIR)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(openapi, f, ensure_ascii=False, indent=2)

    logger.info("Finish create spec!", path=path)


if __name__ == "__main__":
    cli()
