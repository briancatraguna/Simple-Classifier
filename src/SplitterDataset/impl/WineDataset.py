from src.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from src.SplitterDataset.api.SplitterDataset import SplitterDataset

from sklearn.datasets import load_wine

@SplitterDatasetFactory.register("wine")
class WineDataset(SplitterDataset):

    def load_data(self):
        return load_wine(return_X_y=True)