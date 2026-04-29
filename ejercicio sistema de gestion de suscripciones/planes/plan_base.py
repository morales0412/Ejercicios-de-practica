from abc import ABC, abstractmethod


class PlanBase(ABC):
    @abstractmethod
    def obtener_costo(self):
        pass
