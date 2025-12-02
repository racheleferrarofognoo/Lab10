import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        #controllo che l'input sia valido
        threshold = self._view.guadagno_medio_minimo.value
        if threshold.isalpha():
            self._view.show_alert("Inserire un valore numerico")
            return

        #costgruisco il grafo
        self._model.costruisci_grafo(threshold)

        numero_nodi = self._model.get_num_nodes()
        numero_archi = self._model.get_num_edges()
        archi = self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.clear()

        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Hubs: {numero_nodi}"))
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Tratte: {numero_archi}"))

        i = 1
        for u,v,w in archi:
            nome_partenza = self._model.G.nodes[u]["nome"] #prendo l'attributo del nodo u del grafo che è nel model
            nome_arrivo = self._model.G.nodes[v]["nome"]
            self._view.lista_visualizzazione.controls.append(
                ft.Text(f"{i}) {nome_partenza} --> {nome_arrivo} -- guadagno medio per spedizione: {w:.2f}€"))
            i+=1
        self._view.update()






