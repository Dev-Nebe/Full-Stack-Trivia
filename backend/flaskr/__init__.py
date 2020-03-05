import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import load_only
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, PATCH, POST, DELETE, OPTIONS')
        return response

    """
    @TODO: 
    Create an endpoint to handle GET requests 
    for all available categories.
    """

    @app.route('/')
    def homepage():
        return jsonify({"message": "Hello"})

    @app.route('/v1/categories')
    def get_available_categories():
        response_object = {
            "success": False
        }

        try:
            fields = ['type']

            categories = db.session.query(Category.type).all()

            list_of_categories = []

            for category in categories:
                list_of_categories.append(category[0])

            response_object['categories'] = list_of_categories

            response_object['success'] = True

            # Format this data in the right form

        except:
            print(sys.exc_info())
            db.session.rollback()

            # response_object['error_message'] = 'Something went wrong and we were unable to process your request.'
            abort(500)

        finally:
            db.session.close()
            return jsonify(response_object)

    """
    @TODO: 
    Create an endpoint to handle GET requests for questions, 
    including pagination (every 10 questions). 
    This endpoint should return a list of questions, 
    number of total questions, current category, categories. 

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions. 
    """

    @app.route('/v1/questions')
    def get_questions():
        pass

    """
    @TODO: 
    Create an endpoint to DELETE question using a question ID. 

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page. 
    """

    @app.route('/v1/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        pass

    """
    @TODO: 
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab. 
    """
    @app.route('/v1/questions', methods=['POST'])
    def post_new_question():
        pass

    """
    @TODO: 
    Create a POST endpoint to get questions based on a search term. 
    It should return any questions for whom the search term 
    is a substring of the question. 
    

    TEST: Search by any phrase. The questions list will update to include 
    only question that include that string within their question. 
    Try using the word "title" to start. 
    """
    @app.route('/v1/search-questions', methods=['POST'])
    def search_questions():
        pass

    """
    @TODO: 
    Create a GET endpoint to get questions based on category. 

    TEST: In the "List" tab / main screen, clicking on one of the 
    categories in the left column will cause only questions of that 
    category to be shown. 
    """
    @app.route('/v1/categories/<int:category_id>')
    def get_questions_by_category(category_id):
        pass

    """
    @TODO: 
    Create a POST endpoint to get questions to play the quiz. 
    This endpoint should take category and previous question parameters 
    and return a random questions within the given category, 
    if provided, and that is not one of the previous questions. 

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not. 
    """

    """
    @TODO: 
    Create error handlers for all expected errors 
    including 404 and 422. 
    """
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "error": 400,
            "message": "Bad request.",
            "success": False
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": 404,
            "message": "The requested resource does not exist.",
            "success": False
        }), 404

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            "error": 422,
            "message": "The request is unprocessable.",
            "success": False
        }), 422

    @app.errorhandler(500)
    def internal_serval_error(error):
        return jsonify({
            "error": 500,
            "message": "Something went wrong the server.",
            "success": False
        })
        pass

    return app
