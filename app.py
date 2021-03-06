from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html');
 
@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'index.html',name=name)
 
if __name__ == '__main__':
 
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)