from flask import render_template, redirect, request
from survey_app import app
from survey_app.models.Survey import Survey

@app.route('/', methods=['GET'])         
def index():
    return render_template("index.html")

@app.route( '/create/survey', methods=['POST'] )
def add_info():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']

    if Survey.is_valid( name, location, language, comments ):
        Survey.add_info( request.form )
        return redirect ( '/result' )
    else:
        print( "Something went wrong" )
        return redirect ( '/' )

@app.route( '/result' )
def results():
    survey = Survey.get_last_survey()
    return render_template( 'result.html', survey = survey[0] )



# @app.route( '/create/survey', methods=['POST'] )
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