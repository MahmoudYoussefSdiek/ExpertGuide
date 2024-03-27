"""
"""
from database import db
from routes.book_route import book_routes


def init_routes(app):
    book_routes(app, db)