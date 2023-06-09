import requests
import json

class FootBallLiveStatistics(object):


    def nami_resquest(self):
        proxy = {
            "https": f"http://47.96.71.126:59073",
            "http": f"http://47.96.71.126:59073"
        }
        nami_url = 'https://open.sportnanoapi.com/api/v4/football/match/player_stats/list?user=hali&secret=ce210a5881206c1a6ed77760091aec36'
        res = requests.get(url=nami_url, proxies=proxy, timeout=20)
        res_ = res.json()
        results = res_.get('results')
        player_stats = results[0]['player_stats']
        return player_stats


if __name__ == '__main__':
    re = FootBallLiveStatistics()
    re.nami_resquest()