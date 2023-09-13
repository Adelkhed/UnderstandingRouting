from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello World!"

@app.route("/dojo")
def dojo():
  return "Dojo !"

@app.route("/say/<string:name>")
def say_name(name):
  return f"HI {name} !"

@app.route("/repeat/<int:num>/<string:word>")
def repeat_word(num,word):
  return word * num
@app.errorhandler(404)
def not_found(error):
  return "sorry! No Response. Try again."

if __name__ == "__main__":
  app.run(debug=True)