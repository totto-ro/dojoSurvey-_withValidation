from flask import render_template, redirect, request
from survey_app import app
from survey_app.models.Survey import Survey

@app.route( "/", methods=['GET'] )
def getAllUsers():
    users = Survey.add_info()
    return render_template( "index.html", users=users )

# @app.route( '/process', methods=['POST'] )
# def add_info():
#     session['name'] = request.form['name']
#     session['location'] = request.form['location']
#     session['language'] = request.form['language']
#     session['comments'] = request.form['comments']
#     return redirect('/viewInfo')

# @app.route('/viewInfo')
# def sucess():
#     survey = Survey.get_last_survey()
#     return render_template('result.html', survey = survey[0])