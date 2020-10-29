from settings import DBCONNECTIONSTRING
import database.dbaccess as db
import pandas as pd

def save_record_to_database(uid,tid,qid,createdate,result):
    try:
        df=pd.DataFrame({'userid':[uid],'testid':[tid],'questionid':[qid],'createdate':[createdate],'result':[result]})
        conn = db.create_connection(DBCONNECTIONSTRING)
        df.to_sql('records',conn,if_exists='append',index_label='id',index=False)
        return True
    except Exception as e:
        print('save_record_to_database error. ' + str(e))
        return False

def get_records_by_userid(userid):
    try:
        conn = db.create_connection(DBCONNECTIONSTRING)
        sql = 'select * from records where userid = {0}'.format(userid)
        df = db.read_dataframe_query(sql,conn)
        return df
    except Exception as e:
        print('get_records_by_userid error. ' + str(e))

def get_wrong_questions(df):
    df.sort_values(by='result')
    return df