DBCONNECTIONSTRING = 'sqlite:///database/adapt_math.db'

from datetime import datetime
starttime = datetime.now()
sectaken = 60



endtime = datetime.now()

print(starttime)
print(endtime)
print('time taken {}'.format( (endtime- starttime).seconds ))