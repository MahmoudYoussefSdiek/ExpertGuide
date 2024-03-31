from database import db


class ExpertBookReviews(db.Model):
    __tablename__ = 'expert_book_reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    expert_id = db.Column(db.Integer, db.ForeignKey('expert.expert_id'))
    rating = db.Column(db.Integer)
    book_review = db.Column(db.Text)
    book_summary = db.Column(db.Text)


def short_description(self):

        return {
            'review_id': self.review_id,
            'expert_id': self.expert_id,
            'book_id': self.book_id,
            'rating': self.rating
        }
        
def full_description(self):

        return {
            'review_id': self.review_id,
            'expert_id': self.expert_id,
            'book_id': self.book_id,
            'rating': self.rating,
            'book_review': self.book_review,
            'book_summary': self.book_summary
        }