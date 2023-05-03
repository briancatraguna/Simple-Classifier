from simple_classifier.Classifiers.factory.ClassifierFactory import ClassifierFactory
from simple_classifier.Classifiers.api.Classifier import Classifier

@ClassifierFactory.register('svm')
class SVMClassifier(Classifier):
    def fit(self):
        # Fit SVM model
        pass

    def predict(self):
        # Make predictions using SVM model
        pass
