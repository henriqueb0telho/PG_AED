from sistema.gestorDestinos.show_destino import show_destino
def show_json(self):
        for destino in self._destinos:
            show_destino(destino)