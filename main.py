from flask import Flask, render_template, request, session, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField

from game import Game

app = Flask(__name__)
app.secret_key = "asdaqwe123asd1239ua0s8hdub298baosubd 19280"


@app.route("/", methods=["GET", "POST"])
def index():
    # symbols = {
    #         11: " ",
    #         12: " ",
    #         13: " ",
    #         21: " ",
    #         22: " ",
    #         23: " ",
    #         31: " ",
    #         32: " ",
    #         33: " ",
    #     }

    if "radio" in request.form and "side" not in session:
        session["side"] = request.form["radio"]
        game = Game(session["side"])


    if "restart" in request.form:
        for key in list(session.keys()):
            session.pop(key)

    if "game_but11" in request.form and "button11" not in session and "side" in session:
        session["button11"] = session["side"]
    elif "game_but11" in request.form and "button11" not in session and "side" not in session:
        flash("You haven't chosen the side.")

    if "game_but12" in request.form and "button12" not in session and "side" in session:
        session["button12"] = session["side"]
    elif "game_but12" in request.form and "button12" not in session and "side" not in session:
        flash("You haven't chosen the side.")



    print(request.form)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)