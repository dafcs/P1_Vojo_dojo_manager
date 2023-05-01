from flask import Flask, render_template

# from controllers.lesson_controller import placeholder
from controllers.member_controller import member_blueprint
# from controllers.room_controller import placeholder

app = Flask(__name__)

app.register_blueprint(member_blueprint)
# app.register_blueprint(member_blueprint)
# app.register_blueprint(member_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)