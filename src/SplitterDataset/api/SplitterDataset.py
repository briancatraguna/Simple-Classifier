import abc

from src.Splitter.Splitter import Splitter


class SplitterDataset(abc.ABC):

    def __init__(self, splitter: Splitter):
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.splitter = splitter
        self.load_data()

    @abc.abstractmethod
    def load_data(self):
        raise NotImplementedError("Subclasses must implement load_data method")
