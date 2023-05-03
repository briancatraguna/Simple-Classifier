import abc

class Classifier(abc.ABC):

    def __init__(self, dataset):
        self.dataset = dataset

    def fit(self):
        raise NotImplementedError("Subclasses must implement fit method")

    def predict(self):
        raise NotImplementedError("Subclasses must implement predict method")
