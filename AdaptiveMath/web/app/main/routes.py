from app import db #from app package import flask app 
from flask import render_template,flash,redirect,url_for,request,session, current_app
from app.main.forms import EditProfileForm, SingleQuestionForm, AdminForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from app.models import User, Record, Question, Skill, Category
from datetime import datetime
from app.main.test import get_random_questions
import json
import pandas as pd
from collections import namedtuple
from pathlib import Path
import os
import sys
from app.main import bp
from app.auth.routes import logout

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    user = User.query.filter_by(username = current_user.username).first()
    return render_template('index.html',title='home', user = user)



@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    current_app.logger.info('edit profile user name ' + current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',form=form)

@bp.route('/browse_skill', methods=['GET'])
@login_required
def browse_skill():
    page = request.args.get('page',1,type=int)
    skills = Skill.query.order_by(Skill.skill.desc()).paginate(page,current_app.config['ITEMS_PER_PAGE'],False)
    next_url = url_for('main.browse_skill',page=skills.next_num) if skills.has_next else None
    prev_url = url_for('main.browse_skill',page=skills.prev_num) if skills.has_prev else None
    return render_template('admin.html',skills = skills.items, next_url=next_url, prev_url=prev_url)

@bp.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    form = AdminForm()
    if request.method=='POST':
        if form.validate_on_submit():
            uploadfile = request.files['file']
            filename = uploadfile.filename
            print('uploadfile filename {}'.format(filename))
            if filename !='':
                savefile= os.path.join(current_app.config['UPLOAD_PATH'],filename)
                print('save file {}'.format(savefile))
                uploadfile.save(savefile)
                target = form.targettable.data
                print('target table {}'.format(target))
                __load_file(savefile,target)
                flash("{} added to database.".format(filename))

    return render_template('admin.html',form = form)

@bp.route('/start_practice', methods=['GET','POST'])
@login_required
def start_practice():    
    #get user id
    if not session.get('userid'):
        logout()
        return redirect(url_for('auth.login'))

    userid = int(session['userid'])
    print('userid session loaded with {}'.format(userid))    

    questionlist =__load_questions(userid, 1)

    if len(questionlist)> 0:
      
        q = questionlist[0]

        #print('1 question retrieved from session: '+ str(q))
        form = SingleQuestionForm()
        qid =  q['qid']
        form.qid.data = qid
        form.question.data = q['question']
        form.answer.data = q['answer']   

        #if validate submit, remove question from session['test']
        if form.validate_on_submit():
            #response = form.response.data
            #flash('Your answer is ' + response)

            #save response to records 
            print('start saving response to records ')
            if str(form.response.data).strip().upper() == str(form.answer.data).strip().upper():
                result = 1
            else:
                result = 0

            starttime =  datetime.now()
            endtime = datetime.now()
            sectaken = (endtime - starttime).seconds
            current_app.logger.info('question {} start {} end time {}.'.format(form.qid.data,starttime, endtime))
            record = Record(userid=userid,testid=0,questionid=int(form.qid.data),datecreated=datetime.now(),result=result,timetaken = sectaken,response = form.response.data)
            db.session.add(record)
            db.session.commit()
            print('end saving response to records. record {} saved.'.format(record))

            return redirect(url_for('main.start_practice'))
        else:
            print('form.validate_on_submit else reached.')
            return render_template('test.html', title='Practice',form = form)


@bp.route('/start_test', methods=['GET','POST'])
@login_required
def start_test():
    current_app.logger.info('start_test {}'.format(request.method))

    totalquestions = current_app.config['TOTAL_QUESTIONS_PER_TEST']

    if not session.get('userid'):
        logout()
        return redirect(url_for('auth.login'))

    #get user id
    userid = int(session['userid'])
    print('userid session loaded with {}'.format(userid))    


    #if its a new test, not imcomplete test from before
    #check if session['test'] not exists or count == 0
    if 'test' not in session or len(session['test']) == 0:
        #print('no test session')
 
        qlist =__load_questions(userid, totalquestions)
        print(qlist)
        session['test']=json.dumps(qlist)   
        print('test session loaded with' + session['test'])        

        #create test id     
        testid = datetime.now().strftime("%Y%m%d%H%M%S")
        session['testid']=str(testid)
        print('testid session loaded with {}'.format(testid))     

        
    #uncompleted test
    #retrieve 1 question  from session
    teststring = session['test']
    print('session test: {}'.format(teststring))
    # jstring = teststring.replace('"','"""').replace("'","\"")
    # print('jstring ' + jstring)  
    questionlist = json.loads(teststring)
    
    
    if len(questionlist)> 0:
      
        q = questionlist[0]

        #print('1 question retrieved from session: '+ str(q))
        form = SingleQuestionForm()
        qid =  q['qid']
        form.qid.data = qid
        form.question.data = q['question']
        form.answer.data = q['answer']   

        session[qid] =  datetime.now()
        current_app.logger.info('load question {}: {} at {} '.format(qid,q['question'],  datetime.now()))

        #log start time

        #if validate submit, remove question from session['test']
        if form.validate_on_submit():
            #response = form.response.data
            #flash('Your answer is ' + response)

            #save response to records 
            print('start saving response to records ')
            if str(form.response.data).strip().upper() == str(form.answer.data).strip().upper():
                result = 1
            else:
                result = 0

            starttime =  datetime.now()
            endtime = datetime.now()
            sectaken = (endtime - starttime).seconds
            current_app.logger.info('question {} start {} end time {}.'.format(form.qid.data,starttime, endtime))
            record = Record(userid=userid,testid=int(session['testid']),questionid=int(form.qid.data),datecreated=datetime.now(),result=result,timetaken = sectaken,response = form.response.data)
            db.session.add(record)
            db.session.commit()
            print('end saving response to records. record {} saved.'.format(record))

            del questionlist[0]
            print('questionlist: {}'.format(questionlist))
            session['test']=json.dumps(questionlist)   
            print('form validate_on_submit and queston removed from session. new session data: {}'.format(session['test']))

            return redirect(url_for('main.start_test'))
        else:
            print('else reached.')
            return render_template('test.html', title='Test',form = form)
    else:           
        correctrec, wrongrec,result = __test_summary()
        return render_template('test_done.html',title='Test', corrects = correctrec, mistakes = wrongrec,score=result)

def __load_questions(userid,num):
    #convert list of duples to list of dictionary
    questionList = get_random_questions(userid, num)
    # questions = ""
    # for question in questionList:
    #     q = '"qid":{},"question":{},"answer":{},'.format(question[0],question[1],question[2])      
    #     questions= questions + q
    # print('__load_question: {}'.format(questions))
    # return ''.join('{',questions,'}')
    return questionList


#todo:add result summary, score, wrong answer and explaination
def __test_summary():
    session['test']=''
    testid =int(session['testid'])
    records = Record.query.filter_by(testid=testid).all()
    #display result of test
    #correct secion, praises and points
    corrects = [r for r in records if r.result == 1]
    wrongs = [dict(r) for r in records if r.result == 0]
    wrongqidlist = [ r.questionid for r in records if r.result == 0]
    #print('wrongqidlist {}'.format(wrongqidlist))
    wrongexplained = []

    #use foreign key is easier, but this is kept for reference
    if len(wrongqidlist)> 0:
        dfwrong = pd.DataFrame(wrongs)
        #print('df wrong {}'.format(dfwrong))
        questions = Question.query.filter(Question.qid.in_(wrongqidlist))
        #print('questions {}'.format(questions))

        dfexplain = pd.DataFrame([dict(q) for q in questions])
        #print(dfexplain)
        dfwrongexplained = pd.merge(dfwrong,dfexplain,how='left',left_on='questionid', right_on='qid')
        wrongexplained = dfwrongexplained.to_dict('records')

    total = len(records)
    score = 0
    if total > 0 :
        score = round(len(corrects)/total*100)
    result = 'Score: {} ({} of {})'.format(score,len(corrects), total)
    #mistakes & explanation
    return corrects, wrongexplained, result


def __str_to_class(str):
    return getattr(sys.modules[__name__], str)

#load csv file to table
def __load_file(filepath,objectname):
    #read csv file as dictionary
    filename = Path(filepath)
    objectDt = pd.read_csv(filename).to_dict('records')
    objectList = []

    #create object from dictionary
    for q in objectDt:
        #question = Question(q)
        #print('q {} , object name {}'.format(q, objectname))
        obj = (__str_to_class(objectname))(q)
        objectList.append(obj)

    #save to database 
    db.session.bulk_save_objects(objectList)
    db.session.commit()



