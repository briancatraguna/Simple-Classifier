from src.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from src.SplitterDataset.api.SplitterDataset import SplitterDataset

from sklearn.datasets import load_breast_cancer


@SplitterDatasetFactory.register("breast_cancer")
class BreastCancerDataset(SplitterDataset):

    def load_data(self):
        return load_breast_cancer(return_X_y=True)
