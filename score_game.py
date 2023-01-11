
def score_game(pd: "pipedream"):
    """Generate text of wordle golf score and push to email"""
    data_store = pd.inputs["data_store"]
    if "scores" not in data_store:
        print("No Scores")
        return
    scores = data_store["scores"]
    score_message = f"""Scoreboard
         Today  Overall
    """
    for player in scores["players"]:
        score_message += f"{player}: "
        score_message += " " * (5 - len(player)) # make all the spaces equal, longest name 5 letters
        score_message += f"{scores['players'][player]['today']} "