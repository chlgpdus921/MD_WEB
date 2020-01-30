from flask import render_template, request
from flask import Flask
from collections import Counter
import pymysql

db = pymysql.connect("13.59.126.198", "root", "peoplespace5", "md_db")

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
                return render_template('/index.html', usage=usageResult())
            else:
                return render_template('/login.html', LoginState="NO")

        except:
            return 'You are not registered'

def usageResult():
    totalusage = [10,20,30,20,10,30]
    cursor = db.cursor()
    sql = "SELECT * FROM application"
    cursor.execute(sql)
    sqlresult = cursor.fetchall()
    print(sqlresult)

    peopleUsage = []
    cause =[]
    for row in sqlresult:
        #print(row[1])
        #print(row[2])
        peopleUsage.append(row[1])
        cause.append(row[2])

    peopleUsageCnt = Counter(peopleUsage)
    causeCnt = Counter(cause)
    causeCntValue = Counter(causeCnt).values()

    for key in peopleUsageCnt:
        print(key, peopleUsageCnt[key])
    for key in causeCnt:
        print(key, causeCnt[key])

    result = []
    #temp setting
    for i in range(len(totalusage)):
        result.append(
            {
                "usertotal": totalusage[i]
            }
        )
    #print(result)
    #print(totalusage)
    return totalusage


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
