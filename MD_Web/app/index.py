from flask import render_template, request
from flask import Flask
from collections import Counter
import pymysql
from datetime import datetime, timedelta

db = pymysql.connect("52.14.78.174", "root", "peoplespace5", "md_db")
#db = pymysql.connect("localhost", "root", "temp", "md_db")

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def index(state=None):
    return render_template('/login.html', LoginState="None")

@app.route('/main', methods=['POST', 'GET'])
def loginResult():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        print(id)
        print(password)

        try:
            if id == 'admin' and password == '12345':
                return render_template('/index.html', usage=usageResult(), dateCnt = dateCntResult(),
                                     causeTotal = causeCnt())
            else:
                return render_template('/login.html', LoginState="NO")

        except:
            return 'You are not registered'
dateList = []
dateCnt = [0,0,0,0,0,0,0]
causeTotal = [0,0,0,0,0,0]
def usageResult():
    totalusage = [10,20,30,20,10,30]
    cursor = db.cursor()
    sql = "SELECT * FROM application"
    cursor.execute(sql)
    sqlresult = cursor.fetchall()
    print(sqlresult)

    #보낼데이터 : dateList, dateCnt
    today = datetime.today()
    for i in range(0,7):
        date = today + timedelta(days=-i)
        dateList.append(str(date)[:10])
    print(dateList)

    peopleUsage = []
    cause =[]
    for row in sqlresult:
        peopleUsage.append(row[1])
        cause.append(row[2])

    peopleUsageCnt = Counter(peopleUsage)
    causeCnt = Counter(cause)

    for key in peopleUsageCnt:
        if str(key)[:10] in dateList:
            location = dateList.index(str(key)[:10])
            dateCnt[location] = peopleUsageCnt[key]
        print(str(key)[:10], peopleUsageCnt[key])
    print(dateCnt)

    #넘길데이터 : causeNameList, causeTotal
    causeNameList = ['bad_ball_joint', 'bad_brake_pad', 'engine_seizing_up',
                     'failing_water_pump', 'hole_in_muffler', 'no_problem']
    for key in causeCnt:
        if key in causeNameList:
            location = causeNameList.index(key)
            causeTotal[location] = causeCnt[key]
        print(key, causeCnt[key])
    print(causeTotal)

    print(dateCnt)
    print(causeTotal)
    return dateCnt

def dateCntResult():
    return dateCnt
def causeCnt():
    return causeTotal


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
