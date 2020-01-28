from flask import render_template, request
from flask import Flask
import pymongo

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
    result = []
    #temp setting
    for i in range(1):
        result.append(
            {
                "bad ball joint": totalusage[0],
                "bad brake pad": totalusage[1],
                "engine running without oil+engine seizing up": totalusage[2],
                "failing water pump": totalusage[3],
                "hole in muffler": totalusage[4],
                "normal": totalusage[5]

            }
        )
    return result


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
