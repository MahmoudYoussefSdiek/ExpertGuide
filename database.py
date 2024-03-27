"""
This file contains all the database tables for the application,
and instances of the database object.
It is like interface between the application and the database.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from model.user import User
from model.admin import Admin
from model.book import Book
from model.learner import Learner
from model.expert import Expert
from model.roadmap import Roadmap
from model.learnerBookReviews import LearnerBookReviews
from model.learnerRoadmapReviews import LearnerRoadmapReviews
from model.expertBookReviews import ExpertBookReviews
from model.expertRoadmapReviews import ExpertRoadmapReviews