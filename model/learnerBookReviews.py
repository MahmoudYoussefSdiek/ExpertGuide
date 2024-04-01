from database import db

class LearnerBookReviews(db.Model):
    __tablename__ = 'learner_book_reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    learner_id = db.Column(db.Integer, db.ForeignKey('learner.learner_id'))
    rating = db.Column(db.Integer)
    book_review = db.Column(db.Text)

    def short_description(self):

        return {
            'review_id': self.review_id,
            'book_id': self.book_id,
            'rating': self.rating
        }

    def full_description(self):

        return {
            'review_id': self.review_id,
            'learner_id': self.learner_id,
            'book_id': self.book_id,
            'rating': self.rating,
            'book_review': self.book_review,
        }