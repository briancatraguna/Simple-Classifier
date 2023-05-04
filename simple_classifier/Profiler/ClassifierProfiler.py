from simple_classifier.Classifiers.api.Classifier import Classifier
from simple_classifier.Profiler.Profiler import Profiler
from simple_classifier.Profiler.Display import Display


class ClassifierProfiler:

    def __init__(self, classifiers: list[Classifier],
                 profilers: list[Profiler], display: Display):
        self.classifiers = classifiers
        self.profilers = profilers
        self.display = display

    def train(self):
        # Train all classifiers on dataset
        pass

    def profile_classifiers(self):
        # Run all profilers on all classifiers and display results
        pass

    def display_results(self):
        #
        pass
