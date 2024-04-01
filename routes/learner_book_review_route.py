from flask import jsonify, request, send_file
from model.learnerBookReviews import LearnerBookReviews


def learner_book_reviews_route(app, db):

    # Get all learner books reviews
    # This route to get all learner reviews books
    @app.route('/learner/book/reviews', methods=['GET'])
    def get_learner_book_reviews():
        all_book_reviews = LearnerBookReviews.query.all()
        if not all_book_reviews:
            return jsonify({'error': 'No books reveiwes found'}), 404
        return jsonify([
            {
                'meta_data': {
                    'total_reviews': len(all_book_reviews),
                }
            },
            {
                'books reviews': [book_review.short_description() for book_review in all_book_reviews]
            }
        ]), 200

    # Get a specific learner book review
    # This route is for the a specific book review
    @app.route('/learner/book/reviews/<int:review_id>', methods=['GET'])
    def get_learner_book_review(review_id):
        book_review = LearnerBookReviews.query.get(review_id)
        if book_review is None:
            return jsonify({'error': 'review not found'}), 404
        return jsonify(book_review.full_description()), 200

    # Create a new review
    # This route is for the learner to create a review
    @app.route('/learner/book/reviews', methods=['POST'])
    def create_learner_book_review():
        data = request.get_json()
        new_review = LearnerBookReviews(**data)
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.full_description()), 201

    # Update a book review
    # This route is for the learner to update a review
    @app.route('/learner/book/reviews/<int:review_id>', methods=['PUT'])
    def update_learner_book_review(review_id):
        data = request.get_json()
        review = LearnerBookReviews.query.get(review_id)
        if review is None:
            return jsonify({'error': 'review not found'}), 404
        for key, value in data.items():
            setattr(review, key, value)
        db.session.commit()
        return jsonify(review.full_description()), 200

    # Delete a book review
    # This route is for the learner to delete a review
    @app.route('/learner/book/reviews/<int:review_id>', methods=['DELETE'])
    def delete_learner_book_review(review_id):
        review = LearnerBookReviews.query.get(review_id)
        if review is None:
            return jsonify({'error': 'Review not found'}), 404
        db.session.delete(review)
        db.session.commit()
        return jsonify({'message': 'review deleted'}), 200