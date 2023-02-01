from flask import Flask
app = Flask(__name__)
@app.route('/')
def main():
    return "첫번째 페이지"

@app.route('/greet')
def greeting():
    return 'Hello World!'

@app.route('/greet1')
def greeting2():
    return '고로롱'

@app.route('/greet2')
def greeting3():
    return '냐항~'

if __name__ == "__main__":
    app.run(debug=True)