
EMPTY_SCOREBOARD = {
  "players": {
    "Joe": {"today": 0, "overall": 0, "game": 0},
    "Sara": {"today": 0, "overall": 0, "game": 0},
    "Aaron": {"today": 0, "overall": 0, "game": 0}, 
    "Kristi": {"today": 0, "overall": 0, "game": 0}, 
    "James": {"today": 0, "overall": 0, "game": 0}, 
    "Faith": {"today": 0, "overall": 0, "game": 0}
  },
  "Hole": 1, 
  "Round": 1, 
  "game": 0
}

def handler(pd: "pipedream"):
  """Receive an email as a webhook with a players wordle score for the day """
  try:
    data_store = pd.inputs["data_store"]
    if "scores" in data_store:
      scores = data_store["scores"]
    else: 
      scores = EMPTY_SCOREBOARD
    from_address = ""
    sender = ""
    summary = ""
    wordle_score = ""
    score_map = {"1/6": -3, "2/6": -2, "3/6": -1, "4/6": 0, "5/6": 1, "6/6": 2}
    player = ""
    if "body" in pd.steps["trigger"]["event"]:
      if "fromAddress" in pd.steps["trigger"]["event"]["body"]:
        from_Address = pd.steps["trigger"]["event"]["body"]["fromAddress"]
      if "sender" in pd.steps["trigger"]["event"]["body"]:
        sender = pd.steps["trigger"]["event"]["body"]["sender"]
      if "summary" in pd.steps["trigger"]["event"]["body"]:
        summary = pd.steps["trigger"]["event"]["body"]["summary"]
        for line in summary.splitlines():
          if line in scores.keys():
            player = line
          if "Wordle" in line:
            wordle_score = line.split(" ")
          if "Round" in line:
            round = line.split(" ")[1]
            scores.update({"Round": round})
          if "Hole" in line:
            hole = line.split(" ")[1]
            scores.update({"Hole": hole})
        scores["players"][player] = {"today": score_map.get(wordle_score[2]), "overall": score_map.get(wordle_score[2]) + scores["players"][player]["overall"], "game": wordle_score[1]}
        scores.update({"game": wordle_score[1]})

    data_store[sender] = {"sender": sender, "summary": summary, "fromAddress": from_address}
    data_store["scores"] = scores
  except Exception as ex:
    print(f"exception caught, {ex}")
    print(pd.steps["trigger"]["event"])
  return {True}

