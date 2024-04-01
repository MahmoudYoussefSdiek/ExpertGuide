from flask import jsonify, request, send_file
from model.expertRoadmapReviews import ExpertRoadmapReviews


def expert_roadmap_reviews_route(app, db):

    # Get all roadmaps
    # This route is for the expert to get all roadmaps
    @app.route('/expert/roadmap/reviews', methods=['GET'])
    def get_roadmap_reviews():
        roadmap_reviews = ExpertRoadmapReviews.query.all()
        if not roadmap_reviews:
            return jsonify({'error': 'No roadmap reveiwes found'}), 404
        return jsonify([
            {
                'meta_data': {
                    'total_reviews': len(roadmap_reviews),
                }
            },
            {
                'Roadmap reviews': [roadmap.short_description() for roadmap in roadmap_reviews]
            }
        ]), 200

    # Get a specific roadmap review
    # This route is for the expert to get a specific roadmap review
    @app.route('/expert/roadmap/reviews/<int:review_id>', methods=['GET'])
    def get_roadmap_review(review_id):
        roadmap_review = ExpertRoadmapReviews.query.get(review_id)
        if roadmap_review is None:
            return jsonify({'error': 'review not found'}), 404
        return jsonify(roadmap_review.full_description()), 200

    # Create a new Roadmap review
    # This route is for the expert to create a roadmap review
    @app.route('/expert/roadmap/reviews', methods=['POST'])
    def create_roadmap_review():
        data = request.get_json()
        new_review = ExpertRoadmapReviews(**data)
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.full_description()), 201

    # Update a  Roadmap review
    # This route is for the expert to update a Roadmap review
    @app.route('/expert/roadmap/reviews/<int:review_id>', methods=['PUT'])
    def update_roadmap_review(review_id):
        data = request.get_json()
        review = ExpertRoadmapReviews.query.get(review_id)
        if review is None:
            return jsonify({'error': 'review not found'}), 404
        for key, value in data.items():
            setattr(review, key, value)
        db.session.commit()
        return jsonify(review.full_description()), 200

    # Delete a roadmap review
    # This route is for the expert to delete a roadmap review
    @app.route('/expert/roadmap/reviews/<int:review_id>', methods=['DELETE'])
    def delete_roadmap_review(review_id):
        review = ExpertRoadmapReviews.query.get(review_id)
        if review is None:
            return jsonify({'error': 'Review not found'}), 404
        db.session.delete(review)
        db.session.commit()
        return jsonify({'message': 'review deleted'}), 200
