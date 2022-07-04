import os
from rest_api.types import StrEnum

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Spec Folder Path
API_SPEC_DIR = os.path.join(ROOT_DIR, "spec")
