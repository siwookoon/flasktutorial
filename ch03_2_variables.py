# _*_ coding:utf-8 _*_

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hi():
    return 'HI'

@app.route('/greet/<name>')
def greeting(name):
    return f'안녕{name}'

@app.route('/myblog/<num>')
def myblog(num):
    return f'나의 블로그 - {num}'

# 수정번호 - 0.1, 실수형

@app.route('/edit/<float:n0>')
def edit(no):
    print(type(no))
    return f'수정번호 - {no}'

if __name__ == '__main__':
    app.run(debug=True)
