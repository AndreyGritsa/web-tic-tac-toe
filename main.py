from flask import Flask, render_template, request, session, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField

from game import Game

game = False
lastgame = False
app = Flask(__name__)
app.secret_key = "asdaqwe123asd1239ua0s8hdub298baosubd 19280"


def clean_ses(obj):
    for key in list(session.keys()):
        if "button" in key:
            session.pop(key)

    obj.symbols_last_game = obj.symbols
    session["lastgame"] = obj.symbols_last_game
    for key in obj.symbols:
        print(obj.symbols_last_game[key])
        obj.symbols[key] = " "
    obj.is_game = True


def update_score(obj):
    session["x_points"] = obj.x_points
    session["o_points"] = obj.o_points


def button_logic(num, obj):
    if f"game_but{num}" in request.form and f"button{num}" not in session and "side" in session:
        session[f"button{num}"] = session["side"]
        obj.symbols[num] = session["side"]
        obj.run()
        if not obj.is_game and obj.draw:
            update_score(obj)
            clean_ses(obj)
            # session["lastgame"] = obj.symbols_last_game
            print(f"session lastgame: {session['lastgame']}")

        elif not obj.is_game:
            update_score(obj)
            clean_ses(obj)
            # session["lastgame"] = obj.symbols_last_game
            print(f"session lastgame: {session['lastgame']}")
        else:
            session[f"button{obj.ai_go}"] = obj.ai_side
    elif f"game_but{num}" in request.form and f"button{num}" not in session and "side" not in session:
        flash("You haven't chosen the side.")


@app.route("/", methods=["GET", "POST"])
def index():
    global game, lastgame
    if "radio" in request.form and "side" not in session:
        session["side"] = request.form["radio"]
        game = Game(session["side"], request.form["dific"])
        update_score(game)

    if "restart" in request.form:
        for key in list(session.keys()):
            session.pop(key)

    if game:

        # buton 1
        lastgame = button_logic(11, game)

        # buton 2
        lastgame = button_logic(12, game)


        # buton 3
        lastgame = button_logic(13, game)


        # buton 4
        lastgame = button_logic(21, game)


        # buton 5
        lastgame = button_logic(22, game)


        # buton 6
        lastgame = button_logic(23, game)


        # buton 7
        lastgame = button_logic(31, game)


        # buton 8
        lastgame = button_logic(32, game)


        # buton 9
        lastgame = button_logic(33, game)
    print(request.form)
    print(session)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)