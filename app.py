from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Rajiv Siddiqui's  Udacity Final project Blue Deployment Version 1"
app.run(host="0.0.0.0", port=8080, debug=True)
