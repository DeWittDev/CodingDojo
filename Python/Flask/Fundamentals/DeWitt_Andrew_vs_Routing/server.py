from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to my "Hello World!"'

@app.route('/dojo')
def Dojo():
    return "Dojo"

@app.route('/say/<str:name>')
def say(name):
    return "Hi " + name.capitalize()

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    name = name + "<br/>"
    return f"{name * num}"



@app.route("/", defaults={"path": ""})
@app.route("/<string:path>")
@app.route("/<path:path>")
def anythingElse(path):
    return 'Sorry! No Response. Try again.'

if __name__=="__main__":
    app.run(debug=True)