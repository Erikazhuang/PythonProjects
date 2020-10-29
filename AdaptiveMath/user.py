import database.dbaccess as db
from settings import DBCONNECTIONSTRING

def get_all_users():
    pass

def get_id_by_name(username):
    userid = 0
    sql = "select * from users where username='{0}'".format(username)

    try:
        conn = db.create_connection(DBCONNECTIONSTRING)
        user = db.read_dataframe_query(sql,conn)
        userid = user['id'].iloc[0]
    except Exception as e:
        print('error access users in database. ' + str(e))

    return userid