from teams import Teams
import json
import pandas

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "5acc17a71fb2b36eaf7c3c3729425627"
}

team = Teams(headers)

response_games = team.get_team_statistics(season="2023-2024", league_id=12, team_id=132)

print(str(response_games['response']['games']['wins']['all']['percentage']))



