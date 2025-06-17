import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from server import db
db.init_app(app)
migrate = Migrate(app, db)

# Register routes
from server.routes import register_routes
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)