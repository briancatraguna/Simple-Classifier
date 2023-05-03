from simple_classifier.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from simple_classifier.SplitterDataset.api.SplitterDataset import SplitterDataset


@SplitterDatasetFactory.register("iris")
class IrisDataset(SplitterDataset):
    def load_data(self):
        pass
