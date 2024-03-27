from flask import jsonify, request, send_file
from model.book import Book


def book_routes(app, db):

    # Get all books
    @app.route('/books', methods=['GET'])
    def get_books():
        books = Book.query.all()
        return jsonify({
            'meta_data': {
                'total_books': len(books),
            },
            'books': [
                book.short_description()
                for book in books
                if book.short_description() is not None
            ]
        }), 200

    # Get a specific book
    @app.route('/books/<int:book_id>', methods=['GET'])
    def get_book(book_id):
        book = Book.query.get(book_id)
        if book is None:
            return jsonify({'error': 'Book not found'}), 404
        return book.full_description(), 200

    # Create a new book
    @app.route('/books', methods=['POST'])
    def create_book():
        data = request.get_json()
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book), 201

    # Update a book
    @app.route('/books/<int:book_id>', methods=['PUT'])
    def update_book(book_id):
        data = request.get_json()
        book = Book.query.get(book_id)
        if book is None:
            return jsonify({'error': 'Book not found'}), 404
        book.update(**data)
        db.session.commit()
        return jsonify(book.to_dict()), 200

    # Delete a book
    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        book = Book.query.get(book_id)
        if book is None:
            return jsonify({'error': 'Book not found'}), 404
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted'}), 200

    # Download a book
    @app.route('/books/<int:book_id>/download', methods=['GET'])
    def download_book(book_id):
        book = Book.query.get(book_id)
        if book is None:
            return jsonify({'error': 'Book not found'}), 404
        return send_file(book.bookLocation, as_attachment=True)
