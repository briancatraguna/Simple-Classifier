import abc

import numpy as np

from src.Splitter.Splitter import Splitter


class SplitterDataset(abc.ABC):

    def __init__(self, splitter: Splitter):
        X, y = self.load_data()
        self.X_train, self.X_test, self.y_train, self.y_test = splitter.split_data(
            X, y)

    @abc.abstractmethod
    def load_data(self) -> np.ndarray:
        raise NotImplementedError("Subclasses must implement load_data method")
