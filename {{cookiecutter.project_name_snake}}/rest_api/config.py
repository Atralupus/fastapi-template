import typing

import pydantic
from pydantic import BaseSettings, Field


Environment = typing.Literal["local", "test", "development", "production"]


class Settings(BaseSettings):
    #: Environment
    ENV: Environment = "local"

    #: Server Domain
    SERVER_NAME: typing.Optional[str] = "localhost"
    #: Service Name
    SERVICE_NAME: str

    # redoc, swagger ui Access
    DOCS_UI_ALLOW: bool = Field(False)

    @pydantic.validator("DOCS_UI_ALLOW", pre=True, always=True)
    def default_docs_ui_allow(cls, v, *, values):
        if v:
            return v
        elif values["ENV"] in {"local", "test"}:
            return True
        else:
            return False

    #: CORS
    CORS_ORIGIN: str = Field("*")

    class Config:
        env_prefix = "RESTAPI_"

        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()
