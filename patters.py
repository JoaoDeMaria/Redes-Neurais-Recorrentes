from abc import ABC

class Observador(ABC):

    @abstractmethod
    def atualizar():
        pass

class Observavel(ABC):

    @abstractproperty
    def _observers() -> List:
        pass
    
    @abstractmethod
    def adicionar_observer(self, observer):
        pass

    @abstractmethod
    def notificar_observers(self, mensagem):
        pass