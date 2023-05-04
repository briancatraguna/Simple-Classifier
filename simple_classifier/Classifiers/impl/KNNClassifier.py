from simple_classifier.Classifiers.factory.ClassifierFactory import ClassifierFactory
from simple_classifier.Classifiers.api.Classifier import Classifier


@ClassifierFactory.register("KNN")
class KNNClassifier(Classifier):

    def fit(self):
        # Fit KNN model
        pass

    def predict(self):
        # Make predictions using KNN model
        pass
