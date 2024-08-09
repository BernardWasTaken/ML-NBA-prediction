from teams import Teams
import json
import pandas

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "api_key"
}

team = Teams(headers)

response_games = team.get_team_statistics(season="2023-2024", league_id=12, team_id=132)

print(str(response_games['response']['games']['wins']['all']['percentage']))



