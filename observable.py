from game_observable import GameObservable


class Observable(GameObservable):
    def __init__(self):
        self.observers = list()

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, pins_knocked_down):
        for observer in self.observers:
            observer.update(pins_knocked_down)

    def remove_observer(self, observer):
        self.observers.remove(observer)
