from flask import Flask, render_template
# from flask_bootstrap import Bootstrap


app = Flask(__name__)
# bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    print("Anmol")
    print("New changes for the demo purpose")
    # Changes in code
    # Changes in code

    return render_template('index.html')