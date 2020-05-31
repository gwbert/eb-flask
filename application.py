from flask import Flask, render_template, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from config import Config
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import json
from string import Template

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/quiz/<quizName>")
def quiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('quiz.html', quizName=quizName, myObject=myObject)

@app.route("/smallquiz/<quizName>")
def smallquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('smallquiz.html', quizName=quizName, myObject=myObject)

@app.route("/picturequiz/<quizName>")
def picturequiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('picturequiz.html', quizName=quizName, myObject=myObject)

@app.route("/picturequiz2/<quizName>")
def picturequiz2(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('picturequiz2.html', quizName=quizName, myObject=myObject)

@app.route("/picturequiz3/<quizName>")
def picturequiz3(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('picturequiz3.html', quizName=quizName, myObject=myObject)

@app.route("/mediumquiz/<quizName>")
def mediumquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('mediumquiz.html', quizName=quizName, myObject=myObject)

@app.route("/eightquiz/<quizName>")
def eightquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('eightquiz.html', quizName=quizName, myObject=myObject)

@app.route("/twelvequiz/<quizName>")
def twelvequiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('twelvequiz.html', quizName=quizName, myObject=myObject)

@app.route("/twentyquiz/<quizName>")
def twentyquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('twentyquiz.html', quizName=quizName, myObject=myObject)

@app.route("/tenquiz/<quizName>")
def tenquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('tenquiz.html', quizName=quizName, myObject=myObject)

@app.route("/fifteenquiz/<quizName>")
def fifteenquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('fifteenquiz.html', quizName=quizName, myObject=myObject)

@app.route("/sixteenquiz/<quizName>")
def sixteenquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('sixteenquiz.html', quizName=quizName, myObject=myObject)

@app.route("/fivequiz/<quizName>")
def fivequiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('fivequiz.html', quizName=quizName, myObject=myObject)

@app.route("/shirequiz/<quizName>")
def shirequiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('shirequiz.html', quizName=quizName, myObject=myObject)

@app.route("/jumboquiz/<quizName>")
def jumboquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('jumboquiz.html', quizName=quizName, myObject=myObject)

@app.route("/footballquiz/<quizName>")
def footballquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('footballquiz.html', quizName=quizName, myObject=myObject)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/sport")
def sport():
    return render_template('sport.html')

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/subscribe")
def subscribe():
    return render_template('subscribe.html')

@app.route("/geography")
def geography():
    return render_template('geography.html')

@app.route("/general")
def general():
    return render_template('general.html')

@app.route("/highlands")
def highlands():
    return render_template('highlands.html')

@app.route("/mountains")
def mountains():
    return render_template('mountains.html')

@app.route("/people")
def people():
    return render_template('people.html')

@app.route("/history")
def history():
    return render_template('history.html')

@app.route("/culture")
def culture():
    return render_template('culture.html')

@app.route("/jumbo")
def jumbo():
    return render_template('jumbo.html')

application = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=False)