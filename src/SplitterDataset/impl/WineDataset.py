from src.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from src.SplitterDataset.api.SplitterDataset import SplitterDataset

from sklearn.datasets import load_wine

@SplitterDatasetFactory.register("wine")
class WineDataset(SplitterDataset):

    def load_data(self):
        # Load wine dataset and split into train and test sets
        X, y = load_wine(return_X_y=True)
        self.X_train, self.X_test, self.y_train, self.y_test = self.splitter.split_data(X, y)
