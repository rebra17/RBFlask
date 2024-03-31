from flask import Flask, render_template

from scripts.intro import intro, summary
from scripts.profExp import flugger, bilka, siemens, cie, newtec, hpp
from scripts.edu import msc, bscSDU, bscSU
from scripts.awards import otg, tic, dtu
from scripts.projects import project
from scripts.services import services

comp = [hpp(), newtec(), cie(), siemens(), bilka(), flugger()]
edu = [msc(), bscSDU(), bscSU()]
compLen = len(comp)
eduLen = len(edu)
projectLen = project()
serviceLen = services()
introLen = intro()
hdrs = ["About Me", "My Services", "My Projects"]


# Create a Flask Instance
app = Flask(__name__, static_folder='staticFiles')


# Create a route decorator
@app.route('/')
def index():
    return render_template("index.html",
        intro = intro(),
        summary = summary(),
        otg = otg(),
        tic = tic(),
        dtu = dtu(),
        comp = comp,
        edu = edu,
        compLen = compLen,
        skillsLen = len(introLen["skills"]),
        eduLen = eduLen,
        project = project(),
        project_len = len(projectLen["url"]),
        services = services(),
        serviceLen = len(serviceLen["url"]),
        hdrs = hdrs
        )

# USER TEST
# localhost:5000/user/Rene
#@app.route('/user/<name>')

#def user(name):
#    return render_template("user.html",user_name=name)

# Services html route
@app.route('/hw-design')

def hwdesign():
    return render_template("hw-design.html",            
        services = services(),
        serviceLen = len(serviceLen["url"]),
        hdrs = hdrs
        )

@app.route('/sw-design')
def swdesign():
    return render_template("sw-design.html",            
        services = services(),
        serviceLen = len(serviceLen["url"]),
        hdrs = hdrs
        )

@app.route('/management')
def management():
    return render_template("management.html",            
        services = services(),
        serviceLen = len(serviceLen["url"]),
        hdrs = hdrs
        )


@app.route('/mscthesis')
def mscthesis():

    return render_template("mscthesis.html",
        project = project(),
        project_len = len(projectLen["url"]),
        hdrs = hdrs
        )

@app.route('/bscthesis')
def bscthesis():
    return render_template("bscthesis.html",
        project = project(),
        project_len = len(projectLen["url"]),
        hdrs = hdrs
        )

@app.route('/tslvdcdc')
def tslvdcdc():
    return render_template("tslvdcdc.html",
        project = project(),
        project_len = len(projectLen["url"]),
        hdrs = hdrs
        )


@app.route('/ImNoRobot')
def ImNoRobot():
    return render_template("recaptcha.html")

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')