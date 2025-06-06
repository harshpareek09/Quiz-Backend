# This file is the entry point of your backend Flask application.
# It sets up the app, registers routes, and starts the server.

from flask import Flask
from db_config import get_db_connection
from routes.student_routes import student_bp
from routes.teacher_routes import teacher_bp  # ✅ Correct import

app = Flask(__name__)

# Health check route to test DB connection
@app.route('/')
def home():
    try:
        conn = get_db_connection()
        if conn.is_connected():
            return "✅ Database connected successfully!"
    except Exception as e:
        return f"❌ Connection failed: {e}"

# Register Blueprints with URL prefixes
app.register_blueprint(student_bp, url_prefix='/student')
app.register_blueprint(teacher_bp, url_prefix='/teacher')

if __name__ == '__main__':
    print("🚀 Starting Flask server...")
    app.run(debug=True)
