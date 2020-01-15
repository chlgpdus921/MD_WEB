from flask import Flask

# 추가할 모듈이 있다면 추가

app = Flask(__name__, template_folder='templates')

# 파일 이름이 index.py이므로
from app import index
app.run(debug=True)