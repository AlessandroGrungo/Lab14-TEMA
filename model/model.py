import networkx as nx

from database.DAO import DAO
from model.Gene import Gene


class Model:
    def __init__(self):
        self.idMap = {}
        self._grafo = nx.Graph()
        self._nodes = []
        self._edges = []
        self.listaGeni = []
        self.loadListaGeni()

    def loadListaGeni(self):
        self.listaGeni = DAO.getAllGeni()
        self.idMap = {}
        for g in self.listaGeni:
            self.idMap[g.GeneID] = g.Chromosome

    def buildGraph(self):

        for g in self.listaGeni:
            if g.Chromosome != 0:
                self._nodes.append(g.Chromosome)

        self._grafo.add_nodes_from(self._nodes)

        geniConnessi = DAO.getGeniConnessi()

        edges = {}
        for g1, g2, corr in geniConnessi:
            if (self.idMap[g1], self.idMap[g2]) not in edges:
                edges[(self.idMap[g1], self.idMap[g2])] = float(corr)
            else:
                edges[(self.idMap[g1], self.idMap[g2])] += float(corr)

        for keys, value in edges.items():
            self._grafo.add_edge(keys[0], keys[1], weight=value)
        for i in self.get_edges(): print(i)

    def get_nodes(self):
            return self._grafo.nodes()

    def get_edges(self):
            return list(self._grafo.edges(data=True))

    def get_num_of_nodes(self):
            return self._grafo.number_of_nodes()

    def get_num_of_edges(self):
            return self._grafo.number_of_edges()

    def get_sorted_edges(self):
            return sorted(self._grafo.edges(data=True), key=lambda x: x[2]['weight'], reverse=True)

    def get_max(self):
        pesoMax=-1000
        for edge in self.get_edges():
            if edge[2]['weight'] > pesoMax:
                pesoMax = edge[2]['weight']
        return pesoMax


    def get_min(self):
        pesoMin = +1000
        for edge in self.get_edges():
            if edge[2]['weight'] < pesoMin:
                pesoMin = edge[2]['weight']
        return pesoMin

    def num_of_edges_under(self, soglia):
        count = 0
        for edge in self.get_edges():
            if edge[2]['weight'] < soglia:
                count += 1
        return count

    def num_of_edges_upper(self, soglia):
        count = 0
        for edge in self.get_edges():
            if edge[2]['weight'] > soglia:
                count += 1
        return count