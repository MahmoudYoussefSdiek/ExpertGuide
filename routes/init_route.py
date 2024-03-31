"""
"""
from database import db
from routes.book_route import book_routes
from routes.expert_book_reviews_route import expert_book_reviews_route
from routes.expert_roadmap_reviews_route import expert_roadmap_reviews_route


def init_routes(app):
    book_routes(app, db)
    expert_book_reviews_route(app, db)
    expert_roadmap_reviews_route(app, db)