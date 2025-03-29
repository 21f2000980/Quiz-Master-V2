from flask import Flask, request, jsonify
from flask_restful import Api , Resource
from models import User, Subject, Chapter, Quiz, Question,Score, db
from datetime import datetime,timedelta
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity,create_refresh_token
from werkzeug.security import generate_password_hash,check_password_hash



from flask import Blueprint

# Create a blueprint for the API
api_bp = Blueprint('api', __name__)
api = Api(api_bp)


class UserLoginAPI(Resource):
    def post(self):
        """Authenticate user and return access & refresh tokens."""
        data = request.get_json()
        print("Received Data:", data)  # ✅ Debugging

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return {'message': 'Missing email or password'}, 400

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            return {'message': 'Invalid email or password'}, 401

        # Generate JWT tokens
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
        refresh_token = create_refresh_token(identity=user.id)

        return {
            'message': 'Login successful',
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': {
                'id': user.id,
                'email': user.email,
                'full_name': user.full_name,
                'role': user.role
            }
        }, 200

class TokenRefreshAPI(Resource):
    @jwt_required(refresh=True)
    def post(self):
        """Generate a new access token using the refresh token."""
        current_user_id = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user_id, expires_delta=timedelta(hours=1))
        return {'access_token': new_access_token}, 200
