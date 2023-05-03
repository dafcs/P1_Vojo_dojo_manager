from db.run_sql import run_sql
from flask import Blueprint
from flask import request, render_template, redirect
import repositories.member_repository as member_repo
import repositories.lesson_repository as lesson_repo
from models.member import Member

member_blueprint = Blueprint("member", __name__)

@member_blueprint.route('/members',methods=['GET'])
def member_base():
    members = member_repo.select_all()
    return render_template('/member/member_base.jinja',members = members)

@member_blueprint.route('/member_form',methods=['GET'])
def member_form():
    members = member_repo.select_all()
    return render_template('/member/member_add.jinja',members = members)

@member_blueprint.route('/member_form/add',methods=['POST'])
def member_add():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership = request.form['membership_type']
    member = Member(first_name,last_name,membership)
    member_repo.save(member)
    return redirect('/members')

@member_blueprint.route('/member/<id>',methods=['GET'])
def edit_member(id):
    member = member_repo.select(id)
    return render_template('member/member_update.jinja',member = member)

@member_blueprint.route('/member/<id>/update',methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership_type = request.form['membership_type']
    account_status = request.form['account_status']
    member = Member(first_name,last_name,membership_type,account_status,id)
    member_repo.update(member)
    return redirect('/members')

@member_blueprint.route('/member/<id>/delete',methods=['POST'])
def member_delete(id):
    member_repo.delete(id)
    return redirect('/members')

@member_blueprint.route('/member/<id>/show', methods=['GET'])
def member_show(id):
    member = member_repo.select(id)
    lessons = lesson_repo.lessons_for_member(member)
    return render_template('/member/member_page.jinja', member = member,lessons = lessons)