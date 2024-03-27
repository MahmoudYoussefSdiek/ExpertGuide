from database import db

class Learner(db.Model):
    __tablename__ = 'learner'

    learner_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    learning_goals = db.Column(db.Text)
    current_skills = db.Column(db.Text)
    level_of_expertise = db.Column(db.Integer)