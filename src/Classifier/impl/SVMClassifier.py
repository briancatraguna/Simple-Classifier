from src.Classifier.factory.ClassifierFactory import ClassifierFactory
from src.Classifier.api.Classifier import Classifier


@ClassifierFactory.register('svm')
class SVMClassifier(Classifier):

    def fit(self):
        # Fit SVM model
        pass

    def predict(self):
        # Make predictions using SVM model
        pass
