from database import db

class Book(db.Model):
    __tablename__ = 'book'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    short_description = db.Column(db.Text)
    full_description = db.Column(db.Text)
    category = db.Column(db.String(20))
    BookLocation = db.Column(db.String(255))
    CreatedBy = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
    CreatedDT = db.Column(db.DateTime)
    UpdatedBy = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
    UpdatedDT = db.Column(db.DateTime)
    DeletedBy = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
    DeletedDT = db.Column(db.DateTime)
    Enabled = db.Column(db.Boolean)