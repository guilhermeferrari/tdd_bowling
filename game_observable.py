from abc import abstractmethod, ABC


class GameObservable(ABC):

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, pins_knocked_down):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass
