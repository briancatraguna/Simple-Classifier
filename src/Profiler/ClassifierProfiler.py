from src.Classifier.api.Classifier import Classifier
from src.Profiler.Profiler import Profiler
from src.Profiler.Display import Display


class ClassifierProfiler:

    def __init__(self, classifiers: list[Classifier],
                 profilers: list[Profiler], display: Display):
        self.classifiers = classifiers
        self.profilers = profilers
        self.display = display

    def train(self):
        # Train all Classifier on dataset
        pass

    def profile_classifiers(self):
        # Run all Profiler on all Classifier and display results
        pass

    def display_results(self):
        #
        pass
