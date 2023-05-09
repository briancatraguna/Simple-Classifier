from src.Classifier.factory.ClassifierFactory import ClassifierFactory
from src.Classifier.api.Classifier import Classifier


@ClassifierFactory.register('randomforest')
class RandomForestClassifier(Classifier):

    def fit(self):
        # Fit random forest model
        pass

    def predict(self):
        # Make predictions using random forest model
        pass
