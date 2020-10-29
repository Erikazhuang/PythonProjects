import app.dbaccess as db
import pandas as pd
from datetime import datetime
from flask import current_app
import random


def generate_plus_questions_all(maxnum=20):
    questions = list()

    for x in range(0,maxnum + 1):
        if x>10:
            for y in range(0,11):
                questions.append( ("{0} + {1} = ".format(x,y), '{0}'.format(x + y),0,'basic calculation',datetime.now(),1) )
        else:
            for y in range(0,maxnum):
                questions.append( ("{0} + {1} = ".format(x,y),'{0}'.format(x + y),0,'basic calculation',datetime.now(),1) )

    df = pd.DataFrame(questions)
    df.columns = ['question','answer','level','type','datecreated','active']
    return df

def append_question_to_database(questiondf):
    conn = db.create_connection(current_app.config['SQLALCHEMY_DATABASE_URI'])
    questiondf.to_sql('question',conn,if_exists='append',index_label='qid')

def replace_question_to_database(questiondf):
    conn = db.create_connection(current_app.config['SQLALCHEMY_DATABASE_URI'])
    questiondf.to_sql('question',conn, if_exists='replace',index_label='qid')

def __get_all_questions():
    query = 'SELECT qid,question,answer FROM question'
    conn = db.create_connection(current_app.config['SQLALCHEMY_DATABASE_URI'])
    result = db.read_dataframe_query(query,conn)
    return result

def __get_new_questions(userid):
    query = """    
            SELECT qid, question, answer
            FROM question q  LEFT join (select * from record where result<> 1 and userid = {}) r on  q.qid = r.questionid 
            where r.questionid is NULL
            """.format(userid)
    conn = db.create_connection(current_app.config['SQLALCHEMY_DATABASE_URI'])
    result = db.read_dataframe_query(query,conn)
    return result

def get_random_questions(userid, num):
    allquestions = __get_new_questions(userid).to_dict('records') #convert dataframe to a list of dictionary
    #print(allquestions)
    total = len(allquestions)
    print('get_random_questions total {}, num is {}'.format(total,num))
    
    randomquestions = random.sample(allquestions,k= num if total>=num else total ) #sample random questions from the list
    return randomquestions