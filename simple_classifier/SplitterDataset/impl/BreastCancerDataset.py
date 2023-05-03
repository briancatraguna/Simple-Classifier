from simple_classifier.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from simple_classifier.SplitterDataset.api.SplitterDataset import SplitterDataset

@SplitterDatasetFactory.register("breast_cancer")
class BreastCancerDataset(SplitterDataset):
    def load_data(self):
        # Load breast cancer dataset and split into train and test sets
        pass
