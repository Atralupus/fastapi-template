from .api_v1 import routers as v1_routers
from .status import router as status_router

routers = [
    status_router,
    *v1_routers
]

__all__ = [
    "routers",
]
