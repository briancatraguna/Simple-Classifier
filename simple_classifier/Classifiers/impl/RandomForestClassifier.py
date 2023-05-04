from simple_classifier.Classifiers.factory.ClassifierFactory import ClassifierFactory
from simple_classifier.Classifiers.api.Classifier import Classifier


@ClassifierFactory.register('randomforest')
class RandomForestClassifier(Classifier):

    def fit(self):
        # Fit random forest model
        pass

    def predict(self):
        # Make predictions using random forest model
        pass
