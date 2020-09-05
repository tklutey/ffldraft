import csv

import requests

import configurations

URL = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/2020/segments/0/leagues/193035?view=kona_player_info'
cookies = {
    'SWID': '0A7A645D-4090-474B-87F2-5226AAC0281C',
    'espn_s2': 'AEA0bVAcyJ5v3ebA2minDOhJSi2Qt1KAlUnkgf%2B8kIQtcV5kW4%2FCeV8sAzAbxP5EA%2BGV8FgYMgs901PCzbZsnxuwwig%2BiSs%2FzSEUMFF34suJjlX%2F1iZCHOWdX4MTF%2BVN7jitnEebdzz1moeOtd%2Bgp1EKwRevz56PPVUrm%2B9r71%2FXvZkQadRX4SGHkf6FMPhUXKTFy2ZGp7%2BpTuihzI73J1CQK85NDd0ZU8Iof4b0fJA7yo5yU%2Fw%2BdQCqX9JqgMd4090uFL%2Bi0b1BlxHfM%2B11wSSE'
}
positions = {
    1: 'QB',
    2: 'RB',
    3: 'WR',
    4: 'TE',
    5: 'K',
    16: 'D',

}

def get_payload():
    s = requests.Session()
    print("Making request to " + URL)
    r = s.get(URL, cookies=cookies)
    print("Request successful")
    return r.json()

def get_player_total(player):
    stats = player.get('stats')
    a = next(filter(lambda x: x.get('seasonId') == 2020 and x.get('statSourceId') == 1, stats), None).get('appliedTotal')
    print(a)
    return a


def persist(projections):
    players = [(player.get('player')) for player in projections.get('players')]
    player_projections = map(lambda x: (x.get('fullName'), x.get('proTeamId'), positions.get(x.get('defaultPositionId')), get_player_total(x)), players)
    player_projections = sorted(player_projections, key=lambda x : x[-1], reverse=True)

    with open(configurations.ROOT_DIR + '/data/projections.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(['Player', 'Team', 'Position', 'Points'])
        [writer.writerow(player) for player in player_projections]
    writeFile.close()

def main():
    r = get_payload()
    persist(r)

if __name__ == '__main__':
    main()