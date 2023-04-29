import abc

from simple_classifier.Classifiers.ClassifierProfiler import ClassifierProfiler
from simple_classifier.ModelFactory import ModelFactory


class Classifier(abc.ABC,  ClassifierProfiler, ModelFactory):
    def __init__(self, dataset):
        self.dataset = dataset

    def fit(self):
        raise NotImplementedError("Subclasses must implement fit method")

    def predict(self):
        raise NotImplementedError("Subclasses must implement predict method")

    def score(self):
        raise NotImplementedError("Subclasses must implement score method")
