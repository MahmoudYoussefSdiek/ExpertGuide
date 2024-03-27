"""
This is the main file to run the application.
"""
from flask import Flask
from routes.init_route import init_routes
from database import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:post@localhost:5432/ExpertGuide'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    init_routes(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
