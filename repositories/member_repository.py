from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = 'INSERT INTO members (first_name,last_name,membership_type,account_status) VALUES (%s,%s,%s,%s) RETURNING *'
    values = [member.first_name,member.last_name,member.membership_type,member.account_status]
    row = run_sql(sql,values)
    # print(f'PRINTING member_repo row = {row}')
    member.id = row[0]['id']
    return member

def select(id):
    result = None
    sql = 'SELECT * FROM members WHERE id = %s'
    values = [id]
    row = run_sql(sql,values)[0]
    if row != None:
        result = Member(row['first_name'],row['last_name'],row['membership_type'],row['account_status'],row['id'])
    return result
    
def select_all():
    result = []
    sql = 'SELECT * FROM members'
    rows = run_sql(sql)
    for row in rows:
        gym_member = Member(row['first_name'],row['last_name'],row['membership_type'],row['account_status'],row['id'])
        result.append(gym_member)
    return result

def update(member):
    sql = 'UPDATE members SET (first_name,last_name,membership_type,account_status) = (%s,%s,%s,%s) WHERE id = %s'
    values = [member.first_name,member.last_name,member.membership_type,member.account_status,member.id]
    run_sql(sql,values)


def delete(id):
    sql = 'DELETE FROM members WHERE id = %s'
    values = [id]
    run_sql(sql,values)

def delete_all():
    sql = 'DELETE FROM members'
    run_sql(sql)