from flask import flask
app = flask(_name_)

@app.route("/")
def hello():
    return "Hi, happy Xmas."
  
if _name_ == "_main_":
  app.run(host='0.0.0.0')
