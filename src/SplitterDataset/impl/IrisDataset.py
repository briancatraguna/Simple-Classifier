from src.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from src.SplitterDataset.api.SplitterDataset import SplitterDataset

from sklearn.datasets import load_iris

@SplitterDatasetFactory.register("iris")
class IrisDataset(SplitterDataset):

    def load_data(self):
        # Load iris dataset and split into train and test sets
        X, y = load_iris(return_X_y=True)
        self.X_train, self.X_test, self.y_train, self.y_test = self.splitter.split_data(X, y)
