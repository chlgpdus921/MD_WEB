from app import app
from flask import render_template, request

@app.route('/')
@app.route('/login')
def index(state = None):
    # /main/index.html =>  /MD/app/templates/main/index.html
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
