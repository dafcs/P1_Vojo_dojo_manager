from flask import Flask, render_template

# from controllers.gym_class_controller import placeholder
# from controllers.gym_member_controller import placeholder
# from controllers.gym_room_controller import placeholder

app = Flask(__name__)

# app.register_blueprint(blueprint_name)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)