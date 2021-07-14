from flask import Flask

app = Flask(__name__)


@app.route('/user/<name>')
def home(name):
    return "Hello %s" % name

@app.route('/agedetail/<int:age>')
def agedetail(age):
    return "my age is %d" % age


if __name__ == '__main__':
    app.debug = True
    app.run()
