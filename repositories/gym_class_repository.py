from db.run_sql import run_sql
from models.gym_class import GymClass


def save(gym_class):
    sql = "INSERT INTO classes (name) VALUES (%s) RETURNING id"
    values = [gym_class.name]
    row = run_sql(sql,values)
    # print(f'PRINTING repo.save>>>> ROW RUN SQL = {row}')
    gym_class.id = row[0]['id']
    return gym_class

def select(id):
    result = None
    sql = 'SELECT * FROM classes WHERE id = %s'
    values = [id]
    row = run_sql(sql,values)
    if row != None:
        val = row[0]
        result = GymClass(val['name'],val['id'])
    return result
    

def select_all():
    result = []
    sql = 'SELECT * FROM classes'
    rows = run_sql(sql)
    for row in rows:
        gym_class = GymClass(row['name'],row['id'])
        result.append(gym_class)
    return result

def delete(id):
    sql = 'DELETE FROM classes WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def delete_all():
    sql = 'DELETE FROM classes'
    run_sql(sql)