
import time
import datetime
from user import get_id_by_name
from question import get_random_questions
from record import save_record_to_database



def create_test_set(username,numquestion):
    userid = get_id_by_name(username)
    testid = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    #get questions always answered wrong

    #get easier questions for above

    #get questions answered wrong before and the latest record is still wrong

    #get questions that has been wrong in the last 3 tests

    #get some random questions
    questionList = get_random_questions(3)
    return userid, testid, questionList


"""
Run a set of test
"""
def show_test():
    uid, tid, questionlist = create_test_set('luna',2)
    starttime = time.time()
    for question in questionlist:
        try:
            qid = question[0]
            q = question[1]
            a = question[2]
            userinput = input("Question: " + q )

            while str(userinput) != str(a):
                print('Wrong answer. Try again')
                save_record_to_database(uid,tid,qid,datetime.datetime.now(),-1)
                userinput = input("Question: " + q )

            print('Correct!')
            save_record_to_database(uid,tid,qid,datetime.datetime.now(),1)

        except KeyboardInterrupt:
            break # The answer was in the question!
        except Exception as e:
            print('Exit test. ' + str(e))
            break

    endtime = time.time()
    timespan = time.strftime('%H:%M:%S', time.gmtime(endtime - starttime))
    print('time: ' + str(timespan))



show_test()