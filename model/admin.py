from database import db

class Admin(db.Model):
    __tablename__ = 'admin'

    admin_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    admin_role = db.Column(db.String(10))
    department = db.Column(db.String(10))
    responsibilities = db.Column(db.Text)