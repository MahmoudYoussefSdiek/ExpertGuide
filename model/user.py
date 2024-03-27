from database import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    role = db.Column(db.String(10))
    bio = db.Column(db.Text)
    CreatedDT = db.Column(db.DateTime)
    UpdatedDT = db.Column(db.DateTime)
    DeletedDT = db.Column(db.DateTime)
    Activated = db.Column(db.Boolean)
    ActivatedDT = db.Column(db.DateTime)
