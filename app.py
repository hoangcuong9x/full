from flask import Flask, request, render_template, session, redirect, url_for, json, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/signup")
def signup():
    return render_template('signup.html')
@app.route("/experts")
def experts():
    return render_template('ex.html')
if __name__ ==  "__main__":
    app.run(debug=True)