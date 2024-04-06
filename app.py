from flask import Flask, render_template, request, flash, render_template, redirect, url_for
from scripts.forms import ContactForm
from flask_mail import Mail, Message


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

app.secret_key = 'GVGCy8Fxl*l4F}9y,}3mX^eUdLZqow19024'

mail = Mail()
app.config["MAIL_SERVER"] = 'smtp.ionos.co.uk'
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = 'contact@brandbyge.com'
app.config["MAIL_PASSWORD"] = 'ujF6)bvAw]5K}W7B2v8'
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSP"] = False

mail.init_app(app)


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


# Services html route
@app.route('/hw-design')

def hwdesign():
    return render_template("WIP.html",            
        services = services(),
        serviceLen = len(serviceLen["url"]),
        hdrs = hdrs
        )

@app.route('/sw-design')
def swdesign():
    return render_template("WIP.html",            
        services = services(),
        serviceLen = len(serviceLen["url"]),
        hdrs = hdrs
        )

@app.route('/management')
def management():
    return render_template("WIP.html",            
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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  success=False
  form = ContactForm()
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    
    else:
        # name = form.name.data
        # email = form.email.data
        # message = form.message.data
        # return name, message
        msg = Message(form.subject.data, sender='contact@brandbyge.com', recipients=['rene.bloch@brandbyge.com'])
        msg.body = """From
%s\n
Email
%s\n
Message
%s 
            """ % (form.name.data, form.email.data, form.message.data)
        # print('msg made')
        mail.send(msg)
        # print('email send')
        return render_template('contact.html',success=True)
    
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')