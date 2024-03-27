from database import db

class Expert(db.Model):
    __tablename__ = 'expert'

    expert_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    expertise_area = db.Column(db.String(10))
    qualifications = db.Column(db.Text)