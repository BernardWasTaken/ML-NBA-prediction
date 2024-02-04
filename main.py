from time import sleep

from teams import Teams
import pandas
import json



headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "5acc17a71fb2b36eaf7c3c3729425627"
}

team = Teams(headers)

items = team.get_teams(season="2023-2024")

with open("teams.txt", "w") as f:
    f.write(json.dumps(items, indent=4, sort_keys=True))

print(items)

# teams
ids = []
names = []

# statistics
winrate = []
avg_points_home = []
avg_points_away = []
avg_points_allowed_home = []
avg_points_allowed_away = []
winrate_home = []
winrate_away = []

# standings
current_standing = []

# games
outcome_last_game = []
point_diff_last_game = []
opponent_last_game = []
outcome_second_last_game = []
point_diff_second_last_game = []
opponent_second_last_game = []


for i in range(len(items['response'])):
    # Teams
    if items['response'][i]['id'] < 132 or items['response'][i]['id'] > 161:
        continue
    ids.append(str(items['response'][i]['id']))
    names.append(str(items['response'][i]['name']))

for id_s in ids:

    # API calls
    response = team.get_team_statistics(league_id=12, season="2023-2024", team_id=id_s)
    response_standing = team.get_team_standing(league_id=12, season="2023-2024", team_id=id_s)
    response_games = team.get_team_games(league_id=12, season="2023-2024", team_id=id_s)

    # Statistics
    try:
        winrate.append(str(response['response']['games']['wins']['all']['percentage']))
    except TypeError as e:
        print(f"error with winrate at id={id_s}")
        winrate.append("null")
    try:
        winrate_home.append(str(response['response']['games']['wins']['home']['percentage']))
    except TypeError as e:
        print(f"error with winrate_home at id={id_s}")
        winrate_home.append("null")
    try:
        winrate_away.append(str(response['response']['games']['wins']['away']['percentage']))
    except TypeError as e:
        print(f"error with winrate_away at id={id_s}")
        winrate_away.append("null")
    try:
        avg_points_home.append(str(response['response']['points']['for']['average']['home']))
    except TypeError as e:
        print(f"error with avg_points_home at id={id_s}")
        avg_points_home.append("null")
    try:
        avg_points_away.append(str(response['response']['points']['for']['average']['away']))
    except TypeError as e:
        print(f"error with avg_points_away at id={id_s}")
        avg_points_away.append("null")
    try:
        avg_points_allowed_home.append(str(response['response']['points']['against']['average']['home']))
    except TypeError as e:
        print(f"error with avg_points_allowed_home at id={id_s}")
        avg_points_allowed_home.append("null")
    try:
        avg_points_allowed_away.append(str(response['response']['points']['against']['average']['away']))
    except TypeError as e:
        print(f"error with avg_points_allowed_away at id={id_s}")
        avg_points_allowed_away.append("null")

    # Standings
    try:
        current_standing.append(str(response_standing['response'][0][0]['position']))
    except:
        print(f"error with current_standing at id={id_s}")
        current_standing.append("null")

    # Games
    counter = 0
    for i in range(int(response_games['results']) - 1, 0, -1):
        if counter == 2:
            break

        if str(response_games['response'][i]['status']['short']) != "FT":
            continue

        if counter == 0:
            if str(response_games['response'][i]['teams']['home']['id']) == str(id_s):
                if int(response_games['response'][i]['scores']['home']['total']) > int(response_games['response'][i]['scores']['away']['total']):
                    outcome_last_game.append("Win")
                    point_diff_last_game.append(str(int(response_games['response'][i]['scores']['home']['total']) - int(response_games['response'][i]['scores']['away']['total'])))
                elif int(response_games['response'][i]['scores']['home']['total']) < int(response_games['response'][i]['scores']['away']['total']):
                    outcome_last_game.append("Loss")
                    point_diff_last_game.append(str(int(response_games['response'][i]['scores']['away']['total']) - int(response_games['response'][i]['scores']['home']['total'])))
                else:
                    outcome_last_game.append("Tie")
                    point_diff_last_game.append("0")
                opponent_last_game.append(str(response_games['response'][i]['teams']['away']['id']))
            else:
                if int(response_games['response'][i]['scores']['home']['total']) < int(response_games['response'][i]['scores']['away']['total']):
                    outcome_last_game.append("Win")
                    point_diff_last_game.append(str(int(response_games['response'][i]['scores']['away']['total']) - int(response_games['response'][i]['scores']['home']['total'])))
                elif int(response_games['response'][i]['scores']['home']['total']) > int(response_games['response'][i]['scores']['away']['total']):
                    outcome_last_game.append("Loss")
                    point_diff_last_game.append(str(int(response_games['response'][i]['scores']['home']['total']) - int(response_games['response'][i]['scores']['away']['total'])))
                else:
                    outcome_last_game.append("Tie")
                    point_diff_last_game.append("0")
                opponent_last_game.append(str(response_games['response'][i]['teams']['home']['id']))
            counter += 1

        if counter == 1:
            if str(response_games['response'][i]['teams']['home']['id']) == str(id_s):
                if int(response_games['response'][i]['scores']['home']['total']) > int(response_games['response'][i]['scores']['away']['total']):
                    outcome_second_last_game.append("Win")
                    point_diff_second_last_game.append(str(int(response_games['response'][i]['scores']['home']['total']) - int(response_games['response'][i]['scores']['away']['total'])))
                elif int(response_games['response'][i]['scores']['home']['total']) < int(response_games['response'][i]['scores']['away']['total']):
                    outcome_second_last_game.append("Loss")
                    point_diff_second_last_game.append(str(int(response_games['response'][i]['scores']['away']['total']) - int(response_games['response'][i]['scores']['home']['total'])))
                else:
                    outcome_second_last_game.append("Tie")
                    point_diff_second_last_game.append("0")
                opponent_second_last_game.append(str(response_games['response'][i]['teams']['away']['id']))
            else:
                if int(response_games['response'][i]['scores']['home']['total']) < int(response_games['response'][i]['scores']['away']['total']):
                    outcome_second_last_game.append("Win")
                    point_diff_second_last_game.append(str(int(response_games['response'][i]['scores']['away']['total']) - int(response_games['response'][i]['scores']['home']['total'])))
                elif int(response_games['response'][i]['scores']['home']['total']) > int(response_games['response'][i]['scores']['away']['total']):
                    outcome_second_last_game.append("Loss")
                    point_diff_second_last_game.append(str(int(response_games['response'][i]['scores']['home']['total']) - int(response_games['response'][i]['scores']['away']['total'])))
                else:
                    outcome_second_last_game.append("Tie")
                    point_diff_second_last_game.append("0")
                opponent_second_last_game.append(str(response_games['response'][i]['teams']['home']['id']))
            counter += 1

    print(f"--------------------id={id_s}--------------------")
    print(f"ids: {ids}; length={len(ids)}")
    print(f"names: {names}; length={len(names)}")
    print(f"winrate: {winrate}; length={len(winrate)}")
    print(f"winrate_home: {winrate_home}; length={len(winrate_home)}")
    print(f"winrate_away: {winrate_away}; length={len(winrate_away)}")
    print(f"avg_points_home: {avg_points_home}; length={len(avg_points_home)}")
    print(f"avg_points_away: {avg_points_away}; length={len(avg_points_away)}")
    print(f"avg_points_allowed_home: {avg_points_allowed_home}; length={len(avg_points_allowed_home)}")
    print(f"avg_points_allowed_away: {avg_points_allowed_away}; length={len(avg_points_allowed_away)}")
    print(f"outcome_last_game: {outcome_last_game}; length={len(outcome_last_game)}")
    print(f"point_diff_last_game: {point_diff_last_game}; length={len(point_diff_last_game)}")
    print(f"opponent_last_game: {opponent_last_game}; length={len(opponent_last_game)}")
    print(f"outcome_second_last_game: {outcome_second_last_game}; length={len(outcome_second_last_game)}")
    print(f"point_diff_second_last_game: {point_diff_second_last_game}; length={len(point_diff_second_last_game)}")
    print(f"opponent_second_last_game: {opponent_second_last_game}; length={len(opponent_second_last_game)}")
    print("\n\n\n")
    sleep(60)


data = {
    "id": ids,
    "name": names,
    "winrate": winrate,
    "winrate_home": winrate_home,
    "winrate_away": winrate_away,
    "avg_points_home": avg_points_home,
    "avg_points_away": avg_points_away,
    "avg_points_allowed_home": avg_points_allowed_home,
    "avg_points_allowed_away": avg_points_allowed_away,
    "outcome_last_game": outcome_last_game,
    "point_diff_last_game": point_diff_last_game,
    "opponent_last_game": opponent_last_game,
    "outcome_second_last_game": outcome_second_last_game,
    "point_diff_second_last_game": point_diff_second_last_game,
    "opponent_second_last_game": opponent_second_last_game
}

df = pandas.DataFrame(data)

df.to_csv("data.csv", index=False)
