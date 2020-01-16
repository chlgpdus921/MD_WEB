from flask import render_template, request
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def index(state = None):
    return render_template('/login.html', LoginState = "None")

@app.route('/main', methods=['POST', 'GET'])
def loginResult():
    if request.method =='POST':
        id = request.form['id']
        password = request.form['password']
        print(id)
        print(password)

        try:
            if id == 'admin' and password == '12345':
                return render_template('/index.html')
            else:
               return render_template('/login.html', LoginState = "NO")

        except:
            return 'You are not registered'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

