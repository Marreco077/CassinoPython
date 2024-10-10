from pydantic import BaseModel

class Slot:
    def __init__(self, display, value, icon=None):
        self.display = display
        self.value = value
        self.icon = icon  # Adiciona o novo argumento

    def copy(self, deep=False):
        # Lógica de cópia (se necessário)
        return Slot(self.display, self.value, self.icon)
