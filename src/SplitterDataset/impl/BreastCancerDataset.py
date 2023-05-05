from src.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from src.SplitterDataset.api.SplitterDataset import SplitterDataset

from sklearn.datasets import load_breast_cancer

@SplitterDatasetFactory.register("breast_cancer")
class BreastCancerDataset(SplitterDataset):

    def load_data(self):
        # Load breast cancer dataset and split into train and test sets
        X, y = load_breast_cancer(return_X_y=True)
        self.X_train, self.X_test, self.y_train, self.y_test = self.splitter.split_data(X, y)
