import pandas as pd

import configurations
from src.DraftState import DraftState
from src.NflPlayer import NflPlayer
from src.mcst import UCT

def main():

    state = get_state()
    log_round(state.rosters)
    iterations = 1000
    while state.GetMoves() != []:
        move = UCT(state, iterations)
        print(move, end=".")
        player = state.DoMove(move, is_test=True)
        log_pick(player)
        log_round(state.rosters)

def log_round(rosters):
    print ("Round: " + str(max(len(i) for i in rosters)))

def log_pick(player):
    print("==========")
    print("You should pick:")
    print(player)
    print("==========")


def get_state():
    nfl_players = pd.read_csv(configurations.ROOT_DIR + '/data/projections.csv', index_col=0)

    freeagents = [NflPlayer(*p) for p in nfl_players.itertuples(index=True, name=None)]

    state = pd.read_csv(configurations.ROOT_DIR + '/data/draft.csv', index_col=0, header=None)

    num_competitors = 8

    num_rounds = 16
    turns = []
    # generate turns by snake order
    for i in range(num_rounds):
        turns += reversed(range(num_competitors)) if i % 2 else range(num_competitors)

    rosters = []
    for row in range(num_competitors):

        roster = []
        for i in state.iloc[row].dropna().tolist():
            q = None
            q = next((x for x in freeagents if i == x.name), None)
            if i is not None and q is None:
                raise Exception("Possible misspelling! You entered {} but we found no match.".format(i))
            if q is not None:
                freeagents.remove(q)
                roster.append(q)
                turns.pop(0)

        print(roster)

        rosters.append(roster)

    print(rosters)
    state = DraftState(rosters, turns, freeagents)
    return state

if __name__ == '__main__':
    main()
