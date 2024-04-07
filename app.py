from flask import Flask, render_template, request, flash, redirect, url_for, abort
from scripts.forms import ContactForm
from flask_mail import Mail, Message
from datetime import datetime

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

app.secret_key = 'GVGCy8Fxl*l4F}9y,}3mX^eUdLZqow19024'

# LocalHost
# SITE_KEY = '6LftP7MpAAAAAIEfc6JVe1FTrZOwp_Bt6HIbQtfF'
# SECRET_KEY_re = '6LftP7MpAAAAAAzv5vF5f1geu4X59YdayFRUQxz5'

# Public
SITE_KEY = '6LdxbbMpAAAAAEJv9Dp2WEple8FoSTSLsHoOg0dD'
SECRET_KEY = '6LdxbbMpAAAAANZMCT613Ni8QrE_IDVceg3oB9n_'

VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'

# USE ENV VARIABLES BEFORE GOING PUBLIC
mail = Mail()
app.config["MAIL_SERVER"] = 'smtp.ionos.co.uk'
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = 'contact@brandbyge.com'
app.config["MAIL_PASSWORD"] = 'ujF6)bvAw]5K}W7B2v8'
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSP"] = False

# app.config["MAIL_SERVER"] = 'localhost'
# app.config["MAIL_PORT"] = 25
# app.config["MAIL_USERNAME"] = 'contact@brandbyge.com'
# app.config["MAIL_PASSWORD"] = 'ujF6)bvAw]5K}W7B2v8'
# app.config["MAIL_USE_TLS"] = False
# app.config["MAIL_USE_SSP"] = False

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
#   print(form.submit)


  if request.method == 'POST':
    print('request made')
    # print(request.form['g-recaptcha-response'])
    

    if form.validate() == False:
      
    #   flash('All fields are required.')

      return render_template('contact.html', 
                             form=form, 
                             SITE_KEY=SITE_KEY
                             )
    
    if form.validate_on_submit():
        secret_response = request.form['g-recaptcha-response']
        # print(secret_response)
        verify_response = requests.post(
            url=f'{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}').json()
        # print(verify_response)
        # Check Google response. If success == False or score < 0.5, most likely a robot -> abort
        if not verify_response['success'] or verify_response['score'] < 0.5:
            # print('abort')
            abort(401)

    # else:        
    #     secret_response = request.form['g-recaptcha-response']
    #     # name = form.name.data
    #     # email = form.email.data
    #     # message = form.message.data
    #     # return name, message
    #     verify_response = requests.post(url=f'{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}').json()

    #     if not verify_response['success'] or verify_response['score'] < 0.5:
    #        abort(401)
            # if success and score ok -> send email notification for new form submission
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
            sender=('contact@brandbyge.com', app.config['MAIL_USERNAME']),
            # pass recipients as a list (best to use env variables to not disclose email addresses here)
            recipients=['rene.bloch@brandbyge.com']
        )
        
#         msg = Message(form.subject.data, sender='contact@brandbyge.com', recipients=['rene.bloch@brandbyge.com'])
#         msg.body = """From
# %s\n
# Email
# %s\n
# Message
# %s 
#             """ % (form.name.data, form.email.data, form.message.data)
        # print('msg made')
        mail.send(msg)
        # print('email send')
        # print('email sent!')
        return render_template('contact.html',success=True
                             )
    
  elif request.method == 'GET':

    return render_template('contact.html', 
                           form=form,
                           SITE_KEY=SITE_KEY
                           )

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')