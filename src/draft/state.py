# import pandas as pd
#
# import configurations
# from src.DraftState import DraftState
#
#
# def get_state(freeagents):
#     num_competitors = 2
#
#     num_rounds = 16
#     turns = []
#     # generate turns by snake order
#     for i in range(num_rounds):
#         turns += reversed(range(num_competitors)) if i % 2 else range(num_competitors)
#     state = pd.read_csv(configurations.ROOT_DIR + '/data/draft.csv', index_col=0)
#
#     for row in range(num_competitors):
#         team = state.iloc[row]
#         roster = team.tolist()
#         for player in roster:
#             freeagents.remove(player)
#         print(row)
#
#
#     # state = DraftState(rosters, turns, freeagents)
#
# if __name__ == '__main__':
#     get_state()
#
