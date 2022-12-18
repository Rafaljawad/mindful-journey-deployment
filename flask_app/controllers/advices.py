
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, activity,advice
from flask_app.models.user import User

#CREATE ADVICE CONTROLLER
@app.route("/add/advice",methods=['POST','GET'])
def add_advice():
    if request.method=='GET':
            if 'user_id' in session:
                return render_template("add_advice.html")
            else:
                return redirect('/')
    else:
        advice.Advice.create_advice(request.form)
        return redirect('/users/dashboard')


#READ ALL ADVICE CONTROLLER
# @app.route('/users/dashboard')
# def show_all_user_advices():
#     all_advice=advice.Advice.get_all_advices()
#     return render_template('show_advice.html',all_advice=all_advice)

