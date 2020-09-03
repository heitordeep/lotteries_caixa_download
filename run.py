from decouple import config
from settings.server import create_app

app = create_app()

if __name__ == "__main__":
    # Run web Page and API
    app.run(debug=config('DEBUG'))
