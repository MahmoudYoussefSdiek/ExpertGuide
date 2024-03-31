from database import db

class ExpertRoadmapReviews(db.Model):
    __tablename__ = 'expert_roadmap_reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    roadmap_id = db.Column(db.Integer, db.ForeignKey('roadmap.roadmap_id'))
    expert_id = db.Column(db.Integer, db.ForeignKey('expert.expert_id'))
    rating = db.Column(db.Integer)
    roadmap_review = db.Column(db.Text)
    
    def short_description(self):

        return {
            'review_id': self.review_id,
            'roadmap_id': self.roadmap_id,
            'rating': self.rating
        }
        
def full_description(self):

        return {
            'review_id': self.review_id,
            'expert_id': self.expert_id,
            'roadmap_id': self.roadmap_id,
            'rating': self.rating,
            'roadmap_review': self.roadmap_review
        }
        