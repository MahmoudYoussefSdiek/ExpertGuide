from database import db

class Roadmap(db.Model):
    __tablename__ = 'roadmap'

    roadmap_id = db.Column(db.Integer, primary_key=True)
    expert_id = db.Column(db.Integer, db.ForeignKey('expert.expert_id'))
    title = db.Column(db.String(50))
    description = db.Column(db.Text)