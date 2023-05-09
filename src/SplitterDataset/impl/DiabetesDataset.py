from src.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from src.SplitterDataset.api.SplitterDataset import SplitterDataset

from sklearn.datasets import load_diabetes


@SplitterDatasetFactory.register("diabetes")
class DiabetesDataset(SplitterDataset):

    def load_data(self):
        return load_diabetes(return_X_y=True)
