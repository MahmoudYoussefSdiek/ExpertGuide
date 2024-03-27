from database import db
from flask import jsonify


class Book(db.Model):
    __tablename__ = 'book'

    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    shortDescription = db.Column(db.Text)
    fullDescription = db.Column(db.Text)
    category = db.Column(db.String(20))
    BookLocation = db.Column(db.String(255))
    CreatedBy = db.Column(db.Integer, db.ForeignKey(
        'admin.admin_id'), nullable=True)
    CreatedDT = db.Column(db.DateTime, nullable=True)
    UpdatedBy = db.Column(db.Integer, db.ForeignKey(
        'admin.admin_id'), nullable=True)
    UpdatedDT = db.Column(db.DateTime, nullable=True)
    DeletedBy = db.Column(db.Integer, db.ForeignKey(
        'admin.admin_id'), nullable=True)
    DeletedDT = db.Column(db.DateTime, nullable=True)
    Enabled = db.Column(db.Boolean)

    def to_dict(self):
        book_location = self.BookLocation.replace(' ', '^')
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'shortDescription': self.shortDescription,
            'fullDescription': self.fullDescription,
            'category': self.category,
            'BookLocation': book_location,
            'CreatedBy': self.CreatedBy,
            'CreatedDT': self.CreatedDT.isoformat() if self.CreatedDT else None,
            'UpdatedBy': self.UpdatedBy,
            'UpdatedDT': self.UpdatedDT.isoformat() if self.UpdatedDT else None,
            'DeletedBy': self.DeletedBy,
            'DeletedDT': self.DeletedDT.isoformat() if self.DeletedDT else None,
            'Enabled': self.Enabled
        }

    def short_description(self):
        if not self.Enabled:
            return None
        return {
            'book_id': self.book_id,
            'title': self.title,
            'short_description': self.shortDescription,
            'category': self.category
        }

    def full_description(self):
        if not self.Enabled:
            return None
        return {
            'book_id': self.book_id,
            'title': self.title,
            'short_description': self.shortDescription,
            'long_description': self.fullDescription,
            'category': self.category,
            'Enabled': self.Enabled,
            'CreatedAt': self.CreatedDT,
            'UpdatedAt': self.UpdatedDT,
        }
