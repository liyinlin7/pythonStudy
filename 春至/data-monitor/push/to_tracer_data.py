import json


def to_data(tracer_id, data):
    print(data)
    msg = {
        "tracer_id": tracer_id,
        "data": json.dumps(data, ensure_ascii=False)
    }
    print(json.dumps(msg, ensure_ascii=False))


if __name__ == '__main__':
    tracer_id = "series1"
    data = """
    {"id": "311097", "game_id": 4, "source": 7, "create_time": 1637060941, "league_id": "6576", "status": 2, "start_time": 1637053500, "end_time": 1637060933, "bo": 5, "win_team": "85497", "has_odds": 1, "has_inplay": 1, "has_live_data": 2, "has_result": 2, "teams": [{"team": {"id": "85497", "game_id": 4, "source": 7, "create_time": 1637060941, "name_full": "Joy Xman Gaming", "name_abbr": "JXG", "pic": "https://img.abiosgaming.com/competitors/JXG-2021-teamlogo.png", "country": "中国", "area": "亚洲"}, "score": 1, "index": 1}, {"team": {"id": "85498", "game_id": 4, "source": 7, "create_time": 1637060941, "name_full": "Nan Bo Wan", "name_abbr": "NBW", "pic": "https://img.abiosgaming.com/competitors/NBW-2021-teamlogo.png", "country": "中国", "area": "亚洲"}, "score": 1, "index": 2}]}
    """
    data = json.loads(data)
    to_data(tracer_id, data)