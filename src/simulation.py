import csv

import pandas as pd

import configurations
from src.DraftState import DraftState
from src.NflPlayer import NflPlayer
from src.mcst import UCT

nfl_players = pd.read_csv(configurations.ROOT_DIR + '/data/projections.csv', index_col=0)

freeagents = [NflPlayer(*p) for p in nfl_players.itertuples(index=True, name=None)]

num_competitors = 8
rosters = [[] for _ in range(num_competitors)]  # empty rosters to start with

num_rounds = 16
turns = []
# generate turns by snake order
for i in range(num_rounds):
    turns += reversed(range(num_competitors)) if i % 2 else range(num_competitors)

state = DraftState(rosters, turns, freeagents)
iterations = 1000
while state.GetMoves() != []:
    move = UCT(state, iterations)
    print(move, end=".")
    state.DoMove(move)
    print(state.rosters)
    print("Round: " + str(len(rosters[0])))

with open(configurations.ROOT_DIR + '/data/rosters.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    team = 1
    for roster in state.rosters:
        roster.insert(0, team)
        writer.writerow(roster)
        team += 1