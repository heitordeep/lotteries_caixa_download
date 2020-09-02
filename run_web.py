from decouple import config
from flask import Flask

from web.main import app

web = Flask('app')
web.register_blueprint(app)

if __name__ == "__main__":
    web.run(debug=config('DEBUG'))
