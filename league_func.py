import requests;

def getMatchHistory(region, me):
    pastMatchesURL = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{me.puuid}/ids?start=0&count=20&{me.apiKey}"
    print(pastMatchesURL)
    pastMatches = requests.get(pastMatchesURL).json()
    print(pastMatches)
    return pastMatches


class Profile:
    def __init__(self, apiKey, userName):
        self.apiKey = f"api_key= {apiKey}"
        self.name = userName
        apiUrl = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{userName}?{self.apiKey}"
        res = requests.get(apiUrl).json()
        self.id = res["id"]
        self.accountId = res["accountId"]
        self.puuid = res["puuid"]
def getInputOutput():
    apiKey = input("what is your api key? \n")
    userName = input("what is your username? \n")

    me = Profile(apiKey, userName)

    history = getMatchHistory("americas", me)
    print(history)
