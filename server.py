from flask import Flask, render_template, request, redirect, session

app = Flask( __name__ )
app.secret_key = "veryMuchSecret"

if __name__ == "__main__":
    app.run( debug = True )