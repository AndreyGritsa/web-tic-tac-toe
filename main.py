from flask import Flask, render_template, request, session, flash
import os
from game import Game

game = False
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET")


# we need to clean some stuff after win, draw
def clean_ses(obj):
    for key in list(session.keys()):
        if "button" in key or "winner_pos" in key:
            session.pop(key)

    for key in obj.symbols:
        obj.symbols[key] = " "
    obj.is_game = True
    obj.winner_pos = False


def update_score(obj):
    session["x_points"] = obj.x_points
    session["o_points"] = obj.o_points


# logic for each game cell
def button_logic(num, obj):
    if f"game_but{num}" in request.form and f"button{num}" not in session and "side" in session and obj.is_game:
        session[f"button{num}"] = session["side"]
        obj.symbols[num] = session["side"]
        obj.run()
        session[f"button{obj.ai_go}"] = obj.ai_side
        if not obj.is_game and obj.draw:
            update_score(obj)
            session["winner_pos"] = obj.winner_pos
        elif not obj.is_game:
            update_score(obj)
            session["winner_pos"] = obj.winner_pos
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

    if "next" in request.form:
        clean_ses(game)

    if game:
        for button in game.symbols:
            button_logic(button, game)

    print(request.form)
    print(session)
    return render_template("index.html", game=game)


if __name__ == "__main__":
    app.run(debug=True)