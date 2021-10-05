import webbrowser
import sched, time
import pandas as pd
from datetime import datetime

s = sched.scheduler(time.time, time.sleep)
df= pd.read_csv('./data.csv')


def open (a):
    a=str(a)
    a= a.strip()
    # if(a[0:5] != 'https://'):
    #     a= 'https://' +a
    webbrowser.open(a)


for x in df.itertuples():
    date1= datetime.strptime(x[1],"%d/%m/%y %H:%M")

    td= datetime.now().day
    tm= datetime.now().month
    ty= datetime.now().year

    if(datetime.now().weekday()== date1.weekday()):
        date1.replace(day=td, month=tm, year=ty)

        t= (date1-datetime.now())
        seconds = t.seconds

        s.enter( seconds,1,open, argument=(x[2],))

s.run()
