from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G.clear()
        hubs = DAO.get_all_hub()
        for hub in hubs:
            self.G.add_node(hub["id"], nome =hub["nome"])

        tratte = DAO.get_tratte_connesse()
        for t in tratte:
            hub1 = t["hub1"]
            hub2 = t["hub2"]
            valore_medio = t["totale_valore"]/ t["numero_spedizioni"]
            if valore_medio >= float(threshold): #threshold = valore inserito
                self.G.add_edge(hub1, hub2, peso=valore_medio)


    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes() #funzione che restituisce numero dei nodi

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        #resituisce una lista di tuple: (hub1,hub2,peso)
        edges = []
        for u,v,data in self.G.edges(data=True): #data = True almeno mi resituisce anche il peso dell'edge
            peso = data["peso"]
            edges.append((u,v,peso))
        return edges




