from fastapi import APIRouter
from rest_api.schemas.status import Status

router = APIRouter(
    prefix="",
    tags=["status"],
)


@router.get("/", response_model=Status)
def health_check():
    """
    Health Check API

    """

    return Status(status="OK")
