from fastapi import FastAPI
from .config import settings
from .router import api_router
from . import __version__

app = FastAPI(title=settings.APP_NAME,
              version=__version__,
              root_path=settings.ROOT_PATH
              )

app.include_router(api_router, prefix=settings.ROOT_PATH)
