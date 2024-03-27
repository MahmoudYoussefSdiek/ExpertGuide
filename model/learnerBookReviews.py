from database import db

class LearnerBookReviews(db.Model):
    __tablename__ = 'learner_book_reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    learner_id = db.Column(db.Integer, db.ForeignKey('learner.learner_id'))
    rating = db.Column(db.Integer)
    book_review = db.Column(db.Text)