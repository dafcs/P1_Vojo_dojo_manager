from db.run_sql import run_sql
from models.lesson import Lesson


def save(lesson):
    sql = "INSERT INTO lessons (name) VALUES (%s) RETURNING id"
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
        result = Lesson(val['name'],val['id'])
    return result
    

def select_all():
    result = []
    sql = 'SELECT * FROM lessons'
    rows = run_sql(sql)
    for row in rows:
        lesson = Lesson(row['name'],row['id'])
        result.append(lesson)
    return result

def delete(id):
    sql = 'DELETE FROM lessons WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def delete_all():
    sql = 'DELETE FROM lessons'
    run_sql(sql)

def update(member):
    sql = 'UPDATE lessons SET (name) = (%s) WHERE id = %s'
    values = [member.name]
    run_sql(sql,values)
