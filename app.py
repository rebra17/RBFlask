from flask import Flask, render_template, request, abort
from scripts.forms import ContactForm
from flask_mail import Mail, Message
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

import os
import requests

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

app.secret_key = os.getenv("DOMAIN_SECRET_KEY")

# USE ENV VARIABLES BEFORE GOING PUBLIC
mail = Mail()
app.config["MAIL_SERVER"] = os.getenv("SMTP")
app.config["MAIL_PORT"] = os.getenv("PORT")
app.config["MAIL_USERNAME"] = os.getenv("CONTACT_EMAIL")
app.config["MAIL_PASSWORD"] = os.getenv("CONTACT_PASS")
app.config["MAIL_RECIPENT"] = os.getenv("MAIL_RECIPENT")
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
    return render_template("hw-design.html",            
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

      return render_template('contact.html', 
                             form=form,
                             SITE_KEY=os.getenv("SITE_KEY"),
                             API_KEY=os.getenv("API_KEY")
                             )
    
    if form.validate_on_submit():
        secret_response = request.form['g-recaptcha-response']

        verify_response = requests.post(
            url=f'{os.getenv("VERIFY_URL")}?secret={os.getenv("SECRET_KEY")}&response={secret_response}').json()

        # Check Google response. If success == False or score < 0.5, most likely a robot -> abort
        if not verify_response['success'] or verify_response['score'] < 0.5:
            # print('abort')
            abort(401)

        today = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # Send email notification
        html = f"New form submission received!<br>" \
               f"<br>" \
               f"Date : {today}<br>" \
               f"Name : {name}<br>" \
               f"Email : {email}<br>" \
               f"Message : {message}<br><br>"
        
        msg = Message(
            subject='New Contact Form Received',
            html=html,
            sender=(app.config['MAIL_USERNAME']),
            # pass recipients as a list (best to use env variables to not disclose email addresses here)
            recipients=[app.config["MAIL_RECIPENT"]]
        )

        mail.send(msg)

        return render_template('contact.html',success=True
                             )
    
  elif request.method == 'GET':

    return render_template('contact.html', 
                            form=form,
                            SITE_KEY=os.getenv("SITE_KEY"),
                            API_KEY=os.getenv("API_KEY")
                           )

if __name__ == '__main__':
    app.run(debug=False)