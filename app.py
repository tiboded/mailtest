from flask import Flask,request
from flask_mail import Mail,Message

app=Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    MAIL_SERVER='smtp.office365.com',
    MAIL_PORT=587,
    MAIL_USERNAME='tiboded@hotmail.fr',
    MAIL_PASSWORD='',
    MAIL_USE_SSL=False,
    MAIL_USE_TLS=True,
    ))

mail=Mail(app)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return '<form method="POST"><input type="text" name="email"></form>'
    msg=Message('Hello',sender='tiboded@hotmail.fr',recipients=[request.form['email']])
    mail.send(msg)
    return 'Email sent'

if __name__=='__main__':
    app.run(debug=True)
