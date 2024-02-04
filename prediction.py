import json

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import argparse

colors = {
    "green": '\033[92m',
    "red": '\033[91m',
    "reset": '\033[0m'
}

data = pd.read_csv('data.csv')

columns_to_drop = ['name']
data = data.drop(columns=columns_to_drop)

X = data.drop('outcome_last_game', axis=1)
y = data['outcome_last_game']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


def parse_args():
    parser = argparse.ArgumentParser(description='Predict NBA game outcomes.')
    parser.add_argument('--team1', type=str, help='Name or ID of Team 1', required=True)
    parser.add_argument('--team2', type=str, help='Name or ID of Team 2', required=True)
    return parser.parse_args()


def predict_winner(team1, team2):
    input_data = data[(data['id'] == team1) | (data['id'] == team2)].drop('outcome_last_game', axis=1)

    predictions = model.predict(input_data)

    if predictions[0] < predictions[1]:
        return json.dumps({"data": {"winner": str(team1), "loser": str(team2)}})
    elif predictions[0] > predictions[1]:
        return json.dumps({"data": {"winner": str(team2), "loser": str(team1)}})
    else:
        return json.dumps({"data": {"winner": "Tie", "loser": "Tie"}})


def get_teams():
    df = pd.read_csv("data.csv")
    ids = []
    teams = []
    ret = []
    for team in df["name"]:
        teams.append(team)
    for item in df["id"]:
        if str(item).isdigit():
            ids.append(item)
    for i in range(len(teams)):
        ret.append({"name": teams[i], "id": ids[i]})
    return json.dumps({"data": ret})


def main():
    args = parse_args()

    y_pred = model.predict(X_test)

    result = predict_winner(int(args.team1), int(args.team2))
    accuracy = accuracy_score(y_test, y_pred)
    print(colors.get("green") + result[0] + colors.get("reset") + " is predicted to win against " + colors.get("red") +
          result[1] + colors.get("reset"))
    # print(f'Model Accuracy: {accuracy}')


if __name__ == "__main__":
    main()
