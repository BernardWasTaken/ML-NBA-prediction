import requests
import json


class Teams:
    headers = {}
    base_url = "https://v1.basketball.api-sports.io"

    def __init__(self, headers):
        self.headers = headers

    def get_teams(self, season):
        response = requests.get(url=self.base_url + f"/teams?season={str(season)}&league=12", headers=self.headers)
        return response.json()

    def get_team_statistics(self, league_id, season, team_id):
        response = requests.get(
            url=self.base_url + f"/statistics?season={str(season)}&league={str(league_id)}&team={str(team_id)}",
            headers=self.headers)
        return response.json()

    def get_team_standing(self, league_id, season, team_id):
        response = requests.get(
            url=self.base_url + f"/standings?season={str(season)}&league={str(league_id)}&team={str(team_id)}",
            headers=self.headers)
        return response.json()

    def get_team_games(self, league_id, season, team_id):
        response = requests.get(
            url=self.base_url + f"/games?season={str(season)}&league={str(league_id)}&team={str(team_id)}",
            headers=self.headers)
        return response.json()

    def get_h2h(self, team_one, team_two, season=None):
        if season is None:
            response = requests.get(
                url=self.base_url + f"/games?h2h={team_one}-{team_two}",
                headers=self.headers)
        else:
            response = requests.get(
                url=self.base_url + f"/games?h2h={team_one}-{team_two}&season={season}",
                headers=self.headers)
        return json.dumps(response.json(), indent=4, sort_keys=True)
