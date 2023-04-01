from flask import Flask, render_template, request, session, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField

from game import Game

app = Flask(__name__)
app.secret_key = "asdaqwe123asd1239ua0s8hdub298baosubd 19280"


def clean_ses():
    for key in list(session.keys()):
        if "button" in key:
            session.pop(key)

def update_score():



@app.route("/", methods=["GET", "POST"])
def index():

    if "radio" in request.form and "side" not in session:
        global game
        session["side"] = request.form["radio"]
        game = Game(session["side"], request.form["dific"])
        session["x_points"] = game.x_points
        session["o_points"] = game.o_points

    if "restart" in request.form:
        for key in list(session.keys()):
            session.pop(key)
    # buton 1
    if "game_but11" in request.form and "button11" not in session and "side" in session:
        session["button11"] = session["side"]
        game.symbols[11] = session["side"]
        game.run()
        if not game.is_game and game.draw:
            return "DRAW"
        elif not game.is_game:
            return f"Here's is our winner, congratulations to {game.winner}"
        else:
            session[f"button{game.ai_go}"] = game.ai_side
    elif "game_but11" in request.form and "button11" not in session and "side" not in session:
        flash("You haven't chosen the side.")

    # buton 2
    if "game_but12" in request.form and "button12" not in session and "side" in session:
        session["button12"] = session["side"]
        game.symbols[12] = session["side"]
        game.run()
        if not game.is_game and game.draw:
            return "DRAW"
        elif not game.is_game:
            return f"Here's is our winner, congratulations to {game.winner}"
        else:
            session[f"button{game.ai_go}"] = game.ai_side
    elif "game_but12" in request.form and "button12" not in session and "side" not in session:
        flash("You haven't chosen the side.")

    # buton 3
    if "game_but13" in request.form and "button13" not in session and "side" in session:
        session["button13"] = session["side"]
        game.symbols[13] = session["side"]
        game.run()
        if not game.is_game and game.draw:
            return "DRAW"
        elif not game.is_game:
            return f"Here's is our winner, congratulations to {game.winner}"
        else:
            session[f"button{game.ai_go}"] = game.ai_side
    elif "game_but13" in request.form and "button13" not in session and "side" not in session:
        flash("You haven't chosen the side.")

    # buton 4
    if "game_but21" in request.form and "button21" not in session and "side" in session:
        session["button21"] = session["side"]
        game.symbols[21] = session["side"]
        game.run()
        if not game.is_game and game.draw:
            return "DRAW"
        elif not game.is_game:
            return f"Here's is our winner, congratulations to {game.winner}"
        else:
            session[f"button{game.ai_go}"] = game.ai_side
    elif "game_but21" in request.form and "button21" not in session and "side" not in session:
        flash("You haven't chosen the side.")

    # buton 5
    if "game_but22" in request.form and "button22" not in session and "side" in session:
        session["button22"] = session["side"]
        game.symbols[22] = session["side"]
        game.run()
        if not game.is_game and game.draw:
            return "DRAW"
        elif not game.is_game:
            return f"Here's is our winner, congratulations to {game.winner}"
        else:
            session[f"button{game.ai_go}"] = game.ai_side
    elif "game_but22" in request.form and "button22" not in session and "side" not in session:
        flash("You haven't chosen the side.")

    # buton 6
    if "game_but23" in request.form and "button23" not in session and "side" in session:
        session["button23"] = session["side"]
        game.symbols[23] = session["side"]
        game.run()
        if not game.is_game and game.draw:
            return "DRAW"
        elif not game.is_game:
            return f"Here's is our winner, congratulations to {game.winner}"
        else:
            session[f"button{game.ai_go}"] = game.ai_side
    elif "game_but23" in request.form and "button23" not in session and "side" not in session:
        flash("You haven't chosen the side.")

    # buton 7
    if "game_but31" in request.form and "button31" not in session and "side" in session:
        session["button31"] = session["side"]
        game.symbols[31] = session["side"]
        game.run()
        if not game.is_game and game.draw:
            return "DRAW"
        elif not game.is_game:
            return f"Here's is our winner, congratulations to {game.winner}"
        else:
            session[f"button{game.ai_go}"] = game.ai_side
    elif "game_but31" in request.form and "button31" not in session and "side" not in session:
        flash("You haven't chosen the side.")

    # buton 8
    if "game_but32" in request.form and "button32" not in session and "side" in session:
        session["button32"] = session["side"]
        game.symbols[32] = session["side"]
        game.run()
        if not game.is_game and game.draw:
            return "DRAW"
        elif not game.is_game:
            return f"Here's is our winner, congratulations to {game.winner}"
        else:
            session[f"button{game.ai_go}"] = game.ai_side
    elif "game_but32" in request.form and "button32" not in session and "side" not in session:
        flash("You haven't chosen the side.")

    # buton 9
    if "game_but33" in request.form and "button33" not in session and "side" in session:
        session["button33"] = session["side"]
        game.symbols[33] = session["side"]
        game.run()
        if not game.is_game and game.draw:
            return "DRAW"
        elif not game.is_game:
            return f"Here's is our winner, congratulations to {game.winner}"
        else:
            session[f"button{game.ai_go}"] = game.ai_side
    elif "game_but33" in request.form and "button33" not in session and "side" not in session:
        flash("You haven't chosen the side.")

    print(request.form)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)