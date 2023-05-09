from src.Classifier.factory.ClassifierFactory import ClassifierFactory
from src.Classifier.api.Classifier import Classifier


@ClassifierFactory.register("KNN")
class KNNClassifier(Classifier):

    def fit(self):
        # Fit KNN model
        pass

    def predict(self):
        # Make predictions using KNN model
        pass
