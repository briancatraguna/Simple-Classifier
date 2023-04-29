import abc

from simple_classifier.Classifiers.Classifier import Classifier
from simple_classifier.Datasets.SplitterDatasetFactory import SplitterDatasetFactory


class SplitterDataset(abc.ABC, SplitterDatasetFactory, Classifier):
    def __init__(self, test_size):
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.test_size = test_size
        self.splitter = None

    def load_data(self):
        raise NotImplementedError("Subclasses must implement load_data method")
