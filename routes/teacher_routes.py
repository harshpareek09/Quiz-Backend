# routes/teacher_routes.py

from flask import Blueprint, request, jsonify
import mysql.connector
from db_config import get_db_connection

# Blueprint for teacher-related routes
teacher_bp = Blueprint('teacher', __name__)

# POST route for teacher login
@teacher_bp.route('/login', methods=['POST'])
def teacher_login():
    # Step 1: Extract request data
    data = request.get_json()
    teacher_id = data.get('teacher_id')
    full_name = data.get('full_name')
    password = data.get('password')

    # Step 2: Validate required fields
    if not teacher_id or not full_name or not password:
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400

    try:
        # Step 3: Connect to the DB
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Step 4: Query to verify teacher credentials
        query = "SELECT * FROM teachers WHERE teacher_id = %s AND full_name = %s AND password = %s"
        cursor.execute(query, (teacher_id, full_name, password))
        teacher = cursor.fetchone()

        # Step 5: Close connection
        cursor.close()
        conn.close()

        # Step 6: Return appropriate response
        if teacher:
            return jsonify({'success': True, 'message': 'Login successful', 'teacher': teacher}), 200
        else:
            return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

    except mysql.connector.Error as err:
        return jsonify({'success': False, 'message': f'Database error: {err}'}), 500



# POST route to add a question to a quiz
@teacher_bp.route('/add-question', methods=['POST'])
def add_question():
    data = request.get_json()

    quiz_id = data.get('quiz_id')
    question_text = data.get('question_text')
    option1 = data.get('option1')
    option2 = data.get('option2')
    option3 = data.get('option3')
    option4 = data.get('option4')
    correct_option = data.get('correct_option')

    # Validate input
    if not all([quiz_id, question_text, option1, option2, option3, option4, correct_option]):
        return jsonify({'success': False, 'message': 'All fields are required'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert question into DB
        insert_query = """
            INSERT INTO questions (quiz_id, question_text, option1, option2, option3, option4, correct_option)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            quiz_id, question_text, option1, option2, option3, option4, correct_option
        ))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'success': True, 'message': 'Question added successfully'}), 201

    except mysql.connector.Error as err:
        return jsonify({'success': False, 'message': f'Database error: {err}'}), 500


# ✅ Get all results for a specific quiz
@teacher_bp.route('/results/<int:quiz_id>', methods=['GET'])
def get_quiz_results(quiz_id):
    try:
        # Step 1: Connect to DB
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Step 2: Get quiz title
        cursor.execute("SELECT title FROM quizzes WHERE quiz_id = %s", (quiz_id,))
        quiz = cursor.fetchone()
        quiz_title = quiz['title'] if quiz else "Unknown Quiz"

        # Step 3: Fetch all results for this quiz
        cursor.execute("""
            SELECT student_email, total_score, cheating_detected, reason
            FROM final_results
            WHERE quiz_id = %s
        """, (quiz_id,))
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        # Step 4: Return results list
        return jsonify({
            'success': True,
            'quiz_id': quiz_id,
            'quiz_title': quiz_title,
            'results': results
        }), 200

    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500
