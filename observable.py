from game_observable import GameObservable


class Observable(GameObservable):
    def __init__(self):
        self.observers = list()
        self.observers_to_delete = list()

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, pins_knocked_down):
        for observer in self.observers:
            observer.update(pins_knocked_down)

        for observer_to_delete in self.observers_to_delete:
            self.observers.remove(observer_to_delete)

        self.observers_to_delete = list()

    def remove_observer(self, observer):
        self.observers_to_delete.append(observer)
