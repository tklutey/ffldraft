import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import configurations

nfl_players = pd.read_csv(configurations.ROOT_DIR + '/data/projections.csv', index_col=0)

positions = nfl_players['Position'].unique()

counter = 1

for position in positions:
    plt.subplot(len(positions), 1, counter)
    x = nfl_players.loc[nfl_players['Position'] == position]
    x = x['Points'].nlargest(n=30)

    size, scale = 1000, 10

    x.plot.hist(grid=True, bins=20, rwidth=0.9,
                       color='#607c8e')
    plt.title(position)
    plt.xlabel('Projected Points')
    plt.ylabel('Counts')
    plt.grid(axis='y', alpha=0.75)

    counter += 1


plt.show()
