# import dictionary as dic
# from data.sql import reader 
# import data.oracle.reader as oreader


#print(dic.allGuests)
#oreader.readfromoracle()

# from data.json import writer
# jsonstring = writer.jsontostring([2,'new','fun'])
# print(jsonstring)

# try:
#     10/0
# except NameError:
#     print('name error occurred!')
# else:
#     print('else line.')
# finally:
#     print('aleways')

# import os
# from data.json import reader
# print(os.getcwd())
# try:
#     content = reader.readfile("Automation/test.txt")
# except FileNotFoundError as err:
#     print(f'Cannot find file {err.args}')
# else:
#     print(content)



""" def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam) """
""" 
from animal import Dog

d = Dog('Chiwawa')
d.addTrick('Roll over')

dd = Dog('Golden retriever')
dd.addTrick('Retrieve')

print(d.tricks) """

""" import emailutil
emailutil.sendSmtpEmail()
print('email sent') """
