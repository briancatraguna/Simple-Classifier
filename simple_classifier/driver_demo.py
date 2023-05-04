from simple_classifier.SplitterDataset.impl import BreastCancerDataset, DiabetesDataset, IrisDataset, WineDataset  # noqa
from simple_classifier.SplitterDataset.factory.SplitterDatasetFactory import SplitterDatasetFactory
from simple_classifier.Classifiers.impl import KNNClassifier, LogisticRegressionClassifier, RandomForestClassifier, SVMClassifier  # noqa
from simple_classifier.Classifiers.factory.ClassifierFactory import ClassifierFactory

if __name__ == "__main__":
    dataset_name = "breast_cancer"
    classifier_name = "KNN"
    test_size = 0.3

    dataset = SplitterDatasetFactory.create_instance(dataset_name,
                                                     test_size=test_size)
    classifier = ClassifierFactory.create_instance(classifier_name,
                                                   dataset=dataset)
