from database import db
from flask import jsonify

class Book(db.Model):
    __tablename__ = 'book'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    shortDescription = db.Column(db.Text)
    fullDescription = db.Column(db.Text)
    category = db.Column(db.String(20))
    BookLocation = db.Column(db.String(255))
    CreatedBy = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
    CreatedDT = db.Column(db.DateTime)
    UpdatedBy = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
    UpdatedDT = db.Column(db.DateTime)
    DeletedBy = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
    DeletedDT = db.Column(db.DateTime)
    Enabled = db.Column(db.Boolean)
    
    def short_description(self):
        if not self.Enabled:
            return None
        return jsonify({
            'book_id': self.book_id,
            'title': self.title,
            'short_description': self.shortDescription,
            'category': self.category
        })

    def full_description(self):
        if not self.Enabled:
            return None
        return jsonify({
            'book_id': self.book_id,
            'title': self.title,
            'short_description': self.shortDescription,
            'long_description': self.fullDescription,
            'category': self.category,
            'Enabled': self.Enabled,
            'CreatedAt': self.CreatedDT,
            'UpdatedAt': self.UpdatedDT,
        })