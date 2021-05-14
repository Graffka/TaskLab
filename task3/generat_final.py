import random
import datetime
from datetime import datetime


#date=datetime.datetime
strok=17020
f=open('generat.log', 'w')
i=1


timestamp = 1618797322.021

while i < strok:
    konc=random.randint(0,1)
    litrs=str(random.randint(1,100))
    if konc == 0:
        kstr=']-wanna top up '
    else:
        kstr=']-wanna scoop '

    date_time = datetime.fromtimestamp(timestamp)
    rsek=str(random.randint(100,999))
    d = date_time.strftime("%Y-%m-%dT%H:%M:%S")
    k=str(i)

    #iv=date
    f.write(d+'.'+ rsek+'Z–[username'+k+''+kstr+''+litrs+'l'+'\n')
    i=i+1
    timestamp=timestamp+1.31

f.close()



