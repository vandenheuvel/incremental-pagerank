from time import clock
from random import randint

from matplotlib import pyplot, cm
from networkx import gnm_random_graph, pagerank
from numpy import meshgrid

from page_rank import IncrementalPageRank

max_nodes_power = 7
max_edges_power = 6

pr_times = list()
ipr_times = list()

for i in range(1, max_nodes_power):
    nodes = 10 ** i
    pr_timesi = list()
    ipr_timesi = list()

    for j in range(max_edges_power):
        edges = 10 ** j
        if edges < 0.5 * nodes ** 2:
            graph = gnm_random_graph(nodes, edges, directed=True)
            for (u, v) in graph.edges():
                graph.edge[u][v]["weight"] = randint(0, 100)

            ipr = IncrementalPageRank(graph, 5, 0.1)
            ipr.initial_walk()
            for _ in range(int(edges / 100)):
                ipr.add_edge(randint(0, round(nodes * 1.2)), randint(0, round(nodes * 1.2)))

            start = clock()
            ipr.update_walk()
            ipr_timesi.append((nodes, edges, clock() - start))

            start = clock()
            pagerank(graph)
            pr_timesi.append((nodes, edges, clock() - start))
        else:
            pr_timesi.append(0)
            ipr_timesi.append(0)

    pr_times.append(pr_timesi)
    ipr_times.append(ipr_timesi)

print(pr_times)
print(ipr_times)

# figure = pyplot.figure()
# ax = figure.gca(projection='3d')
#
# X = range(1, max_nodes_power)
# Y = range(1, max_edges_power)
# X, Y = meshgrid(X, Y)
#
# surface = ax.plot_surface(X, Y, pr_times,
#                           cmap=cm.coolwarm,
#                           linewidth=0,
#                           antialiased=False)
# surface = ax.plot_surface(X, Y, ipr_times,
#                           cmap=cm.coolwarm,
#                           linewidth=0,
#                           antialiased=False)

# pyplot.show()
