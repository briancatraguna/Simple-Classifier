from simple_classifier.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from simple_classifier.SplitterDataset.api.SplitterDataset import SplitterDataset


@SplitterDatasetFactory.register("diabetes")
class DiabetesDataset(SplitterDataset):

    def load_data(self):
        # Load diabetes dataset and split into train and test sets
        pass
