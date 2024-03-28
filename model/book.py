from database import db


class Book(db.Model):
    __tablename__ = 'book'

    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    shortDescription = db.Column(db.Text)
    fullDescription = db.Column(db.Text)
    category = db.Column(db.String(20))
    bookLocation = db.Column(db.String(255))
    createdBy = db.Column(db.Integer, db.ForeignKey(
        'admin.admin_id'), nullable=True)
    createdDate = db.Column(db.DateTime, nullable=True)
    updatedBy = db.Column(db.Integer, db.ForeignKey(
        'admin.admin_id'), nullable=True)
    updatedDate = db.Column(db.DateTime, nullable=True)
    deletedBy = db.Column(db.Integer, db.ForeignKey(
        'admin.admin_id'), nullable=True)
    deletedDate = db.Column(db.DateTime, nullable=True)
    enabled = db.Column(db.Boolean)

    def to_dict(self):
        book_location = self.bookLocation.replace(' ', '^')
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'shortDescription': self.shortDescription,
            'fullDescription': self.fullDescription,
            'category': self.category,
            'bookLocation': book_location,
            'createdBy': self.createdBy,
            'createdDate': self.createdDate.isoformat() if self.createdDate else None,
            'updatedBy': self.updatedBy,
            'updatedDate': self.updatedDate.isoformat() if self.updatedDate else None,
            'deletedBy': self.deletedBy,
            'deletedDate': self.deletedDate.isoformat() if self.deletedDate else None,
            'enabled': self.enabled
        }

    def short_description(self):
        if not self.enabled:
            return None
        return {
            'book_id': self.book_id,
            'title': self.title,
            'short_description': self.shortDescription,
            'category': self.category
        }

    def full_description(self):
        if not self.enabled:
            return None
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'short_description': self.shortDescription,
            'long_description': self.fullDescription,
            'category': self.category,
            'CreatedAt': self.createdDate,
            'UpdatedAt': self.updatedDate,
        }
