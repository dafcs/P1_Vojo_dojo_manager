from db.run_sql import run_sql
from models.gym_room import GymRoom

def save(room):
    sql = 'INSERT INTO rooms (name,last_name,capacity) VALUES (%s,%s)'
    values = [room.name,room.capacity]
    row = run_sql(sql,values)[0]
    room.id = row.id
    return room

def select(id):
    result = None
    sql = 'SELECT * FROM rooms WHERE id = %s'
    values = [id]
    row = run_sql(sql,values)[0]
    if row != None:
        result = GymRoom(row['name'],row['capacity'],row['id'])
    return result
    

def select_all():
    result = []
    sql = 'SELECT * FROM rooms'
    rows = run_sql(sql)
    for row in rows:
        gym_room = GymRoom(row['name'],row['capacity'],row['id'])
        result.append(gym_room)
    return result

def delete(id):
    sql = 'DELETE FROM rooms WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def delete_all():
    sql = 'DELETE FROM rooms'
    run_sql(sql)