from simple_classifier.Classifiers.factory.ClassifierFactory import ClassifierFactory
from simple_classifier.Classifiers.api.Classifier import Classifier

@ClassifierFactory.register('logistic')
class LogisticRegressionClassifier(Classifier):
    def fit(self):
        # Fit logistic regression model
        pass

    def predict(self):
        # Make predictions using logistic regression model
        pass
