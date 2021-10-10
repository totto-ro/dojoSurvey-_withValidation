from flask import Flask
from survey_app import app
from survey_app.controllers import surveys_controller


if __name__ == "__main__":
    app.run( debug = True )