from src.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from src.SplitterDataset.api.SplitterDataset import SplitterDataset

from sklearn.datasets import load_iris

@SplitterDatasetFactory.register("iris")
class IrisDataset(SplitterDataset):

    def load_data(self):
        return load_iris(return_X_y=True)