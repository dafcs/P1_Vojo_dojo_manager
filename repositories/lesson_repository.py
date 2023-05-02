from db.run_sql import run_sql
from models.lesson import Lesson
import datetime

def save(lesson):
    sql = "INSERT INTO lessons (name,date,time) VALUES (%s,%s,%s) RETURNING id"
    values = [lesson.name]
    row = run_sql(sql,values)
    # print(f'PRINTING repo.save>>>> ROW RUN SQL = {row}')
    lesson.id = row[0]['id']
    return lesson

def select(id):
    result = None
    sql = 'SELECT * FROM lessons WHERE id = %s'
    values = [id]
    row = run_sql(sql,values)
    if row != None:
        val = row[0]
        result = Lesson(val['name'],val['date'],val['time'],val['id'])
    return result
    
def select_all():
    result = []
    sql = 'SELECT * FROM lessons'
    rows = run_sql(sql)
    for row in rows:
        lesson = Lesson(row['name'],row['date'],row['time'],row['id'])
        result.append(lesson)
    return result

def delete(id):
    sql = 'DELETE FROM lessons WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def delete_all():
    sql = 'DELETE FROM lessons'
    run_sql(sql)

def update(lesson):
    sql = 'UPDATE lessons SET (name,date,time) = (%s,%s,%s) WHERE id = %s'
    values = [lesson.name,lesson.date,lesson.time,lesson.id]
    run_sql(sql,values)

def upcoming_lessons():
    lesson_list = []
    sql = 'SELECT * FROM lessons WHERE date > CURRENT_DATE OR (date = CURRENT_DATE AND time > CURRENT_TIME)'
    results = run_sql(sql)
    for lessons in results:
        my_lesson = Lesson(lessons['name'],lessons['date'],lessons['time'])
        lesson_list.append(my_lesson)
    return lesson_list



# def lessons_for_member(member):
#     locations = []
#     sql = "SELECT lessons.* FROM lessons INNER JOIN enrollments ON enrollment.lesson_id = lesson.id WHERE member_id = %s"
#     values = [member.id]
#     results = run_sql(sql, values)

#     for row in results:
#         location = Lesson(row['name'], row['category'], row['id'])
#         locations.append(location)

#     return locations