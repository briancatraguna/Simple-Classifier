from simple_classifier.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from simple_classifier.SplitterDataset.api.SplitterDataset import SplitterDataset


@SplitterDatasetFactory.register("wine")
class WineDataset(SplitterDataset):

    def load_data(self):
        pass
