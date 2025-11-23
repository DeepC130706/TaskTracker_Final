from flask import Flask
from src.routes import register_routes
from src.models import init_db
app = Flask(__name__)
app.secret_key = "dev_secret_key"
# init DB
init_db()
register_routes(app)
if __name__ == "__main__":
    app.run(debug=True)
