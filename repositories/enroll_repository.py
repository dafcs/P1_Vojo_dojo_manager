from db.run_sql import run_sql
from models.enroll import Enroll

def save(enroll):
    sql = "INSERT INTO enrollments (lesson_id,member_id) VALUES (%s,%s) RETURNING *"
    values = [enroll.lesson_id,enroll.member_id]
    row = run_sql(sql,values)
    # print(f'PRINTING repo.save>>>> ROW RUN SQL = {row}')
    enroll.id = row[0]['id']
    return enroll

def select(id):
    result = None
    sql = 'SELECT * FROM enrollments WHERE id = %s'
    values = [id]
    row = run_sql(sql,values)
    if row != None:
        val = row[0]
        result = Enroll(val['lesson_id'],val['member_id'],val['id'])
    return result
    

def select_all():
    result = []
    sql = 'SELECT * FROM enrollments'
    rows = run_sql(sql)
    for row in rows:
        enrollment = Enroll(row['lesson_id'],row['member_id'],row['id'])
        result.append(enrollment)
    return result

def delete(id):
    sql = 'DELETE FROM enrollments WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def delete_all():
    sql = 'DELETE FROM enrollments'
    run_sql(sql)

def update(enroll):
    sql = 'UPDATE enrollments SET (lesson_id,member_id) = (%s,%s) WHERE id = %s'
    values = [enroll.lesson_id,enroll.member_id,enroll.id]
    run_sql(sql,values)
