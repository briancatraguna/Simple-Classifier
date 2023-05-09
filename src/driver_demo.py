from src.SplitterDataset.impl import BreastCancerDataset, DiabetesDataset, IrisDataset, WineDataset  # noqa
from src.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from src.Classifier.impl import KNNClassifier, LogisticRegressionClassifier, RandomForestClassifier, SVMClassifier  # noqa
from src.Classifier.factory.ClassifierFactory import ClassifierFactory

if __name__ == "__main__":
    dataset_name = "breast_cancer"
    classifier_name = "KNN"
    test_size = 0.3

    dataset = SplitterDatasetFactory.create_instance(dataset_name,
                                                     test_size=test_size)
    classifier = ClassifierFactory.create_instance(classifier_name,
                                                   dataset=dataset)
