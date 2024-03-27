from database import db

class LearnerRoadmapReviews(db.Model):
    __tablename__ = 'learner_roadmap_reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    learner_id = db.Column(db.Integer, db.ForeignKey('learner.learner_id'))
    roadmap_id = db.Column(db.Integer, db.ForeignKey('roadmap.roadmap_id'))
    rating = db.Column(db.Integer)
    roadmap_review = db.Column(db.Text)