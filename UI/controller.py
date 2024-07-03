import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    #All’avvio del programma, si crei un grafo semplice, pesato e orientato i cui vertici siano tutti i cromosomi
    #(tabella genes, colonna chromosome, considerando solo i valori diversi da 0).

    def handle_graph(self, e):

        self._model.buildGraph()

        self._view.txt_result.controls.append(ft.Text(
            f"Numero di vertici: {self._model.get_num_of_nodes()}, Numero di archi: {self._model.get_num_of_edges()}"))

        self._view.txt_result.controls.append(ft.Text(
            f"Peso degli archi: Valore minimo -> {self._model.get_min()}, Valore massimo ->{self._model.get_max()}"))

        self._view.update_page()

    def handle_countedges(self, e):

        soglia = float(self._view.txt_name.value)

        if soglia < self._model.get_min() or soglia > self._model.get_max():
            self._view.create_alert("Inserire un valore compreso tra max e min prima citati.")

        self._view.txt_result.controls.append(ft.Text(
            f"Numero di archi sopra alla soglia: {self._model.num_of_edges_under(soglia)}\nNumero di archi sotto la soglia: {self._model.num_of_edges_upper(soglia)}"))

        self._view.update_page()

    def handle_search(self, e):
        pass