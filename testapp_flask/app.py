from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html", title="Home")

# Example route with parameters
@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name, title="Greeting")

# Form submission route (GET and POST)
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        data = request.form.get("data")
        return render_template("submit.html", data=data, title="Form Submitted")
    return render_template("submit.html", title="Submit Form")

# API route returning JSON
@app.route("/api/data")
def api_data():
    sample_data = {"message": "Hello, this is sample data!", "status": "success"}
    return jsonify(sample_data)

# 404 Error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title="Page Not Found"), 404

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
