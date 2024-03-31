from flask import jsonify, request, send_file
from model.expertBookReviews import ExpertBookReviews


def expert_book_reviews_route(app, db):

    # Get all books
    # This route is for the expert to get all books
    @app.route('/expert/book/reviews', methods=['GET'])
    def get_book_reviews():
        book_reviews = ExpertBookReviews.query.all()
        if not book_reviews:
            return jsonify({'error': 'No books reveiwes found'}), 404
        return jsonify([
            {
                'meta_data': {
                    'total_reviews': len(book_reviews),
                }
            },
            {
                'books reviews': [book_reviews.short_description() for book_reviews in book_reviews]
            }
        ]), 200

    # Get a specific book review
    # This route is for the expert to get a specific book review
    @app.route('/expert/book/reviews/<int:review_id>', methods=['GET'])
    def get_book_review(review_id):
        book_review = ExpertBookReviews.query.get(review_id)
        if book_review is None:
            return jsonify({'error': 'review not found'}), 404
        return jsonify(book_review.full_description()), 200

    # Create a new review
    # This route is for the expert to create a review
    @app.route('/expert/book/reviews', methods=['POST'])
    def create_review():
        data = request.get_json()
        new_review = ExpertBookReviews(**data)
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.full_description()), 201

    # Update a book review
    # This route is for the expert to update a review
    @app.route('/expert/book/reviews/<int:review_id>', methods=['PUT'])
    def update_review(review_id):
        data = request.get_json()
        review = ExpertBookReviews.query.get(review_id)
        if review is None:
            return jsonify({'error': 'review not found'}), 404
        for key, value in data.items():
            setattr(review, key, value)
        db.session.commit()
        return jsonify(review.full_description()), 200

    # Delete a book review
    # This route is for the expert to delete a review
    @app.route('/expert/book/reviews/<int:review_id>', methods=['DELETE'])
    def delete_review(review_id):
        review = ExpertBookReviews.query.get(review_id)
        if review is None:
            return jsonify({'error': 'Review not found'}), 404
        db.session.delete(review)
        db.session.commit()
        return jsonify({'message': 'review deleted'}), 200