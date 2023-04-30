from db.run_sql import run_sql
from models.gym_member import GymMember

def save(member):
    sql = 'INSERT INTO members (first_name,last_name,membership_type,account_status) VALUES (%s,%s,%s,%s)'
    values = [member.first_name,member.last_name,member.membership_type,member.account_status]
    row = run_sql(sql,values)[0]
    member.id = row.id
    return member

def select(id):
    result = None
    sql = 'SELECT * FROM members WHERE id = %s'
    values = [id]
    row = run_sql(sql,values)[0]
    if row != None:
        result = GymMember(row['first_name'],row['last_name'],row['membership_type'],row['account_status'],row['id'])
    return result
    

def select_all():
    result = []
    sql = 'SELECT * FROM members'
    rows = run_sql(sql)
    for row in rows:
        gym_member = GymMember(row['first_name'],row['last_name'],row['membership_type'],row['account_status'],row['id'])
        result.append(gym_member)
    return result

def delete(id):
    sql = 'DELETE FROM members WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def delete_all():
    sql = 'DELETE FROM members'
    run_sql(sql)