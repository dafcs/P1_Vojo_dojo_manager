from flask import Flask, render_template

from controllers.lesson_controller import lessons_blueprint
from controllers.member_controller import member_blueprint
from controllers.enroll_controller import enrollments_blueprint

app = Flask(__name__)

app.register_blueprint(member_blueprint)
app.register_blueprint(lessons_blueprint)
app.register_blueprint(enrollments_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)