# --------------------------
# 📝 User Registration API
# --------------------------
class UserRegistrationAPI(Resource):
    def post(self):
        """Register a new user."""
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        full_name = data.get('name')
        dob_str = data.get('dob')
        qualification = data.get('qualification')

        if not email or not password or not full_name or not dob_str:
            return {'message': 'Missing required fields'}, 400

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {'message': 'Email already exists'}, 400

        # Convert DOB to date format
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        except ValueError:
            return {'message': 'Invalid date format. Use YYYY-MM-DD'}, 400

        # Hash the password
        # hashed_password = generate_password_hash(password)

        # Create a new user
        new_user = User(
            email=email,
            full_name=full_name,
            dob=dob,
            qualification=qualification,
            role='user',  # Default role
    
        )
        new_user.set_password(password)
        # Save to database
        db.session.add(new_user)
        db.session.commit()

        # Generate JWT tokens
        access_token = create_access_token(identity=new_user.id)
        refresh_token = create_refresh_token(identity=new_user.id)

        return {
            'message': 'User registered successfully',
            'user': {
                'id': new_user.id,
                'email': new_user.email,
                'full_name': new_user.full_name,
                'role': new_user.role
            },
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 201



# --------------------------
# 🧑‍💻 User API
# --------------------------
class UserAPI(Resource):
    def post(self, user_id=None):
        #  Authenticate user and return access
        """Fetch all users or a specific user."""
        if user_id:
            user = User.query.get(user_id)
            if user:
                return jsonify({
                    'id': user.id,
                    'email': user.email,
                    'full_name': user.full_name,
                    'role': user.role
                })
            return {'message': 'User not found'}, 404
        users = User.query.all()
        return jsonify([{
            'id': user.id,
            'email': user.email,
            'full_name': user.full_name,
            'role': user.role
        } for user in users])

    def post(self):
        """Create a new user."""
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        full_name = data.get('full_name')
        dob_str = data.get('dob')
        qualification = data.get('qualification')

        if not email or not password or not full_name:
            return {'message': 'Missing required fields'}, 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {'message': 'Email already exists'}, 400

        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        new_user = User(
            email=email,
            full_name=full_name,
            dob=dob,
            qualification=qualification,
            role='user'
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User created successfully', 'id': new_user.id}, 201

    def put(self, user_id):
        """Update a user."""
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        data = request.get_json()
        user.email = data.get('email', user.email)
        user.full_name = data.get('full_name', user.full_name)
        user.role = data.get('role', user.role)
        db.session.commit()

        return {'message': 'User updated successfully'}

    def delete(self, user_id):
        """Delete a user."""
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}



class QuizView(Resource):
    def get(self,chapter_id):
        print(f"Received chapter_id: {chapter_id}")  # Debugging
        quizs = Quiz.query.filter_by(chapter_id=chapter_id).all()
        print(quizs)
        if quizs:
             return [{
            'id': quiz.id,
            'date_of_quiz': quiz.date_of_quiz.strftime('%Y-%m-%d'),
            'time_duration':quiz.time_duration,
            'remark': quiz.remarks,   
             } for quiz in quizs  ]
        else :
            return {"message": "No quizzes found for this chapter"}, 404


class QuestionView(Resource):
    def get(self, quiz_id):
        """Fetch all questions or a specific question."""
        if quiz_id:
            questions = Question.query.filter_by(quiz_id = quiz_id).all()
            if questions:
                return jsonify([{
                    'id': question.id,
                    'question_statement': question.question_statement,
                    'option_1': question.option_1,
                    'option_2': question.option_2,
                    'option_3': question.option_3,
                    'option_4': question.option_4,
                    'correct_option': question.correct_option,
                } for question in questions])
            else :
                return {'message': 'Question not found'}, 404
class submitscore(Resource):
    def post(self):
        data = request.get_json()
        new_score = Score(
            user_id=data['user_id'],
            quiz_id=data['quiz_id'],
            total_scored=data['total_scored']
        )
        db.session.add(new_score)
        db.session.commit()
        return {"message": "Score submitted successfully!"}, 201
    
    
class UserScores(Resource):
    def get(self, user_id):
        """Fetch all scores for a specific user with chapter and subject details"""
        
        # Fetch scores with related quiz, chapter, and subject details
        scores = Score.query.filter_by(user_id = user_id).all()

        if scores:
            return [{
                "quiz_id": score.quiz_id,
                "date": score.time_stamp_of_attempt.strftime("%Y-%m-%d"),
                "total_scored": score.total_scored
            } for score in scores], 200
        
        else:
            return {'message': 'No scores found'}, 404
# --------------------------
# 📚 Subject API
# --------------------------
class SubjectAPI(Resource):
    # @jwt_required()
    def get(self, subject_id=None):
        """Fetch all subjects or a specific subject with its chapters."""
        if subject_id:
            subject = Subject.query.get_or_404(subject_id, description="Subject not found")
            return {
                'id': subject.id,
                'name': subject.name,
                'description': subject.description,
                'chapters': [{
                    'id': chapter.id,
                    'name': chapter.name,
                    'description': chapter.description
                } for chapter in subject.chapters]  # Assuming a relationship exists
            }

        subjects = Subject.query.all()
        return [{
            'id': subject.id,
            'name': subject.name,
            'description': subject.description
        } for subject in subjects], 200

    # @jwt_required()
    def post(self):
        """Create a new subject."""
        data = request.get_json()
        if not data or 'name' not in data:
            return {'message': 'Name is required'}, 400

        try:
            new_subject = Subject(
                name=data['name'],
                description=data.get('description', '')  # Default to empty if missing
            )
            db.session.add(new_subject)
            db.session.commit()
            return {'message': 'Subject created successfully', 'id': new_subject.id}, 201
        except Exception as e:
            db.session.rollback()
            return {'message': f'Error creating subject: {str(e)}'}, 500

    # @jwt_required()
    def put(self, subject_id):
        """Update a subject."""
        subject = Subject.query.get(subject_id)
        if not subject:
            return {'message': 'Subject not found'}, 404

        data = request.get_json()
        if not data:
            return {'message': 'No data provided'}, 400

        try:
            subject.name = data.get('name', subject.name)
            subject.description = data.get('description', subject.description)
            db.session.commit()
            return {'message': 'Subject updated successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': f'Error updating subject: {str(e)}'}, 500

    # @jwt_required()
    def delete(self, subject_id):
        """Delete a subject."""
        subject = Subject.query.get(subject_id)
        if not subject:
            return {'message': 'Subject not found'}, 404

        try:
            db.session.delete(subject)
            db.session.commit()
            return {'message': 'Subject deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': f'Error deleting subject: {str(e)}'}, 500

# --------------------------
# 📖 Chapter API
# --------------------------
class ChapterAPI(Resource):
    # @jwt_required()
    def get(self, subject_id=None):
        """Fetch all chapters or a specific chapter."""
        if subject_id:
            chapter = Chapter.query.get(subject_id)
            if chapter:
                return jsonify({
                    'id': chapter.id,
                    'name': chapter.name,
                    'description': chapter.description,
                    # 'subject_id': chapter.subject_id
                })
            return {'message': 'Chapter not found'}, 404
        # chapters = Chapter.query.all()
        # return jsonify([{
        #     'id': chapter.id,
        #     'name': chapter.name,
        #     'description': chapter.description,
        #     'subject_id': chapter.subject_id
        # } for chapter in chapters])

    def post(self):
        """Create a new chapter."""
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        subject_id = data.get('subject_id')

        if not name or not subject_id:
            return {'message': 'Name and subject_id are required'}, 400

        new_chapter = Chapter(name=name, description=description, subject_id=subject_id)
        db.session.add(new_chapter)
        db.session.commit()

        return {'message': 'Chapter created successfully', 'id': new_chapter.id}, 201

    def put(self, chapter_id):
        """Update a chapter."""
        chapter = Chapter.query.get(chapter_id)
        if not chapter:
            return {'message': 'Chapter not found'}, 404

        data = request.get_json()
        chapter.name = data.get('name', chapter.name)
        chapter.description = data.get('description', chapter.description)
        chapter.subject_id = data.get('subject_id', chapter.subject_id)
        db.session.commit()

        return {'message': 'Chapter updated successfully'}

    def delete(self, chapter_id):
        """Delete a chapter."""
        chapter = Chapter.query.get(chapter_id)
        if not chapter:
            return {'message': 'Chapter not found'}, 404

        db.session.delete(chapter)
        db.session.commit()
        return {'message': 'Chapter deleted successfully'}

# --------------------------
# 🧩 Quiz API
# --------------------------
class QuizAPI(Resource):
    # @jwt_required()
    def get(self, quiz_id=None):
        """Fetch all quizzes or a specific quiz."""
        if quiz_id:
            quiz = Quiz.query.get(quiz_id)
            if quiz:
                return jsonify({
                    'id': quiz.id,
                    'date_of_quiz': quiz.date_of_quiz.strftime('%Y-%m-%d'),
                    'time_duration': quiz.time_duration,
                    'remarks': quiz.remarks,
                    'chapter_id': quiz.chapter_id
                })
            return {'message': 'Quiz not found'}, 404
        quizzes = Quiz.query.all()
        return jsonify([{
            'id': quiz.id,
            'date_of_quiz': quiz.date_of_quiz.strftime('%Y-%m-%d'),
            'time_duration': quiz.time_duration,
            'remarks': quiz.remarks,
            'chapter_id': quiz.chapter_id
        } for quiz in quizzes])

    def post(self):
        """Create a new quiz."""
        data = request.get_json()
        date_of_quiz = data.get('date_of_quiz')
        time_duration = data.get('time_duration')
        remarks = data.get('remarks')
        chapter_id = data.get('chapter_id')

        if not date_of_quiz or not time_duration or not chapter_id:
            return {'message': 'Missing required fields'}, 400

        try:
            date_of_quiz = datetime.strptime(date_of_quiz, '%Y-%m-%d').date()
        except ValueError:
            return {'message': 'Invalid date format. Use YYYY-MM-DD.'}, 400

        new_quiz = Quiz(
            date_of_quiz=date_of_quiz,
            time_duration=time_duration,
            remarks=remarks,
            chapter_id=chapter_id
        )
        db.session.add(new_quiz)
        db.session.commit()

        return {'message': 'Quiz created successfully', 'id': new_quiz.id}, 201

    def put(self, quiz_id):
        """Update a quiz."""
        quiz = Quiz.query.get(quiz_id)
        if not quiz:
            return {'message': 'Quiz not found'}, 404

        data = request.get_json()
        quiz.date_of_quiz = datetime.strptime(data.get('date_of_quiz'), '%Y-%m-%d').date()
        quiz.time_duration = data.get('time_duration', quiz.time_duration)
        quiz.remarks = data.get('remarks', quiz.remarks)
        quiz.chapter_id = data.get('chapter_id', quiz.chapter_id)
        db.session.commit()

        return {'message': 'Quiz updated successfully'}

    def delete(self, quiz_id):
        """Delete a quiz."""
        quiz = Quiz.query.get(quiz_id)
        if not quiz:
            return {'message': 'Quiz not found'}, 404

        db.session.delete(quiz)
        db.session.commit()
        return {'message': 'Quiz deleted successfully'}

# --------------------------
# ❓ Question API
# --------------------------
class QuestionAPI(Resource):
    # @jwt_required()
    def get(self, question_id=None):
        """Fetch all questions or a specific question."""
        if question_id:
            question = Question.query.get(question_id)
            if question:
                return jsonify({
                    'id': question.id,
                    'question_statement': question.question_statement,
                    'option_1': question.option_1,
                    'option_2': question.option_2,
                    'option_3': question.option_3,
                    'option_4': question.option_4,
                    'correct_option': question.correct_option,
                    'quiz_id': question.quiz_id
                })
            return {'message': 'Question not found'}, 404
        questions = Question.query.all()
        return jsonify([{
            'id': question.id,
            'question_statement': question.question_statement,
            'option_1': question.option_1,
            'option_2': question.option_2,
            'option_3': question.option_3,
            'option_4': question.option_4,
            'correct_option': question.correct_option,
            'quiz_id': question.quiz_id
        } for question in questions])

    def post(self):
        """Create a new question."""
        data = request.get_json()
        question_statement = data.get('question_statement')
        option_1 = data.get('option_1')
        option_2 = data.get('option_2')
        option_3 = data.get('option_3')
        option_4 = data.get('option_4')
        correct_option = data.get('correct_option')
        quiz_id = data.get('quiz_id')

        if not question_statement or not option_1 or not option_2 or not option_3 or not option_4 or not correct_option or not quiz_id:
            return {'message': 'All fields are required'}, 400

        new_question = Question(
            question_statement=question_statement,
            option_1=option_1,
            option_2=option_2,
            option_3=option_3,
            option_4=option_4,
            correct_option=int(correct_option),
            quiz_id=quiz_id
        )
        db.session.add(new_question)
        db.session.commit()

        return {'message': 'Question created successfully', 'id': new_question.id}, 201

    def put(self, question_id):
        """Update a question."""
        question = Question.query.get(question_id)
        if not question:
            return {'message': 'Question not found'}, 404

        data = request.get_json()
        question.question_statement = data.get('question_statement', question.question_statement)
        question.option_1 = data.get('option_1', question.option_1)
        question.option_2 = data.get('option_2', question.option_2)
        question.option_3 = data.get('option_3', question.option_3)
        question.option_4 = data.get('option_4', question.option_4)
        question.correct_option = int(data.get('correct_option', question.correct_option))
        question.quiz_id = data.get('quiz_id', question.quiz_id)
        db.session.commit()

        return {'message': 'Question updated successfully'}

    def delete(self, question_id):
        """Delete a question."""
        question = Question.query.get(question_id)
        if not question:
            return {'message': 'Question not found'}, 404

        db.session.delete(question)
        db.session.commit()
        return {'message': 'Question deleted successfully'}

# --------------------------
# 🔗 Register API Resources
# --------------------------
api.add_resource(UserLoginAPI, '/login')
api.add_resource(TokenRefreshAPI, '/refresh')
api.add_resource(UserRegistrationAPI, '/register')



api.add_resource(UserAPI, '/users', '/users/<int:user_id>')
api.add_resource(SubjectAPI, '/subjects', '/subjects/<int:subject_id>')
api.add_resource(ChapterAPI,  '/chapters/<int:subject_id>')
api.add_resource(QuizAPI, '/quizzes', '/quizzes/<int:quiz_id>')
api.add_resource(QuestionAPI, '/questions', '/questions/<int:question_id>')




api.add_resource(QuizView, '/quiz/<int:chapter_id>')
api.add_resource(QuestionView,'/QuizQues/<int:quiz_id>')
api.add_resource(submitscore, '/scores')  # POST
api.add_resource(UserScores, '/scores/<int:user_id>')