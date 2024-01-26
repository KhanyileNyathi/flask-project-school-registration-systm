from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase




app = Flask(__name__)

@app.route("/") 
def index():
    return render_template('index.html')

@app.route("/submit",methods=['POST']) 
def submit():
    username=request.form.get('name',False)
    Address=request.form.get("Address",False)
    contact_details=request.form.get("contact_details")
    EmailAddress=request.form.get('EmailAddress')
    Occupation=request.form.get('Occupation')
    name=request.form.get('name')
    id_number=request.form.get('id_number')
    Contact_details=request.form.get('Contact_details')
    Grade=request.form.get('Grade')  
    if name == '' or id_number == '' or EmailAddress=='' or Address=='' or username=='' or contact_details== '' or Contact_details=='' or  Grade=='':
        return render_template('index.html',message='Please fill in the required spaces')   
    return render_template('success.html')
      
     
if __name__=='__main__':
    app.debug=True
    app.run()