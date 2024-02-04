from flask import Flask, request
import json
from prediction import predict_winner, get_teams


app = Flask(__name__)
# cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/getprediction')
def prediction():
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")

    return predict_winner(int(team1), int(team2))

@app.route('/getteams')
def teams():

    return get_teams()


if __name__ == "__main__":
    app.run(debug=True)
