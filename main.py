from decouple import config

from settings.server import create_app

app = create_app()
