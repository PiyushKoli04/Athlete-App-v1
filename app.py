from flask import Flask, render_template

app = Flask(__name__)

#@app.route("/")
#def landing():
#   return render_template("index.html")

@app.route("/")
def landing():
    return "Hello, World!  This is the landing page to let everyone know that the pratham is gay."

if __name__ == "__main__":
    app.run(debug=True)


