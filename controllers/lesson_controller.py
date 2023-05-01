from flask import Blueprint
from flask import request, render_template, redirect
import repositories.lesson_repository as lesson_repo
from models.lesson import Lesson

lessons_blueprint = Blueprint("lessons", __name__)

@lessons_blueprint.route('/lessons',methods=['GET'])
def lessons_base():
    lessons = lesson_repo.select_all()
    return render_template('/lesson/lessons_base.jinja',lessons = lessons)

@lessons_blueprint.route('/lesson_form',methods=['GET'])
def lesson_form():
    lessons = lesson_repo.select_all()
    return render_template('/lesson/lesson_add.jinja',lessons = lessons)

@lessons_blueprint.route('/lesson_form/add',methods=['POST'])
def lesson_add():
    name = request.form['name']
    lesson= Lesson(name)
    lesson_repo.save(lesson)
    return redirect('/lessons')

@lessons_blueprint.route('/lesson/<id>',methods=['GET'])
def edit_member(id):
    lesson = lesson_repo.select(id)
    return render_template('/lesson/lesson_update.jinja',lesson = lesson)

@lessons_blueprint.route('/lesson/<id>/update',methods=['POST'])
def update_member(id):
    name = request.form['name']
    lesson = Lesson(name,id)
    lesson_repo.update(lesson)
    return redirect('/lessons')

@lessons_blueprint.route('/lesson/<id>/delete',methods=['POST'])
def member_delete(id):
    lesson_repo.delete(id)
    return redirect('/lessons')

@lessons_blueprint.route('/lesson/<id>/show', methods=['GET'])
def member_show(id):
    lesson = lesson_repo.select(id)
    return render_template('/lesson/lesson_page.jinja', lesson = lesson)