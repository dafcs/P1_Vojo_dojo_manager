from flask import Blueprint
from flask import request, render_template, redirect
from models.lesson import Lesson
from models.member import Member
from models.enroll import Enroll
import repositories.member_repository as member_repo
import repositories.enroll_repository as enroll_repo
import repositories.lesson_repository as lesson_repo

enrollments_blueprint = Blueprint("enrollments", __name__)

@enrollments_blueprint.route('/enroll',methods=['GET'])
def enroll_show():
    members = member_repo.select_all()
    lessons = lesson_repo.select_all()
    return render_template('/enroll/enroll.jinja',lessons = lessons,members = members)

@enrollments_blueprint.route('/enroll',methods=['POST'])
def member_enroll():
    lesson_id = request.form['lesson_id']
    member_id = request.form['member_id']
    enroll = Enroll(lesson_id,member_id)
    enroll_repo.save(enroll)
    return redirect('/enroll')
    

