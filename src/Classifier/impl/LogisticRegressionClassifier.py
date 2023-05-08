from src.Classifier.factory.ClassifierFactory import ClassifierFactory
from src.Classifier.api.Classifier import Classifier


@ClassifierFactory.register('logistic')
class LogisticRegressionClassifier(Classifier):

    def fit(self):
        # Fit logistic regression model
        pass

    def predict(self):
        # Make predictions using logistic regression model
        pass
