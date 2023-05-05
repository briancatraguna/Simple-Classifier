import abc

from src.SplitterDataset.api.SplitterDataset import SplitterDataset


class Classifier(abc.ABC):

    def __init__(self, dataset: SplitterDataset):
        self.dataset = dataset

    def fit(self):
        raise NotImplementedError("Subclasses must implement fit method")

    def predict(self):
        raise NotImplementedError("Subclasses must implement predict method")
