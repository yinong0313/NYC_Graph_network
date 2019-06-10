# Build graph. Find insights.
# Step 1: Who is the most popular?
# The code below will return the top 100 people and their degree.

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# load edges from saved pandas df
df_tot = pd.read_csv('edges')
df_tot = df_tot.drop(df_tot.columns[[0]], axis=1)

# build graph
mg = nx.MultiGraph()
subset_whole = tuple(zip(df_tot.node1,df_tot.node2))
for i in range(len(subset_whole)):
    mg.add_edges_from([subset_whole[i]])

# print the most popular 100 people and their degree.
popular_100 = sorted(mg.degree, key=lambda x: (-x[1],x[0]), reverse=False)
print(popular_100)

# Step 2: determine popularity is to look at their PageRank
# Use 0.85 as the damping parameter so that there is a 15% chance of jumping to another vertex at random.

import networkx as nx
import matplotlib.pyplot as plt

mg = nx. Graph()
subset_whole = tuple(zip(df_tot.node1,df_tot.node2))
for i in range(len(subset_whole)):
    mg.add_edges_from([subset_whole[i]])
pagerank_100_temp = nx.pagerank(mg, alpha =0.85)
pagerank_100 = sorted(pagerank_100_temp.items(), key=lambda x: x[1], reverse=True)
print(pagerank_100)

# Step 3: Find out people's connections.
# Who tend to co-occur with each other? Code below will print the 100 edges with the highest weights.

from collections import Counter
from collections import OrderedDict

relation_counts = Counter()
subset_whole = tuple(zip(df_tot.node1,df_tot.node2))

for _ in range(len(subset_whole)):
    for i in range(len(subset_whole[_])):
        if (subset_whole[_][i][0],subset_whole[_][i][1]) in relation_counts:
            relation_counts[tuple(subset_whole[_][i])] += 1
        elif (subset_whole[_][i][1],subset_whole[_][i][0]) in relation_counts:
            relation_counts[tuple((subset_whole[_][i][1],subset_whole[_][i][0]))] += 1
        else:
            relation_counts[tuple(subset_whole[_][i])] = 1
best_friends = sorted(relation_counts.items(),key=lambda x: (-x[1], x[0]), reverse=False)
print(best_friends)
