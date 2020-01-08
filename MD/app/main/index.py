from flask import Blueprint, render_template, request

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/login')
def index(state = None):
    # /main/index.html =>  /MD/app/templates/main/index.html
    return render_template('/main/login.html', LoginState = "None")

@main.route('/main', methods=['POST', 'GET'])
def loginResult():
    if request.method =='POST':
        id = request.form['id']
        password = request.form['password']
        print(id)
        print(password)

        try:
            if id == '**' and password == '**':
                return render_template('/main/index.html')
            else:
               return render_template('/main/login.html', LoginState = "NO")

        except:
            return 'You are not registered'